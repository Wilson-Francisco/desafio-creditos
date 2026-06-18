from datetime import date
from decimal import Decimal
from unittest.mock import MagicMock
import pytest
from app.models.credito import Credito
from app.services.credito import CreditoService


@pytest.fixture
def mock_credito() -> Credito:
    """Fixture que cria uma instância fictícia de Credito para os testes."""
    return Credito(
        id=1,
        numero_credito="123456",
        numero_nfse="7891011",
        data_constituicao=date(2024, 2, 25),
        valor_issqn=Decimal("1500.75"),
        tipo_credito="ISSQN",
        simples_nacional=True,
        aliquota=Decimal("5.0"),
        valor_faturado=Decimal("30000.00"),
        valor_deducao=Decimal("5000.00"),
        base_calculo=Decimal("25000.00"),
    )


def test_buscar_por_credito_com_sucesso(mock_credito: Credito) -> None:
    # Arrange (Preparação)
    mock_db = MagicMock()
    service = CreditoService(db=mock_db)

    # Mockando o comportamento do repositório interno
    service.repository.get_by_numero_credito = MagicMock(return_value=mock_credito)

    # Act (Execução)
    resultado = service.buscar_por_credito("123456")

    # Assert (Verificação)
    assert resultado is not None
    assert resultado.numero_credito == "123456"
    assert resultado.numero_nfse == "7891011"
    assert resultado.valor_issqn == Decimal("1500.75")
    service.repository.get_by_numero_credito.assert_called_once_with("123456")


def test_buscar_por_credito_nao_encontrado() -> None:
    # Arrange (Preparação)
    mock_db = MagicMock()
    service = CreditoService(db=mock_db)

    # Repositório retornando None (crédito inexistente)
    service.repository.get_by_numero_credito = MagicMock(return_value=None)

    # Act (Execução)
    resultado = service.buscar_por_credito("000000")

    # Assert (Verificação)
    assert resultado is None
    service.repository.get_by_numero_credito.assert_called_once_with("000000")
