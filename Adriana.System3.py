import pygame

import op
import partical

from player import Player
import bullet
import bulletEnemy
import enemy
import item
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 80)

tile = ''
tileName = randint(0, 11)

if tileName == 0:
    tile = 'I hate this world'
elif tileName == 1:
    tile = 'Hello?'
elif tileName == 2:
    tile = 'QWERTY you fucked crazy'
elif tileName == 3:
    tile = 'This game make Alien'
elif tileName == 4:
    tile = 'Player you ready!'
elif tileName == 5:
    tile = 'Also try: Touhou Project!'
elif tileName == 6:
    tile = 'Also try: Curseball!'
elif tileName == 7:
    tile = 'Also try: Meteorites!'
elif tileName == 8:
    tile = 'False Consensus Effect... Interesting'
elif tileName == 9:
    tile = 'written in python using pygame!'
elif tileName == 10:
    tile = 'Yea boy!'
elif tileName == 11:
    tile = 'This game not funny o_O'

timeSpawnBall = 67
isEnemy = True
ImageURL = 'Sprite/UI/level1.png'

iconSelect = randint(0, 1)
iconGame1 = pygame.image.load('Icon.png')
iconGame2 = pygame.image.load('Icon-1.png')

sc = pygame.display.set_mode((op.RES[0], op.RES[1]))
if iconSelect == 0:
    pygame.display.set_icon(iconGame1)
elif iconSelect == 1:
    pygame.display.set_icon(iconGame2)
pygame.display.set_caption("Adriana.System 3: " + tile)

imageBack = pygame.image.load(ImageURL).convert_alpha()
imageBack = pygame.transform.scale(imageBack, (650, 5195))
imageRect = imageBack.get_rect(center=(350, -1390))

imageUIBack = pygame.image.load('Sprite/UI/uiBack.png').convert_alpha()
imageUIBack = pygame.transform.scale(imageUIBack, (1055, 1010))
imageUIRect = imageUIBack.get_rect(center=(515, 487))

fontText = pygame.font.Font('Font/2.ttf', 47)
fontTextScore = pygame.font.Font('Font/1.ttf', 27)
fontScore = pygame.font.Font('Font/1.ttf', 22)
fontPlayer = pygame.font.Font('Font/1.ttf', 20)
fontFPS = pygame.font.Font('Font/2.ttf', 27)

power = fontText.render("Power: ", False, (0, 255, 255))
pos = power.get_rect(center=(790, 875))

scoreTXT = fontTextScore.render("Score:", False, (255, 190, 0))
posScoreTXT = scoreTXT.get_rect(center=(840, 210))

playerTXT = fontTextScore.render("Player: ", False, (0, 255, 0))
posPlayerTXT = playerTXT.get_rect(center=(805, 735))

p1 = Player(11.5, 1, 'Sprite/player/ioann_idle.png')

clock = pygame.time.Clock()


def effectBullet(x, y, group):
    return bullet.ParticalDamage(x, y, 'Sprite/partical/damage_fire.png', group)


def createBulletPlayer(group, x, y, speed):
    return bullet.Bullet(x, y, speed, 'Sprite/bullet/player_bullet.png', group)


def particalDie(group, bullets, x, y, filename):
    if not bullets:
        posP = randint(0, 4)
        return partical.ParticalSystem(x, y + 10, posP, filename, group)
    if bullet:
        randx = randint(55, 500)
        randy = randint(155, 425)
        posP = randint(0, 4)
        return partical.ParticalSystem(randx, randy + 10, posP, filename, group)


def createBulletShota(x, y, group):
    speed = randint(9, 14)
    return bulletEnemy.Bullet(x + 20, y + 50, speed + 1.5, 18, 18, 'Sprite/bullet/enemy_bullet_fire.png',
                              group)


def createBulletRosa(x, y, speed, group):
    fire = randint(1, 3)
    if fire == 1:
        return bulletEnemy.BulletDrone(x, y + 85, speed + 1.5, 15.5, 15.5, False, False,
                                       'Sprite/bullet/enemy_bullet_mini.png',
                                       group)
    elif fire == 2:
        return bulletEnemy.BulletDrone(x - 15, y + 45, speed + 1.5, 15.5, 15.5, True, False,
                                       'Sprite/bullet/enemy_bullet_mini.png', group)
    elif fire == 3:
        return bulletEnemy.BulletDrone(x + 25, y + 45, speed + 1.5, 15.5, 15.5, False, True,
                                       'Sprite/bullet/enemy_bullet_mini.png', group)


def createEnergy(x, y, filename, group):
    return item.Energy(x, y, filename, group)


def createCard(x, y, filename, group):
    return item.Card(x, y, filename, group)


def createBulletDrone(x, y, speed, group):
    fire = randint(1, 3)
    if fire == 1:
        return bulletEnemy.BulletDrone(x - 7, y, speed, 40, 40, False, False, 'Sprite/bullet/drone_bullet.png', group)
    elif fire == 2:
        return bulletEnemy.BulletDrone(x - 20, y + 10, speed, 40, 40, True, False, 'Sprite/bullet/drone_bullet.png',
                                       group)
    elif fire == 3:
        return bulletEnemy.BulletDrone(x + 20, y + 10, speed, 40, 40, False, True, 'Sprite/bullet/drone_bullet.png',
                                       group)


droneShotSFX = pygame.mixer.music


def createDrone(group):
    if op.countDrone == 1:
        op.countDrone = 0
        if op.level < 5:
            return enemy.drone(350, 1, 'Sprite/enemy/drone1.png', group)
        else:
            return enemy.drone(350, 1, 'Sprite/enemy/eyeDrone.png', group)
    for droneG in drone:
        if op.timeShotDrone >= 2:
            speed = randint(2, 10)
            op.timeShotDrone -= 2
            createBulletDrone(droneG.rect.x + 55, droneG.rect.y + 45, speed + 2, bulletE)
            ballShotSFX.play()
            if op.healthDrone <= 155:
                speed = randint(2, 10)
                op.timeShotDrone -= 2
                createBulletDrone(droneG.rect.x + 10, droneG.rect.y + 45, speed + 1, bulletE)
                createBulletDrone(droneG.rect.x + 10, droneG.rect.y + 45, speed + 1, bulletE)
                ballShotSFX.play()
        else:
            op.timeShotDrone += 1


ballShotSFX = pygame.mixer.Sound('Audio/SFX/18.wav')
dieEnemySFX = pygame.mixer.Sound('Audio/SFX/4.wav')
diePlayerSFX = pygame.mixer.Sound('Audio/SFX/20.wav')
collectItemSFX = pygame.mixer.Sound('Audio/SFX/22.wav')
playerShotSFX = pygame.mixer.Sound('Audio/SFX/17.wav')

playerShotSFX.set_volume(0.05)
ballShotSFX.set_volume(0.30)
dieEnemySFX.set_volume(0.55)
diePlayerSFX.set_volume(0.85)
collectItemSFX.set_volume(0.35)


def createBulletDaddy(group, x, y):
    return bulletEnemy.Bullet(x, y, 6, 34, 34, 'Sprite/bullet/ballDaddy.png', group)


def createDaddy(group):
    if op.level >= 4:
        if op.daddyTimeSpawn >= 350:
            y = randint(250, 655)
            op.daddyTimeSpawn -= 25
            return enemy.Daddy(10, y, 2, 0, 'Sprite/enemy/daddy.png', group)
        else:
            op.daddyTimeSpawn += 1
        for daddyB in daddyG:
            if op.timeDaddyShot >= 15:
                op.timeDaddyShot -= 15
                ballShotSFX.play()
                createBulletDaddy(bulletE, daddyB.rect.x + 40, daddyB.rect.y + 30)
            else:
                op.timeDaddyShot += 1


def createBallRosa(group):
    speed = randint(5, 10)
    if op.time_rosa >= 206:
        x = randint(55, 615)
        op.time_rosa -= timeSpawnBall
        return enemy.BallRosa(x, 28, speed - 1, 'Sprite/enemy/ball_rosa.png', group)
    else:
        op.time_rosa += 3

    for ball in ballRosa:
        ballShotSFX.play()
        createBulletRosa(ball.rect.x + 15, ball.rect.y, speed - 2, bulletE)


def createShota(group):
    if op.level >= 2:
        if op.time_shota >= 990:
            x = randint(35, 551)
            speed = randint(2, 8)
            op.time_shota -= 105
            return enemy.Shota(x, 8, speed, 'Sprite/enemy/shota.png', group)
        else:
            op.time_shota += 3
        for sh in shota:
            if op.timeShotShota >= 6:
                ballShotSFX.play()
                op.timeShotShota -= 6
                createBulletShota(sh.rect.x, sh.rect.y, bulletE)
            else:
                op.timeShotShota += 1


def createBulletDarts(x, y, group):
    select = randint(1, 3)
    if select == 1:
        return bulletEnemy.BulletDarts(x, y, 8, 39, 39, 'Sprite/bullet/enemy_magma.png', group)
    elif select == 2:
        return bulletEnemy.BulletDarts(x, y, 14, 18, 18, 'Sprite/bullet/enemy_bullet_fire.png', group)


def createDarts(group):
    if op.level >= 3:
        if op.time_darts >= 1095:
            x = randint(35, 551)
            speed = randint(3, 9)
            op.time_darts -= 305
            return enemy.Darts(x, 8, speed, 'Sprite/enemy/darts.png', group)
        else:
            op.time_darts += 3
        for sh in darts:
            if op.timeShotDarts >= 3:
                op.timeShotDarts -= 3
                particalDie(bulletE, False, sh.rect.x, sh.rect.y, 'Sprite/bullet/bulletStrike.png')
                particalDie(bulletE, False, sh.rect.x, sh.rect.y, 'Sprite/bullet/bulletStrike.png')
                particalDie(bulletE, False, sh.rect.x, sh.rect.y, 'Sprite/bullet/bulletStrike.png')
            else:
                op.timeShotDarts += 1


def particalDiePlayer(group):
    return partical.Partical(p1.rect.x, p1.rect.y, True, 'Sprite/partical/player_die/player_die_4.png', group)


def particalDieEnemy(group, x, y):
    return partical.Partical(x, y, False, 'Sprite/partical/enemy_die/enemy_die_5.png', group)


def createAdama(group, x, y):
    return item.Adama(x, y, 'Sprite/item/Adama.png', group)


def createParticalDrone(group, x, y):
    return partical.DroneDamage(x, y, group)


def collider():
    for bullP in bulletPlayer:
        for ballR in ballRosa:
            if bullP.rect.collidepoint(ballR.rect.center) or ballR.rect.collidepoint(bullP.rect.center):
                dieEnemySFX.play()
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie.png')
                effectBullet(ballR.rect.x, ballR.rect.y + 25, particalG)
                op.Score += 45
                createEnergy(ballR.rect.x, ballR.rect.y - 35, 'Sprite/item/energy.png', energy)
                particalDieEnemy(particalG, ballR.rect.x, ballR.rect.y)
                ballR.kill()
                bullP.kill()
    for bullP in bulletPlayer:
        for ballR in daddyG:
            if bullP.rect.collidepoint(ballR.rect.center):
                dieEnemySFX.play()
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie3.png')
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie3.png')
                particalDie(particalG, False, ballR.rect.x, ballR.rect.y, 'Sprite/partical/particalDie3.png')
                effectBullet(ballR.rect.x, ballR.rect.y + 25, particalG)
                op.Score += 255
                createEnergy(ballR.rect.x, ballR.rect.y - 35, 'Sprite/item/energy.png', energy)
                particalDieEnemy(particalG, ballR.rect.x, ballR.rect.y)
                ballR.kill()
                bullP.kill()

    for bullP in bulletPlayer:
        for shotaE in shota:
            if bullP.rect.collidepoint(shotaE.rect.center):
                dieEnemySFX.play()
                particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/particalDie.png')
                select = randint(0, 9)
                effectBullet(shotaE.rect.x + 20, shotaE.rect.y + 75, particalG)
                if op.timeEnergy >= 2:
                    op.timeEnergy -= 2
                    if select == 1 or select >= 3:
                        createEnergy(shotaE.rect.x, shotaE.rect.y + 5, 'Sprite/item/energy_shota.png', energy)
                    elif select == 2:
                        createCard(shotaE.rect.x, shotaE.rect.y + 5, 'Sprite/item/card.png', card)
                else:
                    op.timeEnergy += 1

                op.Score += 45
                op.health_shota -= op.Damage
                if op.health_shota <= 0:
                    particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/partilacDie2.png')
                    particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/partilacDie2.png')
                    particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/partilacDie2.png')
                    particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/partilacDie2.png')
                    particalDie(particalG, False, shotaE.rect.x, shotaE.rect.y, 'Sprite/partical/partilacDie2.png')
                    particalDieEnemy(particalG, shotaE.rect.x, shotaE.rect.y)
                bullP.kill()

    for bullP in bulletPlayer:
        for shotaE in darts:
            if bullP.rect.collidepoint(shotaE.rect.center):
                dieEnemySFX.play()
                effectBullet(shotaE.rect.x + 20, shotaE.rect.y + 75, particalG)
                createEnergy(shotaE.rect.x, shotaE.rect.y + 5, 'Sprite/item/energy_shota.png', energy)
                op.Score += 145
                op.health_darts -= op.Damage
                bullP.kill()

    for bullP in bulletPlayer:
        for shotaE in bossG:
            if bullP.rect.collidepoint(shotaE.rect.center):
                dieEnemySFX.play()
                particalDie(particalG, False, shotaE.rect.x + 80, shotaE.rect.y + 65, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, shotaE.rect.x + 80, shotaE.rect.y + 65, 'Sprite/partical/particalDie.png')
                particalDie(particalG, False, shotaE.rect.x + 80, shotaE.rect.y + 65, 'Sprite/partical/particalDie.png')
                effectBullet(shotaE.rect.x + 75, shotaE.rect.y + 65, particalG)
                op.Score += 1045
                op.bossHealth -= op.Damage
                bullP.kill()

    for bullP in bulletPlayer:
        for droneG in drone:
            if bullP.rect.collidepoint(droneG.rect.center):
                if op.healthDrone <= 3:
                    createAlphaBack(fillBack, 2, 645, 5190, 335, 'Sprite/UI/WhitefillBlack.png')
                    createAdama(adama, 145, 65)
                    createAdama(adama, 465, 45)
                dieEnemySFX.play()
                createParticalDrone(particalG, droneG.rect.x + 46, droneG.rect.y + 105)
                effectBullet(droneG.rect.x + 46, droneG.rect.y + 95, particalG)
                op.Score += 174
                op.healthDrone -= op.Damage

                bullP.kill()
    for bullE in bulletE:
        if bullE.rect.collidepoint(p1.rect.center) and op.isDamaged:
            diePlayerSFX.play()
            score = randint(25, 1450)
            op.Score -= score
            particalDiePlayer(particalG)
            op.Player -= 1
            op.timeDamage -= 15
            p1.rect.y = 910.5
            op.isDamaged = False
            bullE.kill()
    for ballR in ballRosa:
        if ballR.rect.collidepoint(p1.rect.center) and op.isDamaged:
            particalDiePlayer(particalG)
            op.Score -= 455
            diePlayerSFX.play()
            op.Player -= 1
            op.timeDamage -= 20
            p1.rect.y = 910.5
            op.isDamaged = False
    for shotaC in shota:
        if p1.rect.collidepoint(shotaC.rect.center) and op.isDamaged:
            particalDiePlayer(particalG)
            diePlayerSFX.play()
            op.Score -= 955
            op.Player -= 1
            op.timeDamage -= 20
            p1.rect.y = 910.5
            op.isDamaged = False
    for droneC in drone:
        if p1.rect.collidepoint(droneC.rect.center) and op.isDamaged:
            particalDiePlayer(particalG)
            op.Score -= 1825
            op.Player -= 1
            op.timeDamage -= 15
            p1.rect.y = float(910.5)
            op.isDamaged = False


def createText(x, y, group, filename):
    return item.textCollect(x, y, filename, group)


def energyCollider():
    for ene in energy:
        if p1.rect.collidepoint(ene.rect.center) and op.power <= 1500:
            createText(ene.rect.x, ene.rect.y, textCollect, 'Sprite/UI/collect_text_+5.png')
            collectItemSFX.play()
            op.power += 5
            op.Score += 35
            ene.kill()
    for cards in card:
        if p1.rect.collidepoint(cards.rect.center) and op.Player <= 10:
            createText(cards.rect.x, cards.rect.y, textCollect, 'Sprite/UI/collect_text_+0.5.png')
            op.Player += 0.5
            op.Score += 135
            cards.kill()

    for adamaG in adama:
        if p1.rect.collidepoint(adamaG.rect.center):
            if op.Player < 5.5:
                op.Player = 5.5
                op.Score += 1535
                adamaG.kill()
            else:
                op.Player = 2.5
                adamaG.kill()


bulletPlayer = pygame.sprite.Group()
bulletE = pygame.sprite.Group()

ballRosa = pygame.sprite.Group()
shota = pygame.sprite.Group()
drone = pygame.sprite.Group()
darts = pygame.sprite.Group()

daddyG = pygame.sprite.Group()

textCollect = pygame.sprite.Group()
fillBack = pygame.sprite.Group()

particalG = pygame.sprite.Group()

energy = pygame.sprite.Group()
card = pygame.sprite.Group()
adama = pygame.sprite.Group()


def createAlphaBack(group, Fill, SizeX, SizeY, x, filename):
    op.idFill = 1
    if Fill == 1:
        return partical.fillBack(x, -1390, 'Sprite/UI/fillBlack.png', SizeX, SizeY, group)

    if Fill == 2:
        return partical.unfillBack(350, 355, -1390, SizeX, SizeY, filename, group)


ostBack = pygame.mixer.music
ostBack.load('Audio/OST/Поляна для тебя.wav')
ostBack.set_volume(1)

current_scene = None


def switch_Scene(scene):
    global current_scene
    current_scene = scene


speedMove = 2.5


def diePlayer():
    global ImageURL, imageBack, imageRect
    op.isDIEplayer = False
    op.timeUnFill = 150
    op.Unalpha = 350
    op.timeFill = 0
    op.alpha = 0
    op.timeFill = 0
    FPS = 60
    createAlphaBack(fillBack, 2, 2005, 5190, 950, 'Sprite/UI/RedfillBlack.png')
    dieImage = pygame.image.load('Sprite/UI/dieScreen.png').convert_alpha()
    dieImage = pygame.transform.scale(dieImage, (428, 428))
    dieRect = dieImage.get_rect(center=(530, 465))
    ostBack.stop()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_Scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    for droneG in drone:
                        droneG.kill()
                    for daddyGG in daddyG:
                        daddyGG.kill()
                    for ballRosaG in ballRosa:
                        ballRosaG.kill()
                    for boss in bossG:
                        boss.kill()
                    ostBack.load('Audio/OST/Поляна для тебя.wav')
                    op.Score = 0
                    op.Player = 4.5
                    op.isDamaged = True
                    op.timeDamage = 0
                    op.isDIEplayer = False
                    op.time_rosa = 0
                    op.time_shota = 0
                    op.time_darts = 0
                    op.countDrone = 1
                    op.timeEnergy = 0
                    op.isUpdate = True
                    op.timeUnFill = 150
                    op.alpha = 0
                    op.Unalpha = 350
                    op.timeShotDrone = 0
                    op.timeShotShota = 0
                    op.timeShotDarts = 0
                    op.timerPartical = 20
                    op.timeDaddyShot = 0
                    op.health_shota = 90
                    op.health_darts = 125
                    op.isActiveLevel = True
                    op.time_shot = 0
                    op.isMoveLevel = True
                    op.healthDrone = 190
                    op.isMove = False
                    op.daddyTimeSpawn = 0
                    ImageURL = 'Sprite/UI/level1.png'
                    imageBack = pygame.image.load(ImageURL).convert_alpha()
                    imageBack = pygame.transform.scale(imageBack, (644, 5195))
                    imageRect = imageBack.get_rect(center=(355, -1392))
                    op.isMoveDrone = False
                    op.countEnemy = 0
                    op.countKillEnemy = 0
                    op.level = 1
                    op.km = 0
                    op.Damage = 3
                    op.isUp = False
                    op.isDown = False
                    op.isLeft = False
                    op.isRight = False
                    op.isShift = False
                    op.create = True
                    op.power = 0
                    running = False
                    switch_Scene(sceneMainMenu)
            sc.fill((0, 0, 0))
            sc.blit(dieImage, dieRect)
            fillBack.draw(sc)
            pygame.display.update()
            clock.tick(FPS)
            fillBack.update()


def createBulletBoss(x, y, id, speed, group):
    fire = randint(1, 3)
    if fire == 1:
        return bulletEnemy.BulletBoss(x + 7, y, speed, 45, 50, False, False, 'Sprite/bullet/bossBullet.png',
                                      group)
    elif fire == 2:
        return bulletEnemy.BulletBoss(x - 25, y + 10, speed, 45, 50, True, False, 'Sprite/bullet/bossBullet.png',
                                      group)
    elif fire == 3:
        return bulletEnemy.BulletBoss(x + 25, y + 10, speed, 45, 50, False, True, 'Sprite/bullet/bossBullet.png',
                                      group)

    if id == 1:
        return bulletEnemy.BulletBoss(x - 55, y + 13, speed, 40, 40, True, False, 'Sprite/bullet/drone_bullet.png',
                                      group)
    elif id == 2:
        return bulletEnemy.BulletBoss(x + 15, y + 5, speed, 40, 40, False, True, 'Sprite/bullet/drone_bullet.png',
                                      group)
    elif id == 3:
        return bulletEnemy.BulletBoss(x + 10, y + 10, speed, 40, 40, False, True, 'Sprite/bullet/drone_bullet.png',
                                      group)


shotTimeT = 5


def createBoss(group):
    global isActiveBoss, shotBossTime, shotTimeT
    if op.bossHealth <= 1400:
        shotTimeT = 3

    if isActiveBoss:
        isActiveBoss = False
        return enemy.Boss(350, 250, group)

    for bossGr in bossG:
        if shotBossTime >= 50:
            shotBossTime -= shotTimeT
            createBulletBoss(bossGr.rect.x + 45, bossGr.rect.y + 75, 0, 11, bulletE)
            if op.bossHealth <= 1300:
                idS = randint(1, 2)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
            if op.bossHealth <= 1200:
                shotTimeT = 2
            if op.bossHealth <= 1150:
                idS = randint(1, 2)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
            if op.bossHealth <= 955:
                idS = randint(1, 2)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 74, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 76, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 90, bossGr.rect.y + 65, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 95, bossGr.rect.y + 85, idS, 11, bulletE)
            if op.bossHealth <= 755:
                randX = randint(-10, 115)
                idS = randint(1, 3)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 14, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 15, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 74, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 76, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 85, bossGr.rect.y + 75, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 90, bossGr.rect.y + 65, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + 95, bossGr.rect.y + 85, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 14, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 25, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 16, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 24, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 17, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 9, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 35, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 68, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 12, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 61, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 9, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 1, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 54, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 17, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 13, idS, 11, bulletE)
                createBulletBoss(bossGr.rect.x + randX, bossGr.rect.y + 15, idS, 11, bulletE)

        else:
            shotBossTime += 1


shotBossTime = 0

isActiveBoss = False

bossG = pygame.sprite.Group()


def scene_Gameplaye():
    global imageRect, timeSpawnBall, imageBack, speedMove, isActiveBoss, ImageURL, back, backRect, BackText, BackTextRect, selectEsc, ExitTextRect, ExitText

    font = pygame.font.Font('Font/1.ttf', 15)
    font2 = pygame.font.Font('Font/1.ttf', 15)

    Color1 = (255, 255, 255)
    Color2 = (255, 255, 255)

    BackText = font.render('Back In Game', False, Color1)
    BackTextRect = BackText.get_rect(center=(350, 550))

    ExitText = font2.render('Exit', False, Color2)
    ExitTextRect = ExitText.get_rect(center=(350, 620))

    for fillG in fillBack:
        fillG.kill()
    if not isActiveBoss:
        createAlphaBack(fillBack, 2, 1010, 5190, 500, 'Sprite/UI/fillBlack.png')
        op.isStartNext2 = False
    elif isActiveBoss:
        createAlphaBack(fillBack, 2, 1010, 5190, 500, 'Sprite/UI/WhitefillBlack.png')
        op.isStartNext2 = False
    selectFlip = randint(0, 3)
    if selectFlip == 0 or 3:
        imageBack = pygame.transform.flip(imageBack, False, False)
    if selectFlip == 1 or 2:
        imageBack = pygame.transform.flip(imageBack, True, False)

    isESC = False
    selectEsc = 0
    FPS = 60
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ostBack.stop()
                switch_Scene(None)
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE and not isESC:
                    isESC = True
                if e.key == pygame.K_UP:
                    op.isUp = True
                elif e.key == pygame.K_DOWN:
                    op.isDown = True
                elif e.key == pygame.K_LEFT:
                    op.isLeft = True
                elif e.key == pygame.K_RIGHT:
                    op.isRight = True
                elif e.key == pygame.K_z:
                    op.isShift = True

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    op.isUp = False
                elif e.key == pygame.K_DOWN:
                    op.isDown = False
                elif e.key == pygame.K_LEFT:
                    op.isLeft = False
                elif e.key == pygame.K_RIGHT:
                    op.isRight = False
                elif e.key == pygame.K_z:
                    op.isShift = False

            if op.isDIEplayer:
                running = False
                switch_Scene(diePlayer)

            if isESC:
                op.isUpdate = False

                back = pygame.image.load('Sprite/UI/fillBlack.png').convert_alpha()
                back = pygame.transform.scale(back, (650, 5195))
                back.set_alpha(175)
                backRect = back.get_rect(center=(355, -1392))
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN and selectEsc == 0:
                        selectEsc = 1
                        Color1 = (255, 255, 255)
                        Color2 = (255, 255, 0)
                        BackText = font.render('Back In Game', False, Color1)
                        BackTextRect = BackText.get_rect(center=(350, 550))
                        ExitText = font2.render('Exit', False, Color2)
                        ExitTextRect = ExitText.get_rect(center=(350, 620))
                    elif e.key == pygame.K_UP and selectEsc == 1:
                        selectEsc = 0
                        Color1 = (255, 255, 0)
                        Color2 = (255, 255, 255)
                        BackText = font.render('Back In Game', False, Color1)
                        BackTextRect = BackText.get_rect(center=(350, 550))
                        ExitText = font2.render('Exit', False, Color2)
                        ExitTextRect = ExitText.get_rect(center=(350, 620))
                    if e.key == pygame.K_z and selectEsc == 0:
                        isESC = False
                    if e.key == pygame.K_z and selectEsc == 1:
                        for droneG in drone:
                            droneG.kill()
                        for daddyGG in daddyG:
                            daddyGG.kill()
                        for ballRosaG in ballRosa:
                            ballRosaG.kill()
                        for shotaE in shota:
                            shotaE.kill()
                        for boss in bossG:
                            boss.kill()
                        ostBack.load('Audio/OST/Поляна для тебя.wav')
                        op.Score = 0
                        op.Player = 4.5
                        op.isDamaged = True
                        op.timeDamage = 0
                        op.isDIEplayer = False
                        op.time_rosa = 0
                        op.time_shota = 0
                        op.time_darts = 0
                        op.countDrone = 1
                        op.timeEnergy = 0
                        op.isUpdate = True
                        op.timeUnFill = 150
                        op.alpha = 0
                        op.Unalpha = 350
                        op.timeShotDrone = 0
                        op.timeShotShota = 0
                        op.timeShotDarts = 0
                        op.timerPartical = 20
                        op.timeDaddyShot = 0
                        op.health_shota = 90
                        op.health_darts = 125
                        op.isActiveLevel = True
                        op.time_shot = 0
                        op.isMoveLevel = True
                        op.healthDrone = 190
                        op.isMove = False
                        op.daddyTimeSpawn = 0
                        ImageURL = 'Sprite/UI/level1.png'
                        imageBack = pygame.image.load(ImageURL).convert_alpha()
                        imageBack = pygame.transform.scale(imageBack, (644, 5195))
                        imageRect = imageBack.get_rect(center=(355, -1392))
                        op.isMoveDrone = False
                        op.countEnemy = 0
                        op.countKillEnemy = 0
                        op.level = 1
                        op.km = 0
                        op.Damage = 3
                        op.isUp = False
                        op.isDown = False
                        op.isLeft = False
                        op.isRight = False
                        op.isShift = False
                        op.create = True
                        op.power = 0
                        running = False
                        switch_Scene(sceneMainMenu)
            else:
                op.isUpdate = True

            if op.bossHealth <= 5:
                running = False
                switch_Scene(finalScene)

            elif e.type == pygame.USEREVENT and op.km <= 4050 and op.isUpdate:
                collider()
                energyCollider()
                if op.bossHealth <= 863:
                    ImageURL = 'Sprite/UI/level6.1.png'
                    imageBack = pygame.image.load(ImageURL).convert_alpha()
                    imageBack = pygame.transform.scale(imageBack, (644, 5195))
                    imageRect = imageBack.get_rect(center=(355, -795))
                if op.level >= 6:
                    createBallRosa(ballRosa)
                    createBoss(bossG)
                if op.isMoveLevel and op.isUpdate:
                    imageRect.y += speedMove
                    op.km += 5

                if op.timeDamage >= 175:
                    op.timeDamage -= 175
                    op.isDamaged = True
                else:
                    op.timeDamage += 1
                if op.km == 1055:
                    timeSpawnBall -= 24
                if op.km == 2585:
                    op.isActiveLevel = False
                    op.isMoveLevel = False
                if op.isActiveLevel and op.isMoveLevel:
                    createBallRosa(ballRosa)
                    createDaddy(daddyG)
                    createShota(shota)
                    createDarts(darts)
                if op.km >= 2425:
                    createDrone(drone)
                if op.km == 3675:
                    op.isActiveLevel = False
                if op.km == 3965:
                    particalDie(bulletE, True, 0, 0, 'Sprite/bullet/bulletStrike.png')
                    particalDie(bulletE, True, 0, 0, 'Sprite/bullet/bulletStrike.png')
                    particalDie(bulletE, True, 0, 0, 'Sprite/bullet/bulletStrike.png')
                    particalDie(bulletE, True, 0, 0, 'Sprite/bullet/bulletStrike.png')
                    particalDie(bulletE, True, 0, 0, 'Sprite/bullet/bulletStrike.png')

                if op.km >= 4040:
                    timeSpawnBall = 65
                    op.isMoveLevel = False
                    if not op.isStartNext:
                        op.idFill = 1
                        op.isStartNext2 = False
                        createAlphaBack(fillBack, 1, 655, 5190, 340, 'Sprite/UI/fillBlack.png')
                    elif op.isStartNext and op.idFill == 0:
                        if op.level == 1:
                            ostBack.stop()
                            ImageURL = 'Sprite/UI/level2.png'
                            speedMove = 3.8
                            imageBack = pygame.image.load(ImageURL).convert_alpha()
                            imageBack = pygame.transform.scale(imageBack, (644, 5195))
                            imageRect = imageBack.get_rect(center=(355, -1392))
                            if not op.isStartNext2:
                                createAlphaBack(fillBack, 2, 655, 5190, 335, 'Sprite/UI/fillBlack.png')
                            elif op.isStartNext2 and op.idFill == 0:
                                ostBack.load('Audio/OST/Я помню эти облока.wav')
                                ostBack.play(-1)
                                op.countDrone = 1
                                op.km = 0
                                op.isMoveLevel = True
                                op.isStartNext = False
                                op.isActiveLevel = True
                                op.idFill = 1
                                op.level = 2
                        elif op.level == 2:
                            ostBack.stop()
                            ostBack.load('Audio/OST/Депресия как страх мой.wav')
                            ImageURL = 'Sprite/UI/level3.png'
                            speedMove = 4.5
                            imageBack = pygame.image.load(ImageURL).convert_alpha()
                            imageBack = pygame.transform.scale(imageBack, (644, 5195))
                            imageRect = imageBack.get_rect(center=(355, -1392))
                            op.idFill = 1
                            op.isStartNext = False
                            running = False
                            switch_Scene(preLevel3)
                        elif op.level == 3:
                            ostBack.stop()
                            ImageURL = 'Sprite/UI/level4.png'
                            speedMove = 2.7
                            imageBack = pygame.image.load(ImageURL).convert_alpha()
                            imageBack = pygame.transform.scale(imageBack, (644, 5195))
                            imageRect = imageBack.get_rect(center=(355, -1392))
                            if not op.isStartNext2:
                                createAlphaBack(fillBack, 2, 645, 5190, 335, 'Sprite/UI/fillBlack.png')
                            elif op.isStartNext2 and op.idFill == 0:
                                ostBack.load('Audio/OST/I --.,- dont --_+= you.wav')
                                ostBack.play(-1)
                                op.countDrone = 1
                                op.km = 0
                                op.idFill = 1
                                op.isStartNext = False
                                op.isMoveLevel = True
                                op.isActiveLevel = True
                                op.level = 4
                        elif op.level == 4:
                            ostBack.stop()
                            ImageURL = 'Sprite/UI/level5.png'
                            imageBack = pygame.image.load(ImageURL).convert_alpha()
                            imageBack = pygame.transform.scale(imageBack, (644, 5195))
                            imageRect = imageBack.get_rect(center=(355, -1392))
                            if not op.isStartNext2:
                                createAlphaBack(fillBack, 2, 645, 5190, 335, 'Sprite/UI/fillBlack.png')
                            elif op.isStartNext2 and op.idFill == 0:
                                ostBack.load('Audio/OST/Зачем они смотрят на тебя.wav')
                                ostBack.play(-1)
                                op.countDrone = 1
                                op.timeUnFill = 240
                                op.Unalpha = 350
                                op.timeFill = 0
                                op.alpha = 0
                                op.timeFill = 0
                                op.km = 0
                                op.idFill = 1
                                op.isStartNext = False
                                op.isMoveLevel = True
                                op.isActiveLevel = True
                                op.level = 5
                        elif op.level == 5:
                            ostBack.stop()
                            ostBack.load('Audio/OST/Devil eye see you.wav')
                            ImageURL = 'Sprite/UI/level6.png'
                            imageBack = pygame.image.load(ImageURL).convert_alpha()
                            imageBack = pygame.transform.scale(imageBack, (644, 5195))
                            imageRect = imageBack.get_rect(center=(355, -795))
                            op.idFill = 1
                            op.isStartNext = False
                            running = False
                            switch_Scene(preLevel6)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c] and op.isUpdate:
            op.Score += 3
            if op.gunID == 0:
                speed = randint(10, 20)
                createBulletPlayer(bulletPlayer, p1.rect.x + 20, p1.rect.y - 10, speed)
            elif op.gunID == 1:
                speed = randint(15, 20)
                select = randint(0, 3)
                if not op.isShift:
                    if select == 0:
                        createBulletPlayer(bulletPlayer, p1.rect.x + 20, p1.rect.y - 10, speed)
                    elif select == 1:
                        createBulletPlayer(bulletPlayer, p1.rect.x - 10, p1.rect.y - 20, speed)
                    elif select == 2:
                        createBulletPlayer(bulletPlayer, p1.rect.x + 50, p1.rect.y - 20, speed)
                    elif select == 3:
                        createBulletPlayer(bulletPlayer, p1.rect.x - 10, p1.rect.y - 20, speed)
                        createBulletPlayer(bulletPlayer, p1.rect.x + 50, p1.rect.y - 20, speed)
                if op.isShift:
                    if select == 0 or select == 3:
                        createBulletPlayer(bulletPlayer, p1.rect.x + 20, p1.rect.y - 10, speed)
                    elif select == 1:
                        createBulletPlayer(bulletPlayer, p1.rect.x + 11, p1.rect.y - 20, speed - 2)
                    elif select == 2:
                        createBulletPlayer(bulletPlayer, p1.rect.x + 31, p1.rect.y - 20, speed - 2)
            playerShotSFX.play()

        sc.fill((0, 0, 0))
        collider()
        energyCollider()
        sc.blit(imageBack, imageRect)
        sc.blit(p1.image, p1.rect)
        bossG.draw(sc)
        bulletPlayer.draw(sc)
        ballRosa.draw(sc)
        shota.draw(sc)
        bulletE.draw(sc)
        textCollect.draw(sc)
        adama.draw(sc)
        particalG.draw(sc)
        darts.draw(sc)
        energy.draw(sc)
        daddyG.draw(sc)
        drone.draw(sc)
        card.draw(sc)
        fillBack.draw(sc)
        sc.blit(imageUIBack, imageUIRect)
        scoreNum = fontScore.render(str(op.Score), False, (205, 205, 205))
        posScore = power.get_rect(center=(855, 250))
        powerNum = fontPlayer.render(str(op.power), False, (255, 255, 255), (255, 0, 0))
        posPower = power.get_rect(center=(915, 875))
        playerNum = fontPlayer.render(str(op.Player), False, (255, 255, 255))
        posPlayer = power.get_rect(center=(945, 740))
        CFPS = fontFPS.render(str(int(clock.get_fps())), False, (255, 255, 255))
        posFPS = CFPS.get_rect(center=(45, 955))
        sc.blit(power, pos)
        sc.blit(CFPS, posFPS)
        sc.blit(powerNum, posPower)
        sc.blit(playerTXT, posPlayerTXT)
        sc.blit(playerNum, posPlayer)
        sc.blit(scoreTXT, posScoreTXT)
        sc.blit(scoreNum, posScore)
        if isESC:
            sc.blit(back, backRect)
            sc.blit(BackText, BackTextRect)
            sc.blit(ExitText, ExitTextRect)
        pygame.display.update()
        clock.tick(FPS)
        if op.isUpdate:
            bossG.update()
            p1.move()
            daddyG.update()
            bulletPlayer.update()
            p1.update()
            ballRosa.update()
            bulletE.update()
            adama.update()
            fillBack.update()
            particalG.update()
            energy.update()
            shota.update()
            darts.update()
            drone.update()
            textCollect.update()
            card.update()


menuOST = pygame.mixer.music
menuOST.load('Audio/OST/Я бы не хотел умереть здесь.wav')

isFinal = False


def selectGun():
    m4Icon = pygame.image.load('Sprite/UI/m4.png').convert_alpha()
    m4Icon = pygame.transform.scale(m4Icon, (335, 335))
    m4Rec = m4Icon.get_rect(center=(125, 455))

    m249Icon = pygame.image.load('Sprite/UI/m249.png').convert_alpha()
    m249Icon = pygame.transform.scale(m249Icon, (328, 328))
    m249Rec = m249Icon.get_rect(center=(455, 455))

    gunBack = pygame.image.load('Sprite/UI/gunSelectBack.png').convert_alpha()
    gunBack = pygame.transform.scale(gunBack, (1010, 990))
    gunBackRec = gunBack.get_rect(center=(505, 495))

    fontDev = pygame.font.Font('Font/3.ttf', 19)
    fontSel = pygame.font.Font('Font/2.ttf', 57)
    keyText = fontDev.render('Z = M4           X = M249', False, (255, 255, 255))
    keyPos = keyText.get_rect(center=(280, 557))

    SelectText = fontSel.render('Select Gun', False, (255, 255, 255))
    SelectPos = SelectText.get_rect(center=(495, 257))

    FPS = 60
    isStart = False
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    op.gunID = 0
                    isStart = True
                if e.key == pygame.K_x:
                    op.gunID = 1
                    isStart = True

            if isStart:
                if not op.isStartNext:
                    createAlphaBack(fillBack, 1, 1005, 5185, 500, 'Sprite/UI/fillBlack.png')
                if op.isStartNext and op.idFill == 0:
                    menuOST.stop()
                    ostBack.load('Audio/OST/Поляна для тебя.wav')
                    ostBack.set_volume(1)
                    ostBack.play(-1)
                    op.idFill = 1
                    op.isStartNext = False
                    running = False
                    switch_Scene(scene_Gameplaye)

            sc.fill((0, 0, 0))
            sc.blit(gunBack, gunBackRec)
            sc.blit(SelectText, SelectPos)
            sc.blit(keyText, keyPos)
            sc.blit(m4Icon, m4Rec)
            sc.blit(m249Icon, m249Rec)
            fillBack.draw(sc)
            fillBack.update()
            pygame.display.update()
            clock.tick(FPS)


menuOST.load('Audio/OST/Я бы не хотел умереть здесь.wav')
menuOST.set_volume(0.75)


def sceneMainMenu():
    global isFinal
    createAlphaBack(fillBack, 2, 2010, 5190, 950, 'Sprite/UI/WhitefillBlack.png')
    boom = pygame.mixer.Sound('Audio/SFX/4.wav')
    boom.play()

    running = True

    isKey = False

    select = pygame.mixer.Sound('Audio/SFX/23.wav')
    playS = pygame.mixer.Sound('Audio/SFX/4.wav')

    fontDev = pygame.font.Font('Font/2.ttf', 25)
    font = pygame.font.Font('Font/1.ttf', 13)
    fontMusic = pygame.font.Font('Font/3.ttf', 24)
    fontQuit = pygame.font.Font('Font/3.ttf', 22)
    fontMenu = pygame.font.Font('Font/3.ttf', 29)
    devText = fontDev.render('Powered By TitleChanQWERTY: *2022*', False, (255, 255, 255))
    devPos = devText.get_rect(center=(787, 957))

    Text = font.render('Press Z to Continue', True, (255, 255, 255))
    Pos = Text.get_rect(center=(190, 665))

    if isFinal:
        backImage = pygame.image.load('Sprite/UI/menu_image2.png').convert_alpha()
        backImage = pygame.transform.scale(backImage, (1010, 995))
        backImagePos = backImage.get_rect(center=(505, 495))
    else:
        backImage = pygame.image.load('Sprite/UI/menu_image.png').convert_alpha()
        backImage = pygame.transform.scale(backImage, (1010, 995))
        backImagePos = backImage.get_rect(center=(505, 495))

    LogoAlpha = -35

    LogoImage = pygame.image.load('Sprite/UI/LogoMain.png').convert_alpha()
    LogoImage = pygame.transform.scale(LogoImage, (395, 354))
    LogoImage.set_alpha(LogoAlpha)
    LogoPos = LogoImage.get_rect(center=(205, 100))

    posYSelect = 702
    posXSelect = 34

    FrameLogo = 0

    selectMenu = 0
    isStart = False
    FPS = 60
    COLOR1 = (255, 255, 255)
    COLOR2 = (255, 255, 0)
    COLOR3 = (255, 255, 255)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN or e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN and selectMenu < 2:
                    select.play()
                    selectMenu += 1
                if e.key == pygame.K_UP and selectMenu > 0:
                    select.play()
                    selectMenu -= 1
                if e.key == pygame.K_z and selectMenu == 0 and isKey:
                    playS.play()
                    isStart = True
                if e.key == pygame.K_z and selectMenu == 1 and isKey:
                    running = False
                    switch_Scene(musicRoom)
                if e.key == pygame.K_z and selectMenu == 2 and isKey:
                    running = False
                    switch_Scene(None)

        if FrameLogo < 290 and op.idFill == 0:
            LogoAlpha += 2
            LogoImage.set_alpha(LogoAlpha)
            FrameLogo += 1

        if selectMenu == 0:
            posYSelect = 702
            posXSelect = 45
            COLOR1 = (255, 255, 0)
            COLOR2 = (255, 255, 255)
            COLOR3 = (255, 255, 255)
        if selectMenu == 1:
            posXSelect = 28
            posYSelect = 762
            COLOR1 = (255, 255, 255)
            COLOR2 = (255, 255, 255)
            COLOR3 = (255, 255, 0)
        if selectMenu == 2:
            posXSelect = 13
            posYSelect = 822
            COLOR1 = (255, 255, 255)
            COLOR2 = (255, 255, 0)
            COLOR3 = (255, 255, 255)

        if op.idFill == 0:
            isKey = True
        else:
            isKey = False
        sc.fill((0, 0, 0))
        if isStart:
            if not op.isStartNext:
                createAlphaBack(fillBack, 1, 1005, 5190, 500, 'Sprite/UI/fillBlack.png')

            if op.isStartNext and op.idFill == 0:
                op.isStartNext = False
                op.idFill = 1
                running = False
                switch_Scene(selectGun)

        SelectImage = pygame.image.load('Sprite/UI/selectIcon.png').convert_alpha()
        SelectImage = pygame.transform.scale(SelectImage, (64, 64))
        SelectImagePos = SelectImage.get_rect(center=(posXSelect, posYSelect))
        playText = fontMenu.render('Start Game', False, COLOR1)
        playPos = playText.get_rect(center=(205, 705))
        quitText = fontQuit.render('Exit Game', False, COLOR2)
        quitPos = quitText.get_rect(center=(125, 825))
        MusicText = fontMusic.render('Music Room', False, COLOR3)
        musicPos = MusicText.get_rect(center=(165, 765))
        sc.blit(backImage, backImagePos)
        sc.blit(Text, Pos)
        sc.blit(SelectImage, SelectImagePos)
        sc.blit(LogoImage, LogoPos)
        sc.blit(playText, playPos)
        sc.blit(devText, devPos)
        sc.blit(MusicText, musicPos)
        sc.blit(quitText, quitPos)
        fillBack.draw(sc)
        pygame.display.flip()
        clock.tick(FPS)
        fillBack.update()


