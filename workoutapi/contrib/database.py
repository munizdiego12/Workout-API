from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Usamos o driver asyncpg para a aplicação, pois ele é assíncrono
DATABASE_URL = "postgresql+asyncpg://workout:workout@localhost:5432/workout"

# Cria a 'engine', o ponto de entrada para o banco de dados
engine = create_async_engine(DATABASE_URL, echo=True)

# Cria uma fábrica de sessões assíncronas
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
