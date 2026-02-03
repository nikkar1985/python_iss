import requests

# Κλήση του API για τη θέση του Διεθνούς Διαστημικού Σταθμού
response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

print(f"Ο ISS είναι εδώ: {data['iss_position']}")