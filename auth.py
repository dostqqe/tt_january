# from fastapi import APIRouter, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from passlib.context import CryptContext
# from db_interactions.database import sessionLocal
# from db_interactions.models import User
# from datetime import datetime, timedelta
# from jose import jwt
#
#
# router = APIRouter()
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
# secret_key = sec
# algorithm = "HS256"
# access_token_expires_minutes = 60
#
# access_token_expires = datetime.utcnow() + timedelta(minutes=access_token_expires_minutes)
# access_token = jwt.encode({
#     "sub": User.login,
#     "exp": access_token_expires
# }, secret_key, algorithm=algorithm)
#
# pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")
#
# @router.post("/register")
# async def register(login: str, password: str):
#     db = sessionLocal()
#     user = db.query(User).filter(User.login == login).first()
#     if user:
#         raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")
#
#     new_user = User(login=login, password=pwd_context.hash(password))
#     db.add(new_user)
#     db.commit()
#     return {"message": "Пользователь создан"}
