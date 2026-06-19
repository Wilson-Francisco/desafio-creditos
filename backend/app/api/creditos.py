from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.mensageria import enviar_evento_auditoria
from app.db.session import get_db
from app.schemas.credito import CreditoResponse
from app.services.credito import CreditoService


router = APIRouter(prefix="/api/creditos", tags=["Creditos"])


@router.get("/{numeroNfse}", response_model=List[CreditoResponse])
def listar_por_nfse(
    numeroNfse: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
) -> List[CreditoResponse]:
    """Retorna uma lista de créditos constituídos e registra a auditoria."""
    service = CreditoService(db)
    creditos = service.buscar_por_nfse(numeroNfse)

    # Registra o evento de auditoria em segundo plano
    background_tasks.add_task(enviar_evento_auditoria, "NFSE", numeroNfse)

    return creditos


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

    # Registra o evento de auditoria em segundo plano
    background_tasks.add_task(enviar_evento_auditoria, "NUMERO_CREDITO", numeroCredito)

    return credito
