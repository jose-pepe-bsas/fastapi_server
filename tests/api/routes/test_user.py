from fastapi.testclient import TestClient
import pytest
from api.routes.users import user_route
from fastapi import FastAPI
from api.routes.users import db
"""user routes"""

app = FastAPI()
app.include_router(user_route)

@pytest.fixture(autouse=True,name="clean_db")
def clean_db():
    db._db = []
    yield
    db._db = []

def test_routes_should_route_user_root():
    client = TestClient(app)
    assert client.get("/users/").status_code == 200

def test_routes_should_route_to_login():
    client = TestClient(app)
    assert client.post("/users/signup/",json={
        "email":"jose.s.contacto@gmail.com",
        "password":"jose321!"
    }).json()["sub"] == "user just register successfully"

def test_login_route_should_only_acept_no_empty_email_and_pass():
    client = TestClient(app)
    resp = client.post("/users/signup/",json={
        "email":" ",
        "password":"\n"
    })
    assert resp.json()["sub"] == "Bad user data entries"
    assert resp.status_code == 403



#TODO: Para probar persistencia usando api, usar el metodo get user/user_id
        
def test_login_should_persist_user_trhought_signup():
    client = TestClient(app)
    client.post("/users/signup/",json={
        "email":"jose.s.contacto@gmail.com",
        "password":"hello123"
    })
    resp = client.get("/users/").json()
    assert resp[0]["email"] == "jose.s.contacto@gmail.com"
    
