from typing import Optional
from getRoleFromJwt import get_role_from_jwt
from getJwtfromUri import get_jwt_from_uri
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/get-credentials", status_code=status.HTTP_200_OK)
def get_jwt_from_uri_and_role(uri: str):
    try:
        # Call your getJWTfromUri function here with await
        jwt_tokens = get_jwt_from_uri(uri)
        # Call get_role_from_jwt with the obtained tokens
        credentials = get_role_from_jwt(jwt_tokens)

        return credentials
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))