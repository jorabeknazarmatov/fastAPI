import uvicorn
from models import Base
import db
from fastapi import FastAPI
import schemas


app = FastAPI()
crud = db.DB_CRUD()



# Все пользователи
@app.get(path="/users", summary="Все пользователи", tags=["Users"])
def all_user():
    return crud.all_users()

# Добавить пользователя
@app.post(path='/users/add', summary="Добавить пользователя", tags=["Users"])
def add_user(user: schemas.User):
    return crud.add_user(name=user.name, email=user.email)

@app.put(path='/users/edit/name', summary='Изменить имя пользователя', tags=['Users'])
def update_name(user: schemas.EditName):
    return crud.update_name(id=user.id, name=user.name)

@app.post(path='/posts/add', summary='Добавить пост', tags=['Users'])
def add_post(post: schemas.Post):
    return crud.add_posts(id=post.user_id, post_title=post.title, post_content=post.content)

@app.delete(path='/users/{id}/delete', summary='Удалить пользователя', tags=['Users'])
def del_user(id: int):
    return crud.del_user(id=id)

if __name__ == "__main__":
    Base.metadata.create_all(db.engine)
    uvicorn.run('main:app', reload=True)