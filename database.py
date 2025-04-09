# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # Importando o Base de models para garantir que as tabelas sejam criadas

# Substitua com a URL de conexão correta para seu banco MySQL
SQLALCHEMY_DATABASE_URL = "mysql://user:password@localhost/cadastro_alunos"

# Criando o engine de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"charset": "utf8mb4"})

# Criando a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
