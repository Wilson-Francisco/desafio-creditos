from typing import Dict

from fastapi import FastAPI


app = FastAPI(
    title="API de consulta de Creditos",
    description="Desafio Tecnico - Consulta de creditos constituidos",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> Dict[str, str]:
    """Retorna o status de saude da aplicacao"""
    return {"status": "healrhy"}
