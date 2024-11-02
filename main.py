from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

allowedNames = ["fifi", "xversone", "ala"]


@app.get("/", response_class=HTMLResponse)
def read_root(request : Request, name):
    return templates.TemplateResponse(
        request=request, name="landing-page.html", context={"name": name}
    )


class MyForm(BaseModel):
    name : str

@app.post("/obierz")
def form(form : Annotated[MyForm, Form()]):
    ...


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

