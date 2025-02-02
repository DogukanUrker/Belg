from fastapi import FastAPI, Response

from .services.staticBadge import staticBadgeGenerate
from .utils.logger import logger

app = FastAPI()

logger.info("App is started")


@app.get("/badge/{label}/{text}/{color}/{theme}")
def staticBadge(
    label: str = "Belg", text: str = ".dev", color: str = "rose", theme: str = "dark"
):
    return Response(
        content=staticBadgeGenerate(label=label, text=text, color=color, theme=theme),
        media_type="image/svg+xml",
    )
