from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def criar_aluno(db: Session, aluno: schemas.AlunoCreate):
    aluno_existente = db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first()

    if aluno_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    novo_aluno = models.Aluno(**aluno.dict())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno
