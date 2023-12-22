import uvicorn
import logging
import asyncio
from api.routes.users import user_route
from fastapi import FastAPI
app =FastAPI()
app.include_router(user_route)

def main(port:str="8080",app:str=f"server:app"):
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.WARNING, filename="logs/log", filemode="w+")
    try:
        config = uvicorn.Config(app, port=port, log_level="info", reload=True)
        server = uvicorn.Server(config)
        server.run()
        logging.log(msg="server has started sucefully", level=logging.INFO)

    except Exception as err:
        logging.error(msg=f"Failed to starting server: {err} ")



if __name__ == "__main__":
    main()
