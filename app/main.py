from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Based Adaptive Input Sanitization Engine (AISE) is running."}
