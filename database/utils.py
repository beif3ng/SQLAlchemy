from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import Author, Genre, Book
from sqlalchemy.orm import selectinload


async def add_author(session: AsyncSession, name: str):
    if not name or len(name.strip()) < 2:
        raise ValueError("Author name must be at least 2 characters long and not empty.")
    author = Author(name=name)
    session.add(author)
    await session.commit()
    return author


async def add_genre(session: AsyncSession, name: str):
    if not name or len(name.strip()) < 2:
        raise ValueError("Genre name must be at least 2 characters long and not empty.")
    genre = Genre(name=name)
    session.add(genre)
    await session.commit()
    return genre


async def add_book(session: AsyncSession, name: str, author_id: int, genre_id: int):
    if not name or len(name.strip()) < 2:
        raise ValueError("Book name must be at least 2 characters long and not empty.")
    author = await session.execute(select(Author).filter_by(id=author_id))
    author = author.scalar_one_or_none()
    if not author:
        raise ValueError(f"No author found with id {author_id}")
    genre = await session.execute(select(Genre).filter_by(id=genre_id))
    genre = genre.scalar_one_or_none()
    if not genre:
        raise ValueError(f"No genre found with id {genre_id}")
    book = Book(name=name, author_id=author_id, genre_id=genre_id)
    session.add(book)
    await session.commit()
    return book


async def get_all_books(session: AsyncSession):
    result = await session.execute(select(Book).options(selectinload(Book.author), selectinload(Book.genre)))
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(
        select(Book).filter_by(id=book_id).options(selectinload(Book.author), selectinload(Book.genre)))
    return result.scalar_one_or_none()


async def delete_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).filter_by(id=book_id))
    book = result.scalar_one_or_none()
    if book:
        await session.delete(book)
        await session.commit()
        return True
    return False
