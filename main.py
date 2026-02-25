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
    else:
        return None
@server.get("/dogs/{god}")
async def dog_info(god):
    if god=="ержан":
        return ":D"
    else:
        return "здеся таких нет"