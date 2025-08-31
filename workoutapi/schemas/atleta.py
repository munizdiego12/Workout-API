from typing import Annotated, Optional
from pydantic import Field, PositiveFloat, UUID4
from workoutapi.schemas.base import BaseSchema
from workoutapi.schemas.categoria import CategoriaIn, CategoriaOut
from workoutapi.schemas.centro_treinamento import CentroTreinamentoIn, CentroTreinamentoOut
from datetime import datetime

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoIn, Field(description='Centro de treinamento do atleta')]

class AtletaOut(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador do atleta')]
    created_at: Annotated[datetime, Field(description='Data de criação do atleta')]
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaOut, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoOut, Field(description='Centro de treinamento do atleta')]

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]

