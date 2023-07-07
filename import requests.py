import requests
import json

url = "https://michaelgathara.com/api/python-challenge"


print("Name : Praneeth Eraganaboina  BalzerID: peragana \n")
# Send a GET request to retrieve the challenge
response = requests.get(url)

# Extract the challenges from the response
challenges = response.json()
print (challenges)
print("\n Answers: ")
for p in challenges:
    print("\n",p)
    print("Answer : ",eval(p['problem'][:-1]),"\n")
    
