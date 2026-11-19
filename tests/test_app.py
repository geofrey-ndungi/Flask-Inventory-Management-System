import unittest
from unittest.mock import Mock, patch

import requests

from app import create_app


class InventoryApiTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app([])
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_create_read_update_and_delete_item(self):
        created = self.client.post(
            "/inventory",
            json={"name": "Tea", "price": 3.5, "quantity": 8},
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.get_json()["id"], 1)

        self.assertEqual(self.client.get("/inventory").get_json(), [created.get_json()])
        self.assertEqual(self.client.get("/inventory/1").get_json()["name"], "Tea")

        updated = self.client.patch("/inventory/1", json={"quantity": 4})
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.get_json()["quantity"], 4)

        deleted = self.client.delete("/inventory/1")
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(self.client.get("/inventory/1").status_code, 404)

    def test_create_and_update_reject_invalid_values(self):
        missing_fields = self.client.post("/inventory", json={"name": "Tea"})
        self.assertEqual(missing_fields.status_code, 400)

        negative_quantity = self.client.post(
            "/inventory",
            json={"name": "Tea", "price": 3.5, "quantity": -1},
        )
        self.assertEqual(negative_quantity.status_code, 400)

        created = self.client.post(
            "/inventory",
            json={"name": "Tea", "price": 3.5, "quantity": 8},
        )
        invalid_update = self.client.patch("/inventory/1", json={"id": 9})
        self.assertEqual(created.status_code, 201)
        self.assertEqual(invalid_update.status_code, 400)
        self.assertEqual(self.client.get("/inventory/1").get_json()["id"], 1)

    @patch("app.requests.get")
    def test_barcode_search_maps_openfoodfacts_product(self, get):
        response = Mock()
        response.json.return_value = {
            "status": 1,
            "product": {
                "code": "123",
                "product_name": "Tea",
                "brands": "Acme",
                "ingredients_text": "Tea leaves",
            },
        }
        get.return_value = response

        result = self.client.get("/products/search?barcode=123")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.get_json()["name"], "Tea")
        self.assertEqual(result.get_json()["brand"], "Acme")
        response.raise_for_status.assert_called_once_with()

    @patch("app.requests.get", side_effect=requests.Timeout("timed out"))
    def test_openfoodfacts_failure_returns_gateway_error(self, get):
        result = self.client.get("/products/search?name=tea")
        self.assertEqual(result.status_code, 502)
        self.assertIn("error", result.get_json())
