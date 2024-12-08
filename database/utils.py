from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import Author, Genre, Book


async def add_author(session: AsyncSession, name: str):
    author = Author(name=name)
    session.add(author)
    await session.commit()
    return author


async def add_genre(session: AsyncSession, name: str):
    genre = Genre(name=name)
    session.add(genre)
    await session.commit()
    return genre


async def add_book(session: AsyncSession, name: str, author_id: int, genre_id: int):
    book = Book(name=name, author_id=author_id, genre_id=genre_id)
    session.add(book)
    await session.commit()
    return book


async def get_all_books(session: AsyncSession):
    result = await session.execute(select(Book).options())
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).filter_by(id=book_id))
    return result.scalar_one_or_none()


async def delete_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(select(Book).filter_by(id=book_id))
    book = result.scalar_one_or_none()
    if book:
        await session.delete(book)
        await session.commit()
        return True
    return False
