import boto3
import os
from dotenv import load_dotenv

load_dotenv()

#This function retrieves credentials for the IAM roles associated with the identity pool.
#Run get_jwt_from_uri to get the tokens to be passed into this function
#Returns a dictionary of credentials 

def get_role_from_jwt(tokens):
    identity_pool_id = os.getenv("IDENTITY_POOL_ID")
    region = "ap-southeast-1"
    user_pool_id = os.getenv("USER_POOL_ID")

    # Create a Cognito Identity client
    client = boto3.client('cognito-identity', region_name=region)

    #Get the identity id from the identity pool
    identity_pool_response = client.get_id(
    AccountId= os.getenv("AWS_USER_ID"),
    IdentityPoolId=identity_pool_id,
    Logins={
            f"cognito-idp.{region}.amazonaws.com/{user_pool_id}": tokens['id_token']
    })
    identity_id = identity_pool_response['IdentityId']

    #get credentials for the IAM role using the identity id
    credentials_response = client.get_credentials_for_identity(
    IdentityId = identity_id,
    Logins={
        f"cognito-idp.{region}.amazonaws.com/{user_pool_id}": tokens['id_token']
    }
    )
    temporary_credentials = credentials_response['Credentials']
    return temporary_credentials