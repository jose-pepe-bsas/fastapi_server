import os
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.server import main

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "hola"}


#TODO: Aprender a testear el inicio del servidor uvicorn sin acoplarlo a fastapi 
def test_server_should_run_on_localhost():
    client = TestClient(app)
    main(app="tests:test_server:app")
    assert client.get("/").json() == {"msg":"hola"}

    
