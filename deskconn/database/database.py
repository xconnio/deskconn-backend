import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from deskconn.models import Base

load_dotenv()

DATABASE_URL = os.getenv("DESKCONN_DSN", None)
if DATABASE_URL is None or DATABASE_URL == "":
    raise ValueError("'DESKCONN_DSN' missing in environment variables.")

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, autoflush=False, autocommit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
