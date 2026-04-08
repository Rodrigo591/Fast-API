from fastapi import FastAPI
from app.modules.movie.router import router as mo


app = FastAPI()

app.include_router(mo)

@app.get("/")
def root():
    return {"message": "Hello world"}


@app.on_event("startup")
async def startup_event():
    print("🚀 Iniciando aplicação...")
    print("👉 Acesse: http://localhost:8000/docs\n")
