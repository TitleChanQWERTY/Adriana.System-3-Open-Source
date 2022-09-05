import pygame

from random import randint

import op


class BallRosa(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (42, 42))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.add(group)

    def update(self):

        if self.posY < 975:
            self.posY += self.speed
        else:
            self.kill()
        self.rect.x = self.posX
        self.rect.y = self.posY


class Shota(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename, group):
        self.select = randint(1, 2)
        self.y = randint(220, 1000)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        if op.health_shota <= 0:
            op.Score += 75
            op.health_shota = 225
            self.kill()

        if self.select == 1:
            if self.rect.y <= self.y:
                self.rect.y += self.speed
            elif self.rect.y >= self.y and self.rect.x <= 890:
                self.image = pygame.image.load('Sprite/enemy/shota_right.png')
                self.image = pygame.transform.scale(self.image, (45, 60))
                self.rect.x += self.speed
            else:
                self.kill()
        if self.select == 2:
            if self.rect.y <= self.y:
                self.rect.y += self.speed
            elif self.rect.y >= self.y and self.rect.x >= 5:
                self.image = pygame.image.load('Sprite/enemy/shota_right.png')
                self.image = pygame.transform.scale(self.image, (45, 60))
                self.image = pygame.transform.flip(self.image, 85, 0)
                self.rect.x -= self.speed
            else:
                self.kill()


class drone(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (99, 99))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        sfx = pygame.mixer.Sound('Audio/SFX/2.wav')
        if op.healthDrone <= 0:
            sfx.play()
            op.Score += 1255
            op.isMoveLevel = True
            op.isActiveLevel = True
            op.healthDrone += 550
            self.kill()

        if self.rect.y <= 25:
            op.isMoveDrone = False
        elif self.rect.y >= 210:
            op.isMoveDrone = True

        if self.rect.y < 210 and not op.isMoveDrone:
            self.rect.y += 2
        elif op.isMoveDrone:
            self.rect.y -= 1


class Darts(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.select = randint(1, 2)
        self.y = randint(220, 1000)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (54, 61))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        if op.health_shota <= 0:
            op.isMoveLevel = True
            op.Score += 75
            op.health_shota = 75
            self.kill()

        if self.select == 1:
            if self.rect.y <= self.y:
                self.rect.y += self.speed
            elif self.rect.y >= self.y and self.rect.x <= 890:
                self.rect.x += self.speed
            else:
                self.kill()

        if self.select == 2:
            if self.rect.y <= self.y:
                self.rect.y += self.speed
            elif self.rect.y >= self.y and self.rect.x >= 5:
                self.rect.x -= self.speed
            else:
                self.kill()


daddySprite = ('Sprite/enemy/daddy_1.png', 'Sprite/enemy/daddy_2.png')


class Daddy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, second, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (54, 61))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = second
        self.speed = speed
        self.add(group)

    def update(self):
        if self.Frame == 25:
            self.Frame = 0
        if self.Frame == 5:
            self.image = pygame.image.load(daddySprite[0]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (54, 61))
        if self.Frame == 20:
            self.image = pygame.image.load(daddySprite[1]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (54, 61))
        self.Frame += 1

        if self.rect.x <= 850:
            self.rect.x += self.speed
        else:
            self.kill()


bossSprite = ('Sprite/enemy/boss/eye_1.png', 'Sprite/enemy/boss/eye_2.png', 'Sprite/enemy/boss/eye_3.png',
              'Sprite/enemy/boss/eye_4.png', 'Sprite/enemy/boss/eye_6.png', 'Sprite/enemy/boss/eye_7.png',
              'Sprite/enemy/boss/eye_8.png', 'Sprite/enemy/boss/eye_9.png', 'Sprite/enemy/boss/eye_10.png',
              'Sprite/enemy/boss/bossFinal/eye_1.png')

frame = 0


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bossSprite[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (142, 142))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        global frame
        if op.bossHealth <= 5:
            self.kill()

        if frame == 120:
            frame = 0

        if frame == 10:
            if op.bossHealth >= 650:
                self.image = pygame.image.load(bossSprite[1]).convert_alpha()
            else:
                self.image = pygame.image.load(bossSprite[9]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 20:
            self.image = pygame.image.load(bossSprite[2]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 30:
            self.image = pygame.image.load(bossSprite[3]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 40:
            self.image = pygame.image.load(bossSprite[4]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 50:
            self.image = pygame.image.load(bossSprite[5]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 60:
            self.image = pygame.image.load(bossSprite[6]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 70:
            self.image = pygame.image.load(bossSprite[7]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 80:
            if op.bossHealth >= 650:
                self.image = pygame.image.load(bossSprite[8]).convert_alpha()
            else:
                self.image = pygame.image.load(bossSprite[9]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))
        if frame == 90:
            if op.bossHealth >= 650:
                self.image = pygame.image.load(bossSprite[0]).convert_alpha()
            else:
                self.image = pygame.image.load(bossSprite[9]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (142, 142))

        frame += 1
