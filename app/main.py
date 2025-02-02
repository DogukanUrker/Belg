from fastapi import FastAPI, Response

from .services.staticBadge import staticBadgeGenerate

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Beg.dev"}


@app.get("/badge/{label:path}/{text:path}/{color}/{theme}")
def staticBadge(
    label: str = "Belg", text: str = ".dev", color: str = "rose", theme: str = "dark"
):
    return Response(
        content=staticBadgeGenerate(label=label, text=text, color=color, theme=theme),
        media_type="image/svg+xml",
    )
