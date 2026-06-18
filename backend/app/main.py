from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.creditos import router as creditos_router


app = FastAPI(
    title="API de consulta de Creditos",
    description="Desafio Tecnico - Consulta de creditos constituidos",
    version="1.0.0",
)


# Configuracao do CORS para permitir que o Angular (normalmente na porta 4200) acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em producao, substitua pelo dominio do Front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(creditos_router)


@app.get("/health")
def health_check() -> Dict[str, str]:
    """Retorna o status de saude da aplicacao"""
    return {"status": "healrhy"}
