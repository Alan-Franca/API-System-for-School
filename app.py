from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from routers.alunos import alunos_router
from routers.cursos import cursos_router
from routers.matriculas import matriculas_router

app = FastAPI(
    title="API de Gestão Escolar",
    description="API para gerenciar alunos, cursos e matrículas.",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alunos_router, tags=["Alunos"])
app.include_router(cursos_router, tags=["Cursos"])
app.include_router(matriculas_router, tags=["Matrículas"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse('static/index.html')