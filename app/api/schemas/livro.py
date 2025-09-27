from typing import Optional
from pydantic import BaseModel, Field


class livroCreated(BaseModel):
    titulo: str = Field(..., min_length=10)
    autor: str = Field(..., min_length=10)
    editora: str = Field(..., min_length=3)
    categoria: int
    ano: Optional[int] = Field(None, le=9999)
    qtd_est: int = Field(default=1)
    disponivel: bool = True


class livroOut(livroCreated):
    id = int
