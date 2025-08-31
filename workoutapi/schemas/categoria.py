from typing import Annotated
from pydantic import Field
from workoutapi.schemas.base import BaseSchema

# Schema de Entrada (o que o usuário precisa enviar para criar uma categoria)
class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]

# Schema de Saída (o que a API vai retornar)
class CategoriaOut(CategoriaIn):
    pk_id: Annotated[int, Field(description='Identificador da categoria')]
