import requests
from datetime import datetime

username = "hasnian"
token = "245k34b5k234b5345bk2"

pixel_endpoint = "https://pixe.la/v1/users"

pixel_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixel_endpoint, json=pixel_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": token
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = "https://pixe.la/v1/users/hasnian/graphs/graph1"

today = datetime.now()

pixe_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.47",
}

pixel_creation_response = requests.post(url=pixel_creation_endpoint, json=pixe_data, headers=headers)

print(pixel_creation_response.text)