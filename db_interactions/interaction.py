from sqlalchemy.ext.asyncio import AsyncSession
from models import User

class UserDAL(): #DataAccessLayer
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, nickname: str, login:str) -> User:
        new_user = User(
            nickname=nickname,
            login=login
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
