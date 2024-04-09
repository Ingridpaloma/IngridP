import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans mon Api pour le projet BIHAR !"}


def test_predict():
    # Simuler des données de requête pour l'endpoint /predict
    data = {
        "step": 3,
        "start_date": "2024-04-09 00:00:00",
        "end_date": "2024-04-09 12:00:00"
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    # Ajoutez plus d'assertions pour vérifier la réponse, selon votre logique métier


def test_predictions():
    # Envoyer une requête GET à /predictions avec des paramètres de date
    response = client.get("/predictions?start_date=2024-04-09&end_date=2024-04-10")
    assert response.status_code == 200
    # Ajoutez des assertions pour vérifier la réponse, selon votre logique métier

