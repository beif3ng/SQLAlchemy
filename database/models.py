from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


# Модель для книги
class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)  # Первичный ключ
    name: Mapped[str] = mapped_column(nullable=False)  # Название книги
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"), nullable=False)  # Ссылка на автора
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), nullable=False)  # Ссылка на жанр


# Модель для автора
class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True)  # Первичный ключ
    name: Mapped[str] = mapped_column(nullable=False)  # Имя автора


# Модель для жанра
class Genre(Base):
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(primary_key=True)  # Первичный ключ
    name: Mapped[str] = mapped_column(nullable=False)  # Название жанра
