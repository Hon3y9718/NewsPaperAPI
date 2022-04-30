from fastapi import FastAPI
from pydantic import BaseModel
from ScrapNewsPaper import NewsPaperData

# Model
class URL(BaseModel):
    url: str

newsPaperAPI = NewsPaperData()
app = FastAPI()

@app.get("/")
async def root():
    data = newsPaperAPI.getNewsPaper()
    return data

@app.post("/getpdf")
async def root(url: URL):
    data = newsPaperAPI.getPDF(url.url)
    return {'url': data}