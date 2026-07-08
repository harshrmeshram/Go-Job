from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title='GoJob API', version='0.1.0')


@app.get('/health')
def health_check() -> JSONResponse:
    return JSONResponse({'status': 'ok', 'service': 'api'})


@app.get('/')
def root() -> JSONResponse:
    return JSONResponse({'message': 'GoJob API is running'})
