from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///example.db", echo=False)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
