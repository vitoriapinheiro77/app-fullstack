from sqlalchemy import Column, Integer, String
from database import Base  

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    idade = Column(Integer)
    curso = Column(String)
