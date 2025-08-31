from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.models.base import BaseModel
from typing import List

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)

    # O mesmo tipo de relacionamento: "Um centro de treinamento pode ter VÁRIOS atletas".
    atletas: Mapped[List['AtletaModel']] = relationship(back_populates='centro_treinamento')