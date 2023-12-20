import uvicorn
import asyncio


async def main(port:str="8080",app:str=f"server:app"):
    try:
        config = uvicorn.Config(app, port=port, log_level="info", reload=True)
        server = uvicorn.Server(config)
        server.run()
        logging.log(msg="server has started sucefully", level=logging.INFO)

    except Exception as err:
        logging.error(msg=f"Failed to starting server: {err} ")



if __name__ == "__main__":
    asyncio.run(main())
