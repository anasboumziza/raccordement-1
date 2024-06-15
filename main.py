import pandas as pd
from batiment import Batiment
from infra import Infra

def read_csv_and_instantiate_objects(csv_file):
    instantiated_batiments = {}
    instantiated_infras = {}

    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        id_batiment = row['id_batiment']
        id_infra = row['infra_id']

        if id_batiment not in instantiated_batiments:
            instantiated_batiments[id_batiment] = Batiment(id_batiment, row['nb_maisons'])

        if id_infra not in instantiated_infras:
            infra_type = row['infra_type']
            longueur = row['longueur']
            instantiated_infras[id_infra] = Infra(id_infra, infra_type, longueur)

        instantiated_batiments[id_batiment].ajouter_infra(instantiated_infras[id_infra])

    return instantiated_batiments

def display_buildings_and_infras(instantiated_batiments):
    for id_batiment, batiment in instantiated_batiments.items():
        print(f"Batiment ID: {id_batiment}")
        print(f"Number of houses: {batiment.nb_maisons}")
        print("Associated Infras:")
        for infra in batiment.connected_infras:
            print(f"  Infra ID: {infra.infra_id}, Type: {infra.infra_type}, Length: {infra.longueur}")
        print()

if __name__ == "__main__":
    csv_file = 'reseau_en_arbre.csv'
    instantiated_batiments = read_csv_and_instantiate_objects(csv_file)
    display_buildings_and_infras(instantiated_batiments)