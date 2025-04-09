from sqlalchemy import Column, Integer, String
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    curso = Column(String(100), nullable=False)
