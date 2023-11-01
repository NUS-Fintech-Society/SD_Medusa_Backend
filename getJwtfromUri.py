import os
import requests
from dotenv import load_dotenv

load_dotenv()

#This function retrieves JSON Web Tokens (JWT) from an authorization URI, handling the OAuth 2.0 authorization code grant flow.
#Testing : Login to the hosted UI, copy the redirected URI and call getJWTfromUri(uri). 
#If you mess up you will have to click on "View Hosted UI" again to generate another uri as this function will no longer work after the first time.
#Returns a dictionary of tokens 

def getJWTfromUri(uri):
    domain = os.getenv("DOMAIN")
    client_id = os.getenv("CLIENT_ID")

    #Get the code from the url
    start_index = uri.index('code=') + len('code=')
    authorization_code = uri[start_index:]

    # Construct the token endpoint URL
    token_endpoint = f"https://{domain}/oauth2/token"

    # Set the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Set the data
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code" : authorization_code,
        "redirect_uri": "https://localhost"
    }

    # Make the POST request
    response = requests.post(token_endpoint, headers=headers, data=data)

    print(response.status_code)
    tokens = {
        "id_token" : response.json().get('id_token'),
        "access_token" : response.json().get('access_token'),
        "refresh_token" : response.json().get('refresh_token')
    }
    return tokens