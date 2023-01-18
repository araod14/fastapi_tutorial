#FastApi
from fastapi import FastAPI
from routes.person import person



app = FastAPI(
    title='api de person',
    description='habla claro',
    version='0.0.9'
)

app.include_router(person)