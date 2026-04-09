from fastapi import FastAPI
import numpy as np
import random

app = FastAPI()

data = {
    "Marks" : random.sample(range(100),10) 
}

@app.get("/")
def index():
    return {"message":"okh"}

@app.get("/check")
def show_array():
    return data
    