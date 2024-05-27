from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database.db import session_manager
from app.config.env import env
from app.versions.route_handler import handle_routing


def init_app(init_db=True):
    

     

    allowed_url=[]

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        if init_db:
            session_manager.init(env["database_url"])
            
        yield
        if session_manager._engine is not None:

            await session_manager.close()
        # app.router.lifespan_context = lifespan        
       
    app:FastAPI = FastAPI(lifespan=lifespan)       

    handle_routing(app=app)
    return app, allowed_url

