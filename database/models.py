from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"), nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), nullable=False)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    books = relationship("Book", back_populates="genre")
