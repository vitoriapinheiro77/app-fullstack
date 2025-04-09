from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    email: str
    idade: int
    curso: str

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True
