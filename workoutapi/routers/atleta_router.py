from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from workoutapi.contrib.dependencies import DatabaseDependency
from workoutapi.models import AtletaModel, CategoriaModel, CentroTreinamentoModel
from workoutapi.schemas import AtletaIn, AtletaOut, AtletaUpdate

router = APIRouter()

@router.post(
    "/",
    summary="Criar um novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    categoria_nome = atleta_in.categoria.nome
    ct_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"A categoria {categoria_nome} não foi encontrada.")

    ct = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=ct_nome))).scalars().first()
    if not ct:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"O centro de treinamento {ct_nome} não foi encontrado.")

    try:
        atleta_model = AtletaModel(**atleta_in.model_dump(exclude={'categoria', 'centro_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = ct.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
        await db_session.refresh(atleta_model)

    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocorreu um erro ao inserir os dados no banco")

    return atleta_model

