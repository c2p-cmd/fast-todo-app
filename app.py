from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.todo import ItemManager, TodoItemContent

app = FastAPI()
favicon_path = 'to-do-list.ico'

item_manager = ItemManager()

# mount static files
app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="./templates")

@app.get('/favicon.ico', include_in_schema=False, response_class=FileResponse)
def favicon():
    return FileResponse(favicon_path)

@app.get("/", response_class=HTMLResponse, summary="Returns all ToDo items in a list")
def items(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html', context={'items': item_manager.get_all()}
    )

@app.post("/add/", response_class=JSONResponse, summary="Adds new todo item")
def add_item(request: Request, item: TodoItemContent):
    item_manager.add_new(item)
    return {
        "status": "ok",
    }


@app.put("/toggle/", response_class=JSONResponse, summary="Toggles todo item")
def toggle_status(request: Request, item_id: str):
    try:
        item_manager.toggle_status(id=item_id)
        return {
            "status": "ok",
        }
    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "message": e.message,
            },
            status_code=404,
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=7860, reload=True)
