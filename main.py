from fastapi import FastAPI
server=FastAPI()
@server.get("/")
async def return_massage():
    return {"message": "helloooo"}
@server.get("/cats/{cat}")
async def cat_info(cat):
    if cat=="барсик":
        return "барсик серый"
    elif cat=="вася":
        return "вася прозрачный"