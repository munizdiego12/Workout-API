from workoutapi.models.base import BaseModel
from sqlalchemy import Float, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    
    # --- AQUI ESTÃO AS CONEXÕES (CHAVES ESTRANGEIRAS) ---
    
    # 1. Conexão com Categoria
    # ForeignKey('categorias.pk_id') cria a restrição no banco de dados.
    # Diz que o valor nesta coluna DEVE existir na coluna 'pk_id' da tabela 'categorias'.
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    # relationship() cria a conexão no lado do Python/SQLAlchemy.
    # Permite que você acesse o objeto Categoria inteiro a partir de um Atleta (ex: meu_atleta.categoria.nome).
    # back_populates='atletas' conecta com o relacionamento que definimos no CategoriaModel.
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atletas')
    
    # 2. Conexão com Centro de Treinamento
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atletas')