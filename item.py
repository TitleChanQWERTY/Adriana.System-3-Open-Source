import pygame


class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        if self.rect.y < 985:
            self.rect.y += 9
        else:
            self.kill()


class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 39))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        if self.rect.y < 980:
            self.rect.y += 9
        else:
            self.kill()


class Adama(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (58, 59))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        if self.rect.y < 985:
            self.rect.y += 3
        else:
            self.kill()


class textCollect(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        self.rect.y += 7
        if self.rect.y >= 985:
            self.kill()
