# SQLAlchemy

An async SQLAlchemy demo project paired with an aiogram Telegram bot. Implements a simple library management system (books, authors, genres) to demonstrate async ORM session patterns, CRUD operations, and multi-database driver support.

## What It Demonstrates

- Defining ORM models with `DeclarativeBase` and `Mapped` / `mapped_column` (SQLAlchemy 2.0 style)
- Async session management via `async_sessionmaker`
- Full async CRUD: insert, select by ID, delete, list all
- ORM relationships (`relationship()` with `back_populates`)
- Database-agnostic design: same models work with SQLite, PostgreSQL, or MySQL via driver swap

## Tech Stack

| Layer | Technology |
|---|---|
| ORM | SQLAlchemy 2.0 (async) |
| Default DB | SQLite via `aiosqlite` |
| Alt drivers | `asyncpg` (PostgreSQL), `aiomysql` (MySQL) |
| Telegram bot | aiogram 3 |

## Data Model

```
Author ──< Book >── Genre
```

| Model | Fields |
|---|---|
| `Author` | `id`, `name` |
| `Genre` | `id`, `name` |
| `Book` | `id`, `name`, `author_id` (FK), `genre_id` (FK) |

## Project Structure

```
SQLAlchemy/
├── main.py              # Entry point: seeds data, runs queries
├── database/
│   ├── db.py            # Async engine and session factory
│   ├── models.py        # Book, Author, Genre ORM models
│   └── utils.py         # CRUD helper functions
└── requirements.txt
```

## Getting Started

```bash
git clone https://github.com/Nezdeshniy/SQLAlchemy.git
cd SQLAlchemy
pip install sqlalchemy aiosqlite aiogram
python main.py
```

This will create `example.db`, seed it with sample authors, genres, and books, then demonstrate querying and deletion.

## Switching the Database

The engine URL in `database/db.py` can be swapped without changing the models:

| Database | URL format |
|---|---|
| SQLite (default) | `sqlite+aiosqlite:///example.db` |
| PostgreSQL | `postgresql+asyncpg://user:pass@host/db` |
| MySQL | `mysql+aiomysql://user:pass@host/db` |

## CRUD Operations

The `database/utils.py` module exposes the following async helpers:

| Function | Description |
|---|---|
| `add_author(session, name)` | Insert a new author |
| `add_genre(session, name)` | Insert a new genre |
| `add_book(session, name, author_id, genre_id)` | Insert a new book |
| `get_all_books(session)` | Return all books |
| `get_book_by_id(session, book_id)` | Return a single book by ID |
| `delete_book_by_id(session, book_id)` | Delete a book and return success |
