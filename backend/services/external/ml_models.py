import requests


def add_wanted_person(folder_name: str, image_name: str) -> dict:
    url = "http://34.107.31.175:8002/api/post/add_wanted"
    payload = {"folder": folder_name, "image": image_name}
    response = requests.post(url, json=payload)
    return response.json()


def match_found_person(found_image_name: str):

    url = "http://34.107.31.175:8002/api/post/search"

    payload = {
        "filename": found_image_name,
        "threshold": 0.94,
    }

    response = requests.post(url, json=payload)
    print(response)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("Error in matching found person")

    return response.json()
