from flask import Blueprint, request, jsonify
from google.cloud import storage
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
from dotenv import load_dotenv
import dspy
import os
from dspy import GROQ
from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine

load_dotenv()


posting_bp = Blueprint("post", __name__, url_prefix="/post")

def download_file(filepath, destiny):
    bucketname = "dataface-hackaton"
    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    bucket = storage_client.get_bucket(bucketname)
    blob = bucket.blob(filepath)
    blob.download_to_filename(destiny)
    print("downloaded")

def upload_file(blob_name, path_to_file):
    bucketname = "dataface-hackaton"
    storage_client = storage.Client.from_service_account_json("cloud_credentials.json")
    bucket = storage_client.get_bucket(bucketname)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

@posting_bp.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    threshold = data["threshold"]
    
    filename = data["filename"]
    filepath = "found/" + filename
    image_to_search = "./image.jpg"
    download_file(filepath=filepath,destiny=image_to_search)
    filename = "data.pt"
    filepath = filename
    embeddings = 'data.pt'
    download_file(filepath=filepath, destiny=embeddings)

    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20) 
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    img = Image.open(image_to_search)
    face, prob = mtcnn(img, return_prob=True) 
    emb = resnet(face.unsqueeze(0)).detach() 
    
    saved_data = torch.load(embeddings)
    embedding_list = saved_data[0] 
    name_list = saved_data[1] 
    dist_list = [] 
    
    for idx, emb_db in enumerate(embedding_list):
        dist = torch.dist(emb, emb_db).item()
        dist_list.append(dist)

    result = []
    for i in range(len(dist_list)):
        if dist_list[i] < threshold:
            r = {}
            r["name"] = name_list[i]
            r["distance"] = dist_list[i]
            result.append(r)
    return jsonify(result), 200


@posting_bp.route("/add_wanted", methods=["POST"])
def add_wanted():
    filename = "data.pt"
    filepath = filename
    embeddings = 'data.pt'
    download_file(filepath=filepath, destiny=embeddings)
    print("downloaded data")

    existing_data = torch.load(embeddings)
    embedding_list, name_list = existing_data
    data = request.get_json()
    print(data["folder"])
    print(data["image"])
    image_path = "in-search/" + data["folder"] + "/" + data["image"]+".jpg"
    image_embedding = "new_wanted.jpg"
    download_file(filepath=image_path, destiny=image_embedding)
    print("downloaded image")
    image_embedding = Image.open(image_embedding)
    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20) 
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    face, prob = mtcnn(image_embedding, return_prob=True) 

    if face is not None and prob>0.90:
        emb = resnet(face.unsqueeze(0))
        embedding_list.append(emb.detach()) 
        name_list.append(data["folder"])
    data = [embedding_list, name_list]
    torch.save(data, 'data.pt')
    blob_name = "data.pt"
    upload_file(blob_name, "data.pt")
    return jsonify(message="Successfully added"),200


@posting_bp.route("/find_similar", methods=["POST"])
def find_similar():
    data = request.get_json()
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    search_person = data["search"]
    available_person = data["available"]
    distance = 0
    for keys in search_person:

        if keys not in available_person.keys():
            continue

        word1 = search_person[keys][0]
        word2 = available_person[keys]
        print(word1)
        print(word2)

        word1_tokens = tokenizer(word1, return_tensors='pt')
        word2_tokens = tokenizer(word2, return_tensors='pt')

        # Get BERT embeddings
        with torch.no_grad():
            word1_outputs = model(**word1_tokens)
            word2_outputs = model(**word2_tokens)

        # Extract the embeddings
        word1_embedding = word1_outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        word2_embedding = word2_outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

        print(cosine(word1_embedding, word2_embedding))
        # Compute distances
        distance += cosine(word1_embedding, word2_embedding) * search_person[keys][1]
    return jsonify(distance),200
