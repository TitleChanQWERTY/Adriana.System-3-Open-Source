import pygame

import op

enemyDie = ('Sprite/partical/enemy_die/enemy_die_1.png', 'Sprite/partical/enemy_die/enemy_die_2.png',
            'Sprite/partical/enemy_die/enemy_die_3.png', 'Sprite/partical/enemy_die/enemy_die_4.png',
            'Sprite/partical/enemy_die/enemy_die_5.png', 'Sprite/partical/enemy_die/enemy_die_6.png',
            'Sprite/partical/enemy_die/enemy_die_7.png', 'Sprite/partical/enemy_die/enemy_die_8.png',
            'Sprite/partical/enemy_die/enemy_die_9.png')

playerDie = ('Sprite/partical/player_die/player_die_1.png', 'Sprite/partical/player_die/player_die_2.png',
             'Sprite/partical/player_die/player_die_3.png', 'Sprite/partical/player_die/player_die_4.png',
             'Sprite/partical/player_die/player_die_5.png', 'Sprite/partical/player_die/player_die_6.png',
             'Sprite/partical/player_die/player_die_7.png', 'Sprite/partical/player_die/player_die_8.png',
             'Sprite/partical/player_die/player_die_9.png')

droneDamage = ('Sprite/partical/droneDamage/drone_damage_1.png', 'Sprite/partical/droneDamage/drone_damage_2.png',
               'Sprite/partical/droneDamage/drone_damage_3.png', 'Sprite/partical/droneDamage/drone_damage_4.png',
               'Sprite/partical/droneDamage/drone_damage_5.png', 'Sprite/partical/droneDamage/drone_damage_6.png',)

frame = 0
frame2 = 0

frame3 = 0


class DroneDamage(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(droneDamage[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (86, 86))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        global frame3
        if frame3 == 10:
            frame3 = 0
            self.kill()
        if frame3 == 2:
            self.image = pygame.image.load(droneDamage[1]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 86))
        if frame3 == 4:
            self.image = pygame.image.load(droneDamage[2]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 86))
        if frame3 == 6:
            self.image = pygame.image.load(droneDamage[3]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 86))
        if frame3 == 8:
            self.image = pygame.image.load(droneDamage[4]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 86))
        if frame3 == 10:
            self.image = pygame.image.load(droneDamage[5]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 86))
        frame3 += 1


class Partical(pygame.sprite.Sprite):
    def __init__(self, x, y, isPlayer, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (76, 76))
        self.rect = self.image.get_rect(center=(x, y))
        self.player = isPlayer
        self.add(group)

    def update(self):
        global frame, frame2

        if self.player:
            if frame2 == 19:
                frame2 = 0
                self.kill()
            if frame2 == 2:
                self.image = pygame.image.load(playerDie[0]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame2 == 4:
                self.image = pygame.image.load(playerDie[1]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame2 == 6:
                self.image = pygame.image.load(playerDie[2]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame2 == 8:
                self.image = pygame.image.load(playerDie[3]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (81, 81))
            if frame2 == 10:
                self.image = pygame.image.load(playerDie[4]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (80, 80))
            if frame2 == 12:
                self.image = pygame.image.load(playerDie[5]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (86, 86))
            if frame2 == 14:
                self.image = pygame.image.load(playerDie[6]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (86, 86))
            if frame2 == 16:
                self.image = pygame.image.load(playerDie[7]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (107, 107))
            if frame2 == 18:
                self.image = pygame.image.load(playerDie[8]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (126, 126))
            frame2 += 1

        if not self.player:
            if frame == 31:
                frame = 0
                self.kill()
            if frame == 1:
                self.image = pygame.image.load(enemyDie[0]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame == 6:
                self.image = pygame.image.load(enemyDie[1]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame == 9:
                self.image = pygame.image.load(enemyDie[2]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (76, 76))
            if frame == 12:
                self.image = pygame.image.load(enemyDie[3]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (81, 81))
            if frame == 15:
                self.image = pygame.image.load(enemyDie[4]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (80, 80))
            if frame == 18:
                self.image = pygame.image.load(enemyDie[5]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (86, 86))
            if frame == 21:
                self.image = pygame.image.load(enemyDie[6]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (86, 86))
            if frame == 24:
                self.image = pygame.image.load(enemyDie[7]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (97, 97))
            if frame == 27:
                self.image = pygame.image.load(enemyDie[8]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (106, 106))
            frame += 1


class ParticalSystem(pygame.sprite.Sprite):
    def __init__(self, x, y, pos, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (54, 54))
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pos
        self.add(group)

    def update(self):
        if self.pos == 0 and self.rect.y >= 5 and self.rect.x <= 950:
            self.rect.y -= 5
            self.rect.x += 10
        elif self.pos == 1 and self.rect.y >= 5:
            self.rect.y -= 15
        elif self.pos == 2 and self.rect.y <= 990:
            self.rect.y += 15
        elif self.pos == 3 and self.rect.y >= 5 and self.rect.x >= 5:
            self.rect.y -= 5
            self.rect.x -= 10
        elif self.pos == 4 and self.rect.y <= 990 and self.rect.x >= 950:
            self.rect.y += 5
            self.rect.x += 10
        elif self.pos == 4 and self.rect.y <= 990 and self.rect.x >= 5:
            self.rect.y += 5
            self.rect.x -= 10
        else:
            self.kill()


frameFill = 0
frameUnFill = 0
alpha = 0


class fillBack(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, sizeX, SizeY, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, SizeY))
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        global frameFill, alpha
        op.isStartNext = True
        if frameFill == 63:
            op.idFill = 0
            alpha = 0
            frameFill = 0
            self.kill()
        alpha += 9
        self.image.set_alpha(alpha)
        frameFill += 1


class unfillBack(pygame.sprite.Sprite):
    def __init__(self, fill, x, y, sizeX, SizeY, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, SizeY))
        self.image.set_alpha(op.Unalpha)
        self.rect = self.image.get_rect(center=(x, y))
        self.fill = fill
        self.add(group)

    def update(self):
        global frameUnFill
        op.isStartNext2 = True
        if frameUnFill == 60:
            op.idFill = 0
            op.Unalpha = 350
            frameUnFill = 0
            self.kill()
        op.Unalpha -= 6
        self.image.set_alpha(op.Unalpha)
        frameUnFill += 1
