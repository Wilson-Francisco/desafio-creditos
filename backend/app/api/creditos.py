from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.credito import CreditoResponse
from app.services.credito import CreditoService


router = APIRouter(prefix="/api/creditos", tags=["Creditos"])


@router.get("/{numeroNfse}", response_model=List[CreditoResponse])
def listar_por_nfse(
    numeroNfse: str, db: Session = Depends(get_db)
) -> List[CreditoResponse]:
    """Retorna uma lista de creditos constituidos com base no numero da NFS-e"""
    service = CreditoService(db)
    creditos = service.buscar_por_nfse(numeroNfse)
    return creditos


@router.get("/credito/{numeroCredito}", response_model=CreditoResponse)
def obter_por_credito(
    numeroCredito: str, db: Session = Depends(get_db)
) -> CreditoResponse:
    """Retorna os detalhes de um crédito constituído específico."""
    service = CreditoService(db)
    credito = service.buscar_por_credito(numeroCredito)
    if not credito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crédito com o número {numeroCredito} não foi encontrado.",
        )
    return credito
