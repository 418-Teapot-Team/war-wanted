from flask import Flask
from flask_cors import CORS
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
from google.cloud import storage
from services import api_bp
from pathlib import Path


def download_dataset():
    bucketname = 'dataface-hackaton'
    prefix = 'in-search/'
    dl_dir = './in-search'

    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    bucket = storage_client.get_bucket(bucketname)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        if blob.name.endswith("/"):
            continue
        file_split = blob.name.split("/")
        directory = "/".join(file_split[0:-1])
        Path(directory).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(blob.name) 

def initialize_embeddings():
    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20) 
    resnet = InceptionResnetV1(pretrained='vggface2').eval() 

    # TODO: DOWNLOAD FOLDERS WITH WANTED PEOPLE ID AND IMAGES
    download_dataset()
    dataset=datasets.ImageFolder('./in-search') 
    idx_to_class = {i:c for c,i in dataset.class_to_idx.items()} 

    def collate_fn(x):
        return x[0]

    loader = DataLoader(dataset, collate_fn=collate_fn)

    face_list = [] # list of cropped faces from photos folder
    name_list = [] # list of names corrospoing to cropped photos
    embedding_list = [] # list of embeding matrix after conversion from cropped faces to embedding matrix using resnet

    for img, idx in loader:
        face, prob = mtcnn(img, return_prob=True) 
        if face is not None and prob>0.90: # if face detected and porbability > 90%
            emb = resnet(face.unsqueeze(0)) # passing cropped face into resnet model to get embedding matrix
            embedding_list.append(emb.detach()) # resulten embedding matrix is stored in a list
            name_list.append(idx_to_class[idx]) # names are stored in a list
    data = [embedding_list, name_list]
    torch.save(data, 'data.pt') # saving data.pt file

    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    bucketname = "dataface-hackaton"

    bucket = storage_client.get_bucket(bucketname)
    blob_name = 'data.pt'
    blob = bucket.blob(blob_name)

    blob.upload_from_filename('data.pt')


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(api_bp)
    initialize_embeddings()
    print(app.url_map)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8003)
