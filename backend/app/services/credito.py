from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.credito import Credito
from app.repositories.credito import CreditoRepository


class CreditoService:
    def __init__(self, db: Session):
        self.repository = CreditoRepository(db)

    def buscar_por_credito(self, numero_credito: str) -> Optional[Credito]:
        """Gerencia a busca por numero do credito"""
        return self.repository.get_by_numero_credito(numero_credito)

    def buscar_por_nfse(self, numero_nfse: str) -> List[Credito]:
        """Gerencia a busca por numero da NFS-e"""
        return self.repository.get_by_numero_nfse(numero_nfse)
