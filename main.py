from fastapi import FastAPI
import numpy as np

app = FastAPI()

arr = np.array([10,20,40,30,70])

@app.get("/")
def index():
    return {"message":"okh"}

@app.get("/check")
def show_array():
    return {"Array" : arr }
    