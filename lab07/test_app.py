# lab07/test_app.py - Tests fuer den Dienst. Ausfuehren (aus dem Hauptordner):  python -m pytest lab07 -q
import base64
from fastapi.testclient import TestClient
from lab07.app import app                      # importiert den Dienst - dabei wird das Modell geladen

client = TestClient(app)                       # ruft die Anwendung direkt auf, ohne Server


def b64(pfad):
    return base64.b64encode(open(pfad, "rb").read()).decode()


def test_health():
    r = client.get("/health")
    assert r.json()["status"] == "ok"


def test_kirche():                             # ein gutes Bild -> 200, richtige Klasse, p zwischen 0 und 1
    r = client.post("/predict", json={"image_b64": b64("lab07/kirche.JPEG")})
    assert r.status_code == 200
    assert r.json()["klasse"] == "Kirche"
    assert 0 <= r.json()["p"] <= 1


def test_kein_bild():                          # "hallo" als Base64 -> 422 von unserer Fehlerbehandlung
    r = client.post("/predict", json={"image_b64": "aGFsbG8="})
    assert r.status_code == 422


def test_feld_fehlt():                         # leere Anfrage -> 422 vom Schema
    r = client.post("/predict", json={})
    assert r.status_code == 422


def test_fallschirm():                         # Ihr Test: fallschirm.JPEG -> 200 und Klasse "Fallschirm"
    # TODO 2.4 (Loesung): wie test_kirche: client.post(...) mit b64("lab07/fallschirm.JPEG"), dann zwei assert-Zeilen
    r = client.post("/predict", json={"image_b64": b64("lab07/fallschirm.JPEG")})
    assert r.status_code == 200
    assert r.json()["klasse"] == "Fallschirm"
