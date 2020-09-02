import requests


response = requests.get("https://photos.google.com/photo/AF1QipO1IOvdARrBe1De0vj0PGfhaanRiTnBLvUVUXid")

print(response.text)
