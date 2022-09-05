import pygame

import op


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sizeX, sizeY, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        if self.rect.y < 980:
            self.rect.y += self.speed
        else:
            self.kill()


class BulletDrone(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sizeX, sizeY, left, right, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.left = left
        self.right = right
        self.add(group)

    def update(self):
        if not self.left and not self.right:
            if self.rect.y < 980:
                self.rect.y += self.speed + 4
            elif self.rect.x > 15:
                self.rect.x -= self.speed + 4
            else:
                self.kill()

        if self.left:
            if self.rect.y < 951:
                self.rect.y += self.speed + 3
            else:
                self.kill()

            if self.rect.x > 25:
                self.rect.x -= 4

            else:
                self.kill()
        if self.right:
            if self.rect.y < 951:
                self.rect.y += self.speed + 3
            else:
                self.kill()

            if self.rect.x < 885:
                self.rect.x += 4

            else:
                self.kill()


class BulletDarts(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sizeX, sizeY, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        if self.rect.y < 980:
            self.rect.y += self.speed + 1
        else:
            self.kill()


class BulletMouse(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sizeX, sizeY, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        if self.rect.y < 979:
            self.rect.y += self.speed + 0.5
        else:
            self.kill()


class BulletBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, sizeX, sizeY, left, right, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect(center=(x, y))
        self.left = left
        self.right = right
        self.speed = speed
        self.add(group)

    def update(self):
        if op.bossHealth >= 1400:
            if self.rect.y < 979:
                self.rect.y += self.speed + 0.5
            else:
                self.kill()
        elif op.bossHealth <= 1400:
            if not self.left and not self.right:
                if self.rect.y < 980:
                    self.rect.y += self.speed + 4
                elif self.rect.x > 15:
                    self.rect.x -= self.speed + 4
                else:
                    self.kill()

            if self.left:
                if self.rect.y < 951:
                    self.rect.y += self.speed + 3
                else:
                    self.kill()

                if self.rect.x > 25:
                    self.rect.x -= 3

                else:
                    self.kill()
            if self.right:
                if self.rect.y < 951:
                    self.rect.y += 15
                else:
                    self.kill()

                if self.rect.x < 885:
                    self.rect.x += 6

                else:
                    self.kill()

        elif op.bossHealth <= 1350:
            if not self.left and not self.right:
                if self.rect.y < 980:
                    self.rect.y += self.speed + 4
                elif self.rect.x > 15:
                    self.rect.x -= 4
                else:
                    self.kill()

            if self.left:
                if self.rect.y < 951:
                    self.rect.y += self.speed + 2
                else:
                    self.kill()

                if self.rect.x > 25:
                    self.rect.x -= 4

                else:
                    self.kill()
            if self.right:
                if self.rect.y < 951:
                    self.rect.y += self.speed + 2
                else:
                    self.kill()

                if self.rect.x < 885:
                    self.rect.x += 4
                else:
                    self.kill()


