from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def get_status():
    """
    Endpoint simples que retorna o estado atual da aplicação.
    Em um sistema real, poderia verificar disponibilidade de serviços,
    uso de CPU, banco de dados etc.
    """
    return {"status": "ok", "uptime": 99.9}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
