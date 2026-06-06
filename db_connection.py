import psycopg
import bcrypt
from fastapi import HTTPException
from passw import STR_CONN

class DataBaseConn():
    def __init__(self):
        self.STR_CONN=STR_CONN
        self.inicialization()
        
    def add_client(self,username,password,email):
        #cadastra um cliente na tabela clients
        hash_password=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        with psycopg.connect(self.STR_CONN) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("""INSERT INTO clients (username,password,email) VALUES (%s,%s,%s)""",(username,hash_password,email,))
                    conn.commit()
                except Exception as error:
                    print("Ocorreu um erro ao cadastrar o cliente: ",error)
                    raise HTTPException(status_code=409,detail="Dados inválidos!")
    
    def show_clients(self):
        #RETORNA UMA TUPLA COM TODOS OS CLIENTES
        with psycopg.connect(self.STR_CONN) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT (username,email) FROM clients")
                clients=cursor.fetchall()
                return clients
   
    def show_client(self,id):
        #RETORNA UMA TUPLA COM UM CLIENTE
        with psycopg.connect(STR_CONN) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""SELECT (username,email) FROM clients WHERE id=%s""",(id,))
                client=cursor.fetchone()
                if client:
                    return client
                else: raise HTTPException(status_code=404,detail="Cliente não encontrado!")
            

        
    def inicialization(self):
        #inicializa todas as tabelas do banco de dados
        with psycopg.connect(self.STR_CONN) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
                                id SERIAL PRIMARY KEY,
                                username VARCHAR(100) NOT NULL,
                                password TEXT NOT NULL,
                                email TEXT NOT NULL
                               )""")
                conn.commit()
                cursor.execute("""CREATE TABLE IF NOT EXISTS technicians (
                               id SERIAL PRIMARY KEY,
                               username VARCHAR(100) NOT NULL,
                               password TEXT NOT NULL,
                               email TEXT NOT NULL
                               )""")
                conn.commit()