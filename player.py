import pygame

import op


class Player(pygame.sprite.Sprite):
    def __init__(self, speed, health, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (42, 62))
        self.rect = self.image.get_rect(center=(op.RES[0] // 2, op.RES[1] - 55))
        self.speed = speed
        self.health = health

    def move(self):
        if op.isUp and self.rect.y >= 45:
            self.rect.y -= self.speed
        if op.isDown and self.rect.y <= 915:
            self.rect.y += self.speed

        if op.isLeft and self.rect.x >= 35:
            self.image = pygame.image.load('Sprite/player/ioann_right.png')
            self.image = pygame.transform.scale(self.image, (40, 60))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x -= self.speed
        elif op.isRight and self.rect.x <= 615:
            self.image = pygame.image.load('Sprite/player/ioann_right.png')
            self.image = pygame.transform.scale(self.image, (40, 60))
            self.rect.x += self.speed
        else:
            self.image = pygame.image.load('Sprite/player/ioann_idle.png')
            self.image = pygame.transform.scale(self.image, (42, 62))

        if op.isShift:
            self.speed = 6.5
        else:
            self.speed = 11.5

    def update(self):
        if op.Player <= 0.5:
            op.isDIEplayer = True
