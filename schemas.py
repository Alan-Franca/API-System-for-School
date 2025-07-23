from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Matricula(BaseModel):
    aluno_id: int
    curso_id: int

    class Config:
        from_attributes = True
        from_attributes = True

Matriculas = List[Matricula]

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    telefone: Optional[str] = None

    class Config:
        from_attributes = True

Alunos = List[Aluno]

class Curso(BaseModel):
    nome: str
    codigo: str
    descricao: str

    class Config:
        from_attributes = True

Cursos = List[Curso]