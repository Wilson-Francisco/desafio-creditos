from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.credito import CreditoResponse
from app.services.credito import CreditoService
from app.core.mensageria import enviar_evento_auditoria

router = APIRouter(prefix="/api/creditos", tags=["Creditos"])


@router.get("/{numeroNfse}", response_model=List[CreditoResponse])
def listar_por_nfse(
    numeroNfse: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
) -> List[CreditoResponse]:
    """Retorna uma lista de créditos constituídos e registra a auditoria."""
    service = CreditoService(db)
    creditos = service.buscar_por_nfse(numeroNfse)

    background_tasks.add_task(enviar_evento_auditoria, "NFSE", numeroNfse)

    # Conversão explícita para satisfazer a tipagem estrita do Mypy
    return [CreditoResponse.from_orm(c) for c in creditos]


@router.get("/credito/{numeroCredito}", response_model=CreditoResponse)
def obter_por_credito(
    numeroCredito: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
) -> CreditoResponse:
    """Retorna os detalhes de um crédito específico e registra a auditoria."""
    service = CreditoService(db)
    credito = service.buscar_por_credito(numeroCredito)
    if not credito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crédito com o número {numeroCredito} não foi encontrado.",
        )

    background_tasks.add_task(enviar_evento_auditoria, "NUMERO_CREDITO", numeroCredito)

    # Conversão explícita para satisfazer a tipagem estrita do Mypy
    return CreditoResponse.from_orm(credito)
