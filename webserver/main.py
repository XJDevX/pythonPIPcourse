import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4,5,6,7,8,9,10]

@app.get("/contacts", response_class = HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Hola soy un parrafo</p>
    """

def run():
    store.getCategories()

if __name__ == "__main__":
    run()