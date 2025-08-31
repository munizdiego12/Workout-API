from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.models.base import BaseModel
from typing import List # Usaremos isso para o relacionamento

class CategoriaModel(BaseModel):
    # __tablename__ é o nome que a tabela terá no banco de dados PostgreSQL.
    __tablename__ = 'categorias'

    # Mapped[str] diz ao Python que o tipo deste atributo é uma string.
    # mapped_column(String(40)) diz ao banco de dados para criar uma coluna
    # do tipo VARCHAR com tamanho máximo de 40 caracteres.
    # unique=True garante que não haverá duas categorias com o mesmo nome.
    nome: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)

    # Este é o relacionamento que diz: "Uma categoria pode estar associada a uma LISTA de atletas".
    # back_populates='categoria' é a "mágica" que conecta este lado do relacionamento
    # com o lado do atleta, mantendo tudo sincronizado.
    atletas: Mapped[List['AtletaModel']] = relationship(back_populates='categoria')