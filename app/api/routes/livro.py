from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/livro",
    tags=["Livros"]
)


@router.post("/cadastrar", response_model=livroOut, status_code=status.HTTP_201_CREATED)
async def adicionar_livro(payload=livroCreated, db: AsyncSession = Depends(get_db)):
    """
    :param payload: Dados do livro conforme shecma.
    :param db: Inicia a sessão.
    :return: Retorna livro criado (id)
    """

    # Passando atributo por atributo

    novo = Livro(
        titulo=payload.titulo.strip(),
        autor=payload.autor.strip(),
        editora=payload.editora.strip(),
        categoria=payload.categoria,
        ano=payload.ano,
        qtd_est=payload.qtd_est,
        disponivel=payload.disponivel
    )

    # Passando chave e valor dinamincamente por atributo
    novoT = Livro(**dict(payload))

    db.add(novoT)
    await db.flush()
    await db.refresh(novo)
    return livro_to_out(novo)
