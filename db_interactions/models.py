from sqlalchemy import Column, Integer, String, ForeignKey

from db_interactions.database import Base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    publication_date = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    genres = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=False)
    birthday = Column(String, nullable=False)

class Author_Book(Base):
    __tablename__ = 'author_book'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    author_id = Column(Integer, ForeignKey('author.id'))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    books_taken = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, nickname={self.nickname}, login={self.login})>"

class User_Book(Base):
    __tablename__ = 'user_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


class token_expired(Base):
    __tablename__ = 'token_expired'
    id = Column(Integer, primary_key=True)
    token = Column(String, nullable=False)
