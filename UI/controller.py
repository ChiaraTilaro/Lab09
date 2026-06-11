import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_aeroporti(self, e):
        if self._view.txt_distanza_minima == "":
            self._view.txt_result.controls.append(
            ft.Text("Attenzione, inserire una distanza minima")
        )
            return

        distanza_minima = self._view.txt_distanza_minima.value
        self._model.grafo(distanza_minima)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumEdges} vertici")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumNodes} nodi")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Elenco archi e relativa distanza:")
        )
        allEdges = self._model.getAllEdges()
        for arco in allEdges:
            self._view.txt_result.controls.append(
                ft.Text(f"{arco[0]} -- avgDist: {self._model.getAvgDist(arco[0] , arco[1])}")
        )
            self._view.update_page()
