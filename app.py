from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.todo import ItemManager

app = FastAPI()

item_manager = ItemManager()

# mount static files
app.mount('/static', StaticFiles(directory='./static'), name='static')

templates = Jinja2Templates(directory='./templates')

@app.get('/', response_class=JSONResponse, summary="Returns all ToDo items in a list")
def items(request: Request):
    return {
        'items' : item_manager.get_all()
    }
    # return templates.TemplateResponse(
    #     request=request, name='index.html', context={'items': item_manager.get_all()}
    # )

@app.post('/add/{name}', response_class=JSONResponse)
def add_item(request: Request, content: str):
    item_manager.add_new(content=content)
    return {
        'status' : 'ok'
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=7860, reload=True)
