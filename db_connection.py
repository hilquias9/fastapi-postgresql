import psycopg
import bcrypt
from fastapi import HTTPException
from passw import STR_CONN

class DataBaseConn():
    def __init__(self):
        self.STR_CONN=STR_CONN
        
    def add_client(self,username,password,email):
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
        with psycopg.connect(self.STR_CONN) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT (username,email) FROM clients")
                clients=cursor.fetchall()
                return clients