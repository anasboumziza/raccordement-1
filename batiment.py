from infra import Infra

class Batiment:
    def __init__(self, id_batiment, nb_maisons):
        self.id_batiment = id_batiment
        self.nb_maisons = nb_maisons
        self.connected_infras = []

    def ajouter_infra(self, infrastructure):
        self.connected_infras.append(infrastructure)

    def supprimer_infra(self, infrastructure):
        if infrastructure in self.connected_infras:
            self.connected_infras.remove(infrastructure)

    def calculate_difficulty(self):
        total_difficulty = sum(infra.calculate_difficulty(self.nb_maisons) for infra in self.connected_infras)
        return total_difficulty