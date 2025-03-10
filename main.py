import os
from db_interactions.models import User
from fastapi import FastAPI
from authx import AuthX, AuthXConfig
app = FastAPI()

config = AuthXConfig
config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
config.JWT_ACCESS_COOKIE_NAME = "acces_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

@app.post("/registration")
def registration(creds: User):
    pass
