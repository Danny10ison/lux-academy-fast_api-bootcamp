from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_root(name: str):
    return {"greeting": f"Hello! {name}, you're welcome"}