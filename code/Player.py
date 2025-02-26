import pygame.key

from code.Cont import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        

    def update(self):
        pass

    def move(self):
        # usando 'if' para mover o player na diagonal
        # get_pressed ação de manter prescionado a tecla
        pressed_key = pygame.key.get_pressed()
        # mover player para cima eixo y
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        # mover player para baixo eixo y
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        # mover player para esquerda eixo x
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # mover player para direita eixo x
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
