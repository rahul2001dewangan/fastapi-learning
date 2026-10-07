from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Rahul",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date-posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Somu",
        "title": "Python is great for Web Development",
        "content": "Python is a great language for web dev, and FastAPI makes it even better.",
        "date-posted": "April 21, 2025",
    },
]


@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})
