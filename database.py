from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ('postgresql+asyncpg://postgres:0000@localhost/TeskTaskDataBase')

engine = create_async_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, class_=AsyncSession)
Base = declarative_base()
