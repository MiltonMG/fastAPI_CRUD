from fastapi import FastAPI

 #instanciamos fast api
app = FastAPI()

#1. El protocolo que nosotros utilizaraemos para comunicarnos entre la red y nuestro backend es el protocolo http.


# Notacion para indicar que quiero acceder a fastAPI
@app.get('/')
async def root():
    return "Hola Mundo"

# 2. ¿Como comprobamos que nuestro server funciona?
# Para Esto utilizaremos el server que instalamos con FastAPI
# El comndo sera uvicorn main:app --reload (el --reload lo que hace es recargar el server a cada cambio que el server sufra).

# python -m uvicorn main:app --reload -> Comando para correr uvicorn
# detener server CTRL + C

# Con FastAPI se puede documentar muy facil nuestro API
# Utilizando  http://127.0.0.1:8000/docs
# y http://127.0.0.1:8000/redoc