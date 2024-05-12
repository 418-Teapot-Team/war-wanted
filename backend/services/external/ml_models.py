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


def match_person_by_fields(input_person: dict, all_in_search_persons: list[dict]):
    url = "http://34.107.31.175:8002/api/post/find_similar"

    # remove empty fields
    input_person = {k: [str(v), 1] for k, v in input_person.items() if v}

    for person in all_in_search_persons:
        # remove empty fields
        person = {k: str(v) for k, v in person.items() if v}

        payload = {"search": input_person, "available": person}

        print(payload)
        response = requests.post(url, json=payload)

        print("SIMILARITY:", response.text)
        break
