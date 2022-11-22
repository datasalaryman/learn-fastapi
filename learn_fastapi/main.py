from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello, I'm CRUD API"

@app.post("/create")
async def create():
    return "Creating table in DB"

@app.get("/read")
async def read():
    return "Reading table in DB"

@app.post("/update")
async def update():
    return "Updating table in DB"

@app.get("/delete")
async def delete():
    return "Deleting table in DB"