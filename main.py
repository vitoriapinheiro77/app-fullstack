from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
import models
from aluno_routes import router as aluno_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Instância do FastAPI
app = FastAPI()

# Configuração de CORS para permitir o acesso do frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Libera o frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas do arquivo aluno_routes
app.include_router(aluno_router)
