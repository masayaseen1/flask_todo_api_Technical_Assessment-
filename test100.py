import requests

url = "http://127.0.0.1:5000/tasks"

for i in range(1, 101):
    requests.post(url, json={"description": f"Task number {i}"})
