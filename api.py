from fastapi import FastAPI

players={}
server=FastAPI()
@server.get("/player/connect")
async def history(name:str, color:str, position:tuple):
    players.update({name:{"color":color, "position":position}})
@server.get("/player/live")
async def history1(name:str, color:str, position_x:int, position_y:int):
    players.update({name:{"color":color, "position":(position_x, position_y)}})
    return players

