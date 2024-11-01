from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import settings

engine = create_async_engine(settings.db.url)
session_factory = async_sessionmaker(bind=engine, autoflush=True, autocommit=False)

Base = declarative_base(metadata=MetaData(schema="participants_manager"))
