from fastapi import FastAPI, Request
import models
from routers import auth, todos, admin, user
from database import engine
from fastapi.templating import Jinja2Templates

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/healthy')
def health_check():
    return {'status': 'healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)
