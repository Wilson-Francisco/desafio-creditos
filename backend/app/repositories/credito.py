from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.credito import Credito


class CreditoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_numero_credito(self, numero_credito: str) -> Optional[Credito]:
        """Busca um credito constituido especifico pelo numero de credito"""
        stmt = select(Credito).where(Credito.numero_credito == numero_credito)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_numero_nfse(self, numero_nfse: str) -> List[Credito]:
        """Retorna uma lista de credito constituido com base no numero da NFS-e"""
        stmt = select(Credito).where(Credito.numero_nfse == numero_nfse)
        return list(self.db.execute(stmt).scalars().all())
