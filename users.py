from fastapi import FastAPI
from pydantic import BaseModel #Nos sirve para crear modelos de nuestra informacion


app = FastAPI()

#Definimos la entidad de un usuario
class User(BaseModel): 
    id: int
    name: str
    lastname: str
    url: str
    age: int | str

# ¿Que es una entidad?
# Significado de Entidad: En bases de datos, una entidad es la representación de un objeto o concepto del mundo real que se describe en una base de datos.

users_list = [
    User(id = 1,name = 'Milton', lastname = 'Jeremias', url = 'www.miltongalindo.com',age = '23'),
    User(id = 2,name = 'Oscar', lastname = 'Jeremias', url = 'www.miltongalindo.com',age = '23'),
    User(id = 3,name = 'Rafael', lastname = 'Jeremias', url = 'www.miltongalindo.com',age = '23'),
    User(id = 4,name = 'anonimo', lastname = 'Jeremias', url = 'www.miltongalindo.com',age = 23)
    ]


# GET -------------------------------

# LISTAR TODOS LOS USUARIOS

@app.get('/users') # Listar todos los usuarios
async def users():
    return users_list


# LLAMAR USUARIO POR PATH ID

@app.get('/users/{id}') # Listar todos los usuarios
async def user(id: int):

    return search_user(id)
    
# LLAMAR USUARI POR QUERY

@app.get('/usersquery') # Listar todos los usuarios
async def user(id: int, name: str):

    return search_user(id)
     


#Cuando utilizar path y cuando Query ? 
#Path para parametros que son fijos y son necesarios para realizar busquedas, como por ejemplo el users/1 <- ese uno es necesario para traer la informacion del usuario 1

#Query cuando queremos indicarle un limite de datos por ejemmplo a la pagina users/?limit=10 <- nos traera solo 10 registros

# POST ------------------------------- (Crear)

@app.post('/users')
async def user(user: User): 
    if type(search_user(user.id)) == User:
        return {"Error:":" El usuario ya existe"}
    else:
        users_list.append(user)

# PUT ------------------------------- (Actualizar)

@app.put('/users')
async def user(user: User):
    if type(search_user(user.id)) == User:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user

    else:
        return {"Error:":" El usuario no existe"}


# DELETE ------------------------------- (Eliminar)

@app.delete('/users/{id}')
async def user(id: int):
    if type(search_user(id)) == User:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]

    else:
        return {"Error:":" El usuario no existe"}



# FUNCIONES --------------------------------

# Funcion para filtrar
def search_user(id: int):
    #Codigo para filtrar un array de objetos
    users = filter(lambda user: user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"Eroor":"No se encuentra el usuario"}

