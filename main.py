#fastapi dev main.py
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