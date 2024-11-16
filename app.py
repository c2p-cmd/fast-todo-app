from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.todo import ItemManager, TodoItemContent

app = FastAPI(title="Fast ToDo App")
favicon_path = "to-do-list.ico"

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

item_manager = ItemManager()

# mount static files
app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="./templates")


@app.get("/favicon.ico", include_in_schema=False, response_class=FileResponse)
def favicon():
    return FileResponse(favicon_path)


@app.get("/", response_class=HTMLResponse, summary="Returns all ToDo items in a list")
def items(request: Request):
    items = item_manager.get_all()
    response = templates.TemplateResponse(
        request=request, name="index.html", context={"items": items}
    )
    response.headers["Cache-Control"] = "no-store"
    return response


@app.post("/add/", response_class=JSONResponse, summary="Adds new todo item")
def add_item(item: TodoItemContent):
    item_manager.add_new(item)
    return {
        "status": "ok",
    }


@app.put("/update", response_class=JSONResponse, summary="Updates todo item")
def toggle_status(item_id: str, status: bool):
    try:
        item_manager.update_status(id=item_id, new_status=status)
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


@app.delete(
    "/item/", response_class=JSONResponse, summary="Deletes specified todo item"
)
def delete_item(request: Request, item_id: str):
    try:
        item_manager.remove_item(id=item_id)
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
