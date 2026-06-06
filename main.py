#fastapi dev main.py

# status codes (200, 201, 404, 409...)
# parâmetros de rota
# query parameters
# validação com Pydantic
from fastapi import FastAPI
from db_connection import DataBaseConn


app=FastAPI()
data_base=DataBaseConn()

@app.post("/user/register")
def sesson(username:str,password:str,email:str):
    data_base.add_client(username=username,password=password,email=email)
    return {"MSG":"Cliente cadastrado com sucesso!"}

@app.get("/clients")
def show_clients():
    clients=data_base.show_clients()
    return {"MSG":clients}

@app.get("/clients/{id}")
def show_client(id:int):
    client=data_base.show_client(id)
    return {"MSG":{"nome":client[0][0],"email":client[0][1]}}