import pygame

import op


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (11, 11))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        upgrade_sfx = pygame.mixer.Sound('Audio/SFX/21.wav')
        if op.power == 150 and op.gunID == 0:
            upgrade_sfx.play()
            op.power += 5
            op.Damage = 5

        if op.power == 250 and op.gunID == 0:
            upgrade_sfx.play()
            op.power += 5
            op.Damage = 9
        if op.power == 350 and op.gunID == 0:
            upgrade_sfx.play()
            op.power += 5
            op.Damage = 13
        if op.power == 450 and op.gunID == 0:
            upgrade_sfx.play()
            op.power += 5
            op.Damage = 17

        if self.rect.y > 25:
            self.rect.y -= self.speed
        else:
            self.kill()


class ParticalDamage(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        op.timerPartical -= 1
        if op.timerPartical <= 1:
            op.timerPartical = 14
            self.kill()
