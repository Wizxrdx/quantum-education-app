import flet
from src.QuantumEducationApp import QuantumEducationApp


def main(page: flet.Page):
    page.title = "Quantum Education App"
    QuantumEducationApp(page)


flet.app(target=main)
