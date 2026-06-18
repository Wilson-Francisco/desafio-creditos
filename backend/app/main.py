from typing import Dict
from fastapi import FastAPI
from app.api.creditos import router as creditos_router


app = FastAPI(
    title="API de consulta de Creditos",
    description="Desafio Tecnico - Consulta de creditos constituidos",
    version="1.0.0",
)


# Inclui as rotas de consulta de creditos na aplicacao
app.include_router(creditos_router)


@app.get("/health")
def health_check() -> Dict[str, str]:
    """Retorna o status de saude da aplicacao"""
    return {"status": "healrhy"}
