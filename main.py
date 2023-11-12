# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. import Libraries
import uvicorn  # For ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


# 4. Route with a parameter
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to FastAPI Practice': f'{name}'}


# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# After running, can open these webpages:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/Welcome
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/Welcome?name=PM
