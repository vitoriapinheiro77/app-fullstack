from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/alunos/", response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return crud.criar_aluno(db=db, aluno=aluno)

@router.get("/alunos/", response_model=list[schemas.Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    return crud.listar_alunos(db)
