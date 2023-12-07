import uvicorn

from fastapi import FastAPI

from routing.comics import routers as comics_router


app = FastAPI(title='Comics')

app.include_router(comics_router.router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run("app:app", host='localhost', port=8000, reload=True)