import unittest
from unittest import mock

from flask import Flask

from app import main


class SwaggerInitializationTests(unittest.TestCase):
    def test_initialize_swagger_handles_missing_dependency(self):
        app = Flask(__name__)

        with mock.patch("flasgger.Swagger", side_effect=ImportError("flasgger unavailable")):
            main.initialize_swagger(app)

        self.assertEqual(app.config["SWAGGER"]["title"], "TravelOps AI API")
        self.assertIn("description", app.config["SWAGGER"])


if __name__ == "__main__":
    unittest.main()
