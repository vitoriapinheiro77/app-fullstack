from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, models
from database import get_db

router = APIRouter()

@router.get("/alunos/", response_model=List[schemas.Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    alunos = db.query(models.Aluno).all()
    return alunos
