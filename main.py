from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
 return {"message": "Hello World, SOO ULRICH a deployé son premier API "}