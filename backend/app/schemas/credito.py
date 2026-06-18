from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator


class CreditoResponse(BaseModel):
    numero_credito: str = Field(..., serialization_alias="numeroCredito")
    numero_nfse: str = Field(..., serialization_alias="numeroNfse")
    data_constituicao: date = Field(..., serialization_alias="dataConstituicao")
    valor_issqn: Decimal = Field(..., serialization_alias="valorIssqn")
    tipo_credito: str = Field(..., serialization_alias="tipoCredito")
    simples_nacional: str = Field(..., serialization_alias="simplesNacional")
    aliquota: Decimal
    valor_faturado: Decimal = Field(..., serialization_alias="valorFaturado")
    valor_deducao: Decimal = Field(..., serialization_alias="valorDeducao")
    base_calculo: Decimal = Field(..., serialization_alias="baseCalculo")

    @field_validator("simples_nacional", mode="before")
    @classmethod
    def transformar_simples_nacional(cls, v: bool | str) -> str:
        """Transforma o booleano do banco de dados em 'Sim' ou 'Não' para o JSON."""
        if isinstance(v, bool):
            return "Sim" if v else "Não"
        return v

    class Config:
        from_attributes = True
        populate_by_name = True
