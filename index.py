from typing import Optional

from fastapi import FastAPI

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database="coronadb"
)

mycursor = mydb.cursor()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