def titleScreen():
    frame = 0
    alpha = 0
    FPS = 60
    TitleChan = pygame.image.load('Sprite/UI/TitleChanQWERTY.png').convert_alpha()
    TitleChan = pygame.transform.scale(TitleChan, (635, 150))
    TitleChan.set_alpha(alpha)
    TitleRec = TitleChan.get_rect(center=(530, 450))

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_Scene(None)
            sc.fill((0, 0, 0))
            alpha += 5
            TitleChan.set_alpha(alpha)
            sc.blit(TitleChan, TitleRec)
            pygame.display.update()
            clock.tick(FPS)
            if frame <= 40:
                frame += 1
            elif frame >= 40:
                running = False
                menuOST.play(-1)
                switch_Scene(sceneMainMenu)


def preLevel3():
    FPS = 60
    op.timeUnFill = 150
    op.Unalpha = 350
    op.timeFill = 0
    op.alpha = 0
    op.timeFill = 0
    filename = 'Sprite/cutSceane/1.png'
    number = 0
    cutImage = pygame.image.load(filename).convert_alpha()
    cutImage = pygame.transform.scale(cutImage, (128, 128))
    cutRect = cutImage.get_rect(center=(450, 440))

    isActiveKey = True

    fontSel = pygame.font.Font('Font/2.ttf', 47)
    SelectText = fontSel.render('Press Z to continue', False, (255, 255, 255))
    SelectPos = SelectText.get_rect(center=(495, 815))

    for fillG in fillBack:
        fillG.kill()

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_Scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z and isActiveKey:
                    number += 1
            sc.fill((0, 0, 0))
            if number == 0:
                filename = 'Sprite/cutSceane/1.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 1:
                filename = 'Sprite/cutSceane/2.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 2:
                filename = 'Sprite/cutSceane/3.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 3:
                filename = 'Sprite/cutSceane/4.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 4:
                if not op.isStartNext:
                    isActiveKey = False
                    createAlphaBack(fillBack, 1, 1010, 5190, 500, 'Sprite/UI/fillBlack.png')
                if op.isStartNext and op.idFill == 0:
                    ostBack.play(-1)
                    op.km = 0
                    op.countDrone = 1
                    isActiveKey = False
                    op.Unalpha = 350
                    op.isMoveLevel = True
                    op.isStartNext = False
                    op.idFill = 1
                    op.isActiveLevel = True
                    op.level = 3
                    running = False
                    switch_Scene(scene_Gameplaye)
            sc.blit(cutImage, cutRect)
            sc.blit(SelectText, SelectPos)
            fillBack.draw(sc)
            pygame.display.update()
            clock.tick(FPS)
            fillBack.update()


def finalScene():
    global imageRect, imageBack, ImageURL
    global isFinal
    for fillG in fillBack:
        fillG.kill()
    boom = pygame.mixer.Sound('Audio/SFX/BossDie.wav')
    boom.play()
    createAlphaBack(fillBack, 2, 2010, 5190, 950, 'Sprite/UI/WhitefillBlack.png')

    pygame.mixer.music.load('Audio/OST/end.wav')
    pygame.mixer.music.play(-1)

    FPS = 60
    op.timeUnFill = 150
    op.Unalpha = 350
    op.timeFill = 0
    op.alpha = 0
    op.timeFill = 0

    bossDie = ('Sprite/UI/bossDie/bossDie_1.png', 'Sprite/UI/bossDie/bossDie_2.png', 'Sprite/UI/bossDie/bossDie_3.png',
               'Sprite/UI/bossDie/bossDie_4.png')

    bossDieImage = pygame.image.load(bossDie[0]).convert_alpha()
    bossDieImage = pygame.transform.scale(bossDieImage, (628, 628))
    bossDieRect = bossDieImage.get_rect(center=(255, 600))

    Font = pygame.font.Font('Font/2.ttf', 55)
    Font2 = pygame.font.Font('Font/3.ttf', 22)

    TheEndText = Font.render('The End', False, (255, 255, 255))
    TheEndRect = TheEndText.get_rect(center=(255, 220))

    CreatorText = Font2.render('Create by TitleChanQWERTY', False, (255, 255, 255))
    CreatorRect = CreatorText.get_rect(center=(705, 550))

    Frame = 0

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                op.Score = 0
                op.Player = 3.5
                op.isDamaged = True
                op.timeDamage = 0
                op.isDIEplayer = False
                op.time_rosa = 0
                op.time_shota = 0
                op.time_darts = 0
                op.countDrone = 1
                op.timeEnergy = 0
                op.isUpdate = True
                op.timeUnFill = 150
                op.alpha = 0
                op.Unalpha = 350
                op.timeShotDrone = 0
                op.timeShotShota = 0
                op.timeShotDarts = 0
                op.timerPartical = 20
                op.timeDaddyShot = 0
                op.health_shota = 90
                op.health_darts = 125
                op.isActiveLevel = True
                op.time_shot = 0
                op.isMoveLevel = True
                op.healthDrone = 190
                op.isMove = False
                op.daddyTimeSpawn = 0
                op.isMoveDrone = False
                op.countEnemy = 0
                isFinal = True
                op.countKillEnemy = 0
                op.level = 1
                op.km = 0
                op.Damage = 3
                op.isUp = False
                op.isDown = False
                op.isLeft = False
                op.isRight = False
                op.isShift = False
                op.create = True
                op.power = 0
                ImageURL = 'Sprite/UI/level1.png'
                imageBack = pygame.image.load(ImageURL).convert_alpha()
                imageBack = pygame.transform.scale(imageBack, (644, 5195))
                imageRect = imageBack.get_rect(center=(355, -1392))
                menuOST.load('Audio/OST/Я бы не хотел умереть здесь.wav')
                menuOST.set_volume(0.75)
                menuOST.play(-1)
                running = False
                switch_Scene(sceneMainMenu)
            sc.fill((0, 0, 0))
            sc.blit(bossDieImage, bossDieRect)
            sc.blit(TheEndText, TheEndRect)
            sc.blit(CreatorText, CreatorRect)
            if Frame == 45:
                Frame = 0
            if Frame == 4:
                bossDieImage = pygame.image.load(bossDie[0]).convert_alpha()
                bossDieImage = pygame.transform.scale(bossDieImage, (628, 628))
                bossDieRect = bossDieImage.get_rect(center=(255, 600))
            if Frame == 9:
                bossDieImage = pygame.image.load(bossDie[1]).convert_alpha()
                bossDieImage = pygame.transform.scale(bossDieImage, (628, 628))
                bossDieRect = bossDieImage.get_rect(center=(255, 600))
            if Frame == 15:
                bossDieImage = pygame.image.load(bossDie[2]).convert_alpha()
                bossDieImage = pygame.transform.scale(bossDieImage, (628, 628))
                bossDieRect = bossDieImage.get_rect(center=(255, 600))
            if Frame == 21:
                bossDieImage = pygame.image.load(bossDie[3]).convert_alpha()
                bossDieImage = pygame.transform.scale(bossDieImage, (628, 628))
                bossDieRect = bossDieImage.get_rect(center=(255, 600))
            Frame += 1
            fillBack.draw(sc)
            pygame.display.update()
            clock.tick(FPS)
            fillBack.update()


