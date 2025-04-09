from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Cria as tabelas no banco (se ainda não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência pra obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para cadastrar um aluno
@app.post("/alunos/", response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    return crud.criar_aluno(db=db, aluno=aluno)

# Rota para listar todos os alunos
@app.get("/alunos/", response_model=list[schemas.Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    return crud.listar_alunos(db)

from fastapi import FastAPI
from aluno_routes import router as aluno_router  # ou importando de crud.py, se for o caso

app = FastAPI()

# Incluindo as rotas de aluno no app FastAPI
app.include_router(aluno_router)

