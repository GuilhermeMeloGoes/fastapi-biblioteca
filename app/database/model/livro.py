from app.database.db import Base
from sqlalchemy import Integer, Column, String, Boolean, CheckConstraint


class Livro(Base):
    """

    Modelo ORM para tabela 'livro'.

    - 'id': PK autoincrement
    - 'titulo': Titulo (obrigatorio)
    - 'autor': Autor (obrigatorio)
    - 'editora': Editora (obrigatorio)
    - 'categoria': Categoria (enum, obrigatorio)
    - 'ano': Ano de Publicação
    - 'quantidade': Quantidade de Livros (Default=1)
    - 'disponivel': Booleano de disponibilidade (Default=True)

    """
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String, index=True, nullable=False)
    autor = Column(String, index=True, nullable=False)
    editora = Column(String, index=True, nullable=False)
    categoria = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)
    qtd_est = Column(Integer, default=1)
    disponivel = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        CheckConstraint("disponivel in (0, 1))", name="ck_disponivel_bool")
    )


