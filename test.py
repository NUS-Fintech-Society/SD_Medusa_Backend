from getJwtfromUri import get_jwt_from_uri
from getRoleFromJwt import get_role_from_jwt

#Place redirect URI in "" to test, after logging into the hosted UI. you may have to set the resultant
#credentials to perform further S3 operations
tokens = get_jwt_from_uri("")
credentials = get_role_from_jwt(tokens)
#print(tokens)
#print(credentials)