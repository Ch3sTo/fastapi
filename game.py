import block as b
import pygame
import requests
from dataclasses import dataclass

class Player:
    def __init__(self, x, y, w, h, color, name):
        self.name=name
        self.body=pygame.Rect(275, 275, w, h)

        self.color=color
        self.nameplate=self.create_nameplate()
        #self.pos=list(self.body.center)
    def show(self):
        pygame.draw.rect(pg, self.color, self.body)
        pg.blit(self.nameplate, (self.body.x, self.body.y - 20))
    def create_nameplate(self):
        font=pygame.font.Font(None, 20)
        name_plate=font.render(self.name, True, "white")
        return name_plate

name=input()
color=input()
session=requests.Session()
adapter=requests.adapters.HTTPAdapter()
session.mount("http://", adapter)
pygame.init()
pg=pygame.display.set_mode((600, 600))
fps=pygame.time.Clock()
players={}
#b_1=block.Block(300, 300, 0, 0, 100, 100, "green")
all_blocks=[]
players_param={}
posx=0
posy=0

while True:
    if name not in players:
        live=session.get(f"http://127.0.0.1:8000/player/live/?name={name}&color={color}&position_x=300&position_y=300")
        players_param.update(live.json())
        print(players_param)
        for player_name in players_param:

            players.update({player_name:Player(players_param[player_name]["position"][0], players_param[player_name]["position"][1], 50, 50, players_param[player_name]["color"], player_name)})





    else:
        print(posx)
        live = session.get(f"http://127.0.0.1:8000/player/live/?name={name}&color={color}&position_x={posx}&position_y={posy}")
        players_param.update(live.json())
        for player_name in players_param:
            if player_name not in players:
                print(players_param[player_name])
                players.update({player_name:Player(0, 0, 50, 50, players_param[player_name]["color"], player_name)})
            if player_name!=name:

                players[player_name].body.x= players_param[player_name]["position"][0] - players_param[name]["position"][0] + 275
                players[player_name].body.y= players_param[player_name]["position"][1] - players_param[name]["position"][1] + 275
    for block in all_blocks:
        block.move(players_param[name]["position"][0], players_param[name]["position"][1])
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:

            all_blocks.append(b.Block(players[name].body.x, players[name].body.y, players_param[name]["position"][0], players_param[name]["position"][1], event.pos[0]/2, event.pos[1]/2, 100, 100, "green"))
        if event.type==256:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                posy-=20
            if event.key==pygame.K_a:
                posx-=20
            if event.key==pygame.K_s:
                posy+=20
            if event.key==pygame.K_d:
                posx+=20
    pg.fill((0, 0, 0))
    for block in all_blocks:
        block.show(pg)
    for player in players:
        players[player].show()
    print(players_param)
    pygame.display.flip()
    fps.tick(60)

