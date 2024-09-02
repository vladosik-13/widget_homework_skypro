import json
import unittest
from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount


class TestGetTransactionAmount(unittest.TestCase):

    @patch('requests.request')
    def test_get_transaction_amount_rub(self, mock_request):
        transaction = {
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "code": "RUB"
                }
            }
        }

        # Проверьте, что функция возвращает ожидаемое значение
        result = get_transaction_amount(transaction)
        self.assertEqual(result, 1000.0)


@patch('requests.request')
def test_get_transaction_amount_usd(self, mock_request):
    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {
                "code": "USD"
            }
        }
    }

    # Имитация ответа API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"result": 4200})  # Пример: 50 USD = 4200 RUB
    mock_request.return_value = mock_response

    result = get_transaction_amount(transaction)
    self.assertEqual(result, 4200.0)
