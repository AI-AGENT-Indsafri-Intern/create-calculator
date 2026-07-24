from fastapi import FastAPI

app= FastAPI()

@app.get("/Subtraction")
def subtract(a:float, b:float):
    return{
        "message":a-b
    }
