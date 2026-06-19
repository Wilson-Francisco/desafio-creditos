from datetime import date
from decimal import Decimal

from sqlalchemy import Boolean, Date, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Credito(Base):
    __tablename__ = "credito"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    numero_credito: Mapped[str] = mapped_column(String(50), nullable=False)
    numero_nfse: Mapped[str] = mapped_column(String(50), nullable=False)
    data_constituicao: Mapped[date] = mapped_column(Date, nullable=False)
    valor_issqn: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    tipo_credito: Mapped[str] = mapped_column(String(50), nullable=False)
    simples_nacional: Mapped[bool] = mapped_column(Boolean, nullable=False)
    aliquota: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    valor_faturado: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    valor_deducao: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    base_calculo: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
