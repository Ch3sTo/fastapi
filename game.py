import pygame
import requests
from dataclasses import dataclass

class Player:
    def __init__(self, x, y, w, h, color):
        self.body=pygame.Rect(x, y, w, h)
        self.color=color
        #self.pos=list(self.body.center)
    def show(self):
        pygame.draw.rect(pg, self.color, self.body)
name=input()
color=input()
pygame.init()
pg=pygame.display.set_mode((600, 600))
fps=pygame.time.Clock()
players={}
players_param={}

while True:
    if name not in players:
        live=requests.get(f"http://127.0.0.1:8000/player/live/?name={name}&color={color}&position_x=300&position_y=300")
        players_param.update(live.json())
        print(players_param)
        for player_name in players_param:

            players.update({player_name:Player(players_param[player_name]["position"][0], players_param[player_name]["position"][1], 50, 50, players_param[player_name]["color"])})





    else:
        live = requests.get(f"http://127.0.0.1:8000/player/live/?name={name}&color={color}&position_x={players[name].body.x}&position_y={players[name].body.y}")
        players_param.update(live.json())
        for player_name in players_param:
            if player_name not in players:
                players.update({player_name:Player(players_param[player_name]["position"][0], players_param[player_name]["position"][1], 50, 50, players_param[player_name]["color"])})
            players[player_name].body.x=players_param[player_name]["position"][0]
            players[player_name].body.y=players_param[player_name]["position"][1]
    for x in pygame.event.get():
        if x.type==256:
            pygame.quit()
        if x.type==pygame.KEYDOWN:
            if x.key==pygame.K_w:
                players[name].body.y-=20
            if x.key==pygame.K_a:
                players[name].body.x-=20
            if x.key==pygame.K_s:
                players[name].body.y+=20
            if x.key==pygame.K_d:
                players[name].body.x+=20
    pg.fill((0, 0, 0))
    for player in players:
        players[player].show()
    print(players_param)
    pygame.display.flip()
    fps.tick(60)

