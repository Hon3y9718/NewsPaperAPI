from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from ScrapNewsPaper import NewsPaperData

# Model
class URL(BaseModel):
    url: str

newsPaperAPI = NewsPaperData()
app = FastAPI()

@app.get("/")
async def home():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/getnewspaper/{name}")
async def NewsPaper(name: str):
    data = newsPaperAPI.getNewsPaper(name)
    return data

@app.post("/getpdf")
async def pdf(url: URL):
    data = newsPaperAPI.getPDF(url.url)
    return {'url': data}