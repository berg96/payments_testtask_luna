from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config.settings import settings

engine = create_async_engine(settings.get_db_url(), poolclass=NullPool)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
