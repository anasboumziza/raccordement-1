class Infra:
    def __init__(self, infra_id, infra_type, longueur):
        self.infra_id = infra_id
        self.infra_type = infra_type
        self.longueur = longueur

    def calculate_difficulty(self, num_houses_connected):
        return self.longueur / num_houses_connected
