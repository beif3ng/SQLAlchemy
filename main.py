import asyncio

from database import Base, engine, session, get_all_books, get_book_by_id, add_author, add_genre, add_book, \
    delete_book_by_id


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session() as async_session:

        await add_author(async_session, "Jane Austen")
        await add_author(async_session, "Charles Dickens")
        await add_author(async_session, "Leo Tolstoy")

        await add_genre(async_session, "Romance")
        await add_genre(async_session, "Fiction")
        await add_genre(async_session, "Historical Fiction")

        await add_book(async_session, "Pride and Prejudice", 1, 1)
        await add_book(async_session, "Great Expectations", 2, 2)
        await add_book(async_session, "War and Peace", 3, 3)
        await add_book(async_session, "Anna Karenina", 3, 1)

        books = await get_all_books(async_session)
        print("All Books:")
        for book in books:
            print(f"ID: {book.id}, name: {book.name}, author ID: {book.author_id}, genre ID: {book.genre_id}")

        book_info = await get_book_by_id(async_session, 1)
        if book_info:
            print(f"\nBook with ID {1}:")
            print(f"Name: {book_info.name}, Author ID: {book_info.author_id}, Genre ID: {book_info.genre_id}")
        else:
            print(f"\nBook with ID {1} not found.")

        delete_result = await delete_book_by_id(async_session, 2)
        print(f"\nBook with ID {2} deleted: {delete_result}")

        updated_books = await get_all_books(async_session)
        print("\nUpdated Books:")
        for book in updated_books:
            print(f"ID: {book.id}, name: {book.name}, author ID: {book.author_id}, genre ID: {book.genre_id}")





if __name__ == '__main__':
    asyncio.run(main())
