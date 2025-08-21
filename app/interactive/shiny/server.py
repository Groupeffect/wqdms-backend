import sys
from shiny import App, ui, render, reactive
from starlette.routing import Mount
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(BASE_DIR.__str__())
print("########")
print(sys.path)
from interactive.django_setup import start_django_in_notebook

start_django_in_notebook()

from interface import models

geom = models.Geometry.objects.first().geom
data = getattr(geom, "geojson", '{"test":"test"}')

import requests


class ShinyAPIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {"Content-Type": "application/json"}

    def create(self, endpoint, data):
        return self._request("POST", endpoint, data)

    def read(self, endpoint, params=None):
        return self._request("GET", endpoint, params)

    def update(self, endpoint, data):
        return self._request("PUT", endpoint, data)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)

    def _request(self, method, endpoint, payload=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}


app_ui = ui.page_fluid(
    ui.input_text("name", "Enter your name:", ""),
    ui.output_text_verbatim("greeting"),
    ui.input_text_area("json_display", "JSON Data", data, rows=10),
)


def server(input, output, session):
    @output()
    @render.text
    def greeting():
        return f"Hello, {input.name()}!"


app_shiny = App(app_ui, server)
# app_static = StaticFiles(directory=".")
routes = [
    Mount("/shiny", app=app_shiny),
    # Mount('/static', app=app_static),
]

app = Starlette(routes=routes)