def preLevel6():
    global isActiveBoss, timeSpawnBall
    for fillG in fillBack:
        fillG.kill()
    FPS = 60
    isActiveKey = True
    op.timeUnFill = 150
    op.Unalpha = 350
    op.timeFill = 0
    op.alpha = 0
    op.timeFill = 0
    filename = 'Sprite/cutSceane/5.png'
    number = 0
    cutImage = pygame.image.load(filename).convert_alpha()
    cutImage = pygame.transform.scale(cutImage, (128, 128))
    cutRect = cutImage.get_rect(center=(450, 440))

    fontSel = pygame.font.Font('Font/2.ttf', 47)
    SelectText = fontSel.render('Press Z to continue', False, (255, 255, 255))
    SelectPos = SelectText.get_rect(center=(495, 815))

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_Scene(None)
            elif e.type == pygame.KEYDOWN and isActiveKey:
                if e.key == pygame.K_z:
                    number += 1
            sc.fill((0, 0, 0))
            if number == 0:
                filename = 'Sprite/cutSceane/5.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 1:
                filename = 'Sprite/cutSceane/6.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 2:
                filename = 'Sprite/cutSceane/7.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 3:
                filename = 'Sprite/cutSceane/8.png'
                cutImage = pygame.image.load(filename).convert_alpha()
                cutImage = pygame.transform.scale(cutImage, (528, 528))
                cutRect = cutImage.get_rect(center=(460, 450))
            if number == 4:
                isActiveKey = False
                op.Unalpha = 350
                createAlphaBack(fillBack, 2, 1010, 5190, 500, 'Sprite/UI/WhitefillBlack.png')
                ostBack.play(-1)
                op.countDrone = 1
                op.km = 0
                op.level = 6
                isActiveBoss = True
                timeSpawnBall = 195
                running = False
                switch_Scene(scene_Gameplaye)
            sc.blit(cutImage, cutRect)
            sc.blit(SelectText, SelectPos)
            fillBack.draw(sc)
            pygame.display.update()
            clock.tick(FPS)
            fillBack.update()


def musicRoom():
    global musicRect, iconMusic
    FPS = 30
    running = True

    imageBackRoom = pygame.image.load('Sprite/UI/musicRoomBack.png').convert_alpha()
    imageBackRoom = pygame.transform.scale(imageBackRoom, (1010, 995))
    roomRect = imageBackRoom.get_rect(center=(505, 495))

    if not isFinal:
        iconMusic = pygame.image.load('Sprite/UI/musicIcon.png').convert_alpha()
        iconMusic = pygame.transform.scale(iconMusic, (226, 226))
        musicRect = iconMusic.get_rect(center=(755, 355))
    if isFinal:
        iconMusic = pygame.image.load('Sprite/UI/musicIcon2.png').convert_alpha()
        iconMusic = pygame.transform.scale(iconMusic, (226, 226))
        musicRect = iconMusic.get_rect(center=(755, 355))

    Frame = 0

    font1 = pygame.font.Font('Font/3.ttf', 23)
    font2 = pygame.font.Font('Font/3.ttf', 23)
    font3 = pygame.font.Font('Font/3.ttf', 23)
    font4 = pygame.font.Font('Font/3.ttf', 23)
    font5 = pygame.font.Font('Font/3.ttf', 23)
    font6 = pygame.font.Font('Font/3.ttf', 23)
    font7 = pygame.font.Font('Font/3.ttf', 23)
    font8 = pygame.font.Font('Font/3.ttf', 23)
    font9 = pygame.font.Font('Font/1.ttf', 23)

    Color1 = (255, 255, 0)
    Color2 = (255, 255, 255)
    Color3 = (255, 255, 255)
    Color4 = (255, 255, 255)
    Color5 = (255, 255, 255)
    Color6 = (255, 255, 255)
    Color7 = (255, 255, 255)
    Color8 = (255, 255, 255)
    Color9 = (255, 255, 255)

    select = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                switch_Scene(sceneMainMenu)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN and select < 8:
                    select += 1
                elif e.key == pygame.K_UP and select > 0:
                    select -= 1

                if e.key == pygame.K_z and select == 0:
                    pygame.mixer.music.load('Audio/OST/Я бы не хотел умереть здесь.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 1:
                    pygame.mixer.music.load('Audio/OST/Поляна для тебя.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 2:
                    pygame.mixer.music.load('Audio/OST/Я помню эти облока.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 3:
                    pygame.mixer.music.load('Audio/OST/Депресия как страх мой.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 4:
                    pygame.mixer.music.load('Audio/OST/I --.,- dont --_+= you.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 5:
                    pygame.mixer.music.load('Audio/OST/Зачем они смотрят на тебя.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 6:
                    pygame.mixer.music.load('Audio/OST/Devil eye see you.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 7:
                    pygame.mixer.music.load('Audio/OST/end.wav')
                    pygame.mixer.music.play(-1)
                if e.key == pygame.K_z and select == 8:
                    running = False
                    switch_Scene(sceneMainMenu)
        if select == 0:
            Color1 = (255, 255, 0)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 1:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 0)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 2:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 0)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 3:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 0)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 4:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 0)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 5:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 0)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)
        if select == 6:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 0)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 255)

        if select == 7:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 0)
            Color9 = (255, 255, 255)

        if select == 8:
            Color1 = (255, 255, 255)
            Color2 = (255, 255, 255)
            Color3 = (255, 255, 255)
            Color4 = (255, 255, 255)
            Color5 = (255, 255, 255)
            Color6 = (255, 255, 255)
            Color7 = (255, 255, 255)
            Color8 = (255, 255, 255)
            Color9 = (255, 255, 0)

        if Frame < 20:
            musicRect.y += 1
        if Frame > 20:
            musicRect.y -= 1.5
        if Frame == 30:
            Frame = 0
            musicRect = iconMusic.get_rect(center=(755, 355))
        Frame += 1

        TextF = font1.render('1: Menu ost', False, Color1)
        textFRect = TextF.get_rect(center=(225, 140))

        TextS = font2.render('2: Level 1 ost', False, Color2)
        textSRect = TextS.get_rect(center=(225, 225))

        TextT = font3.render('3: Level 2 ost', False, Color3)
        textTRect = TextT.get_rect(center=(225, 275))

        TextFF = font4.render('4: Level 3 ost', False, Color4)
        textFFRect = TextFF.get_rect(center=(225, 325))

        TextFi = font5.render('5: Level 4 ost', False, Color5)
        textFiRect = TextFi.get_rect(center=(225, 375))

        TextSi = font6.render('6: Level 5 ost', False, Color6)
        textSiRect = TextSi.get_rect(center=(225, 425))

        TextSe = font7.render('7: Level 6 ost', False, Color7)
        textSeRect = TextSe.get_rect(center=(225, 475))

        TextE = font8.render('8: Final ost', False, Color8)
        textERect = TextE.get_rect(center=(225, 560))

        TextBack = font9.render('Back Menu', False, Color9)
        textBRect = TextBack.get_rect(center=(160, 825))

        sc.fill((0, 0, 0))
        sc.blit(imageBackRoom, roomRect)
        sc.blit(iconMusic, musicRect)
        sc.blit(TextF, textFRect)
        sc.blit(TextS, textSRect)
        sc.blit(TextT, textTRect)
        sc.blit(TextFF, textFFRect)
        sc.blit(TextFi, textFiRect)
        sc.blit(TextSi, textSiRect)
        sc.blit(TextSe, textSeRect)
        sc.blit(TextE, textERect)
        sc.blit(TextBack, textBRect)
        pygame.display.update()
        clock.tick(FPS)


switch_Scene(titleScreen)
while current_scene is not None:
    current_scene()

pygame.quit()
