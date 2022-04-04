import pygame, os

# variables
WIDTH, HEIGHT = 800, 640
FPS = 60
gravity = 0.75

# moving
moving_left = False
moving_right = False

# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('shooter.exe')
clock = pygame.time.Clock()
BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, (255, 255, 255), (0, 300), (WIDTH, 300))

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, person):
        pygame.sprite.Sprite.__init__(self)
        self.flip = False
        self.direction = 1
        self.speed = speed
        self.animation_list = []
        self.frameIndex = 0
        self.updateTime = pygame.time.get_ticks()
        self.action = 0
        self.jump = False
        self.vel_y = 0
        self.in_air = True

        animation_types = ['Idle', 'Run', 'Jump']
        for animation_type in animation_types:
            temp_list = []
            num_of_files = len(os.listdir(f'img/{person}/{animation_type}'))
            for i in range(num_of_files):
                img = pygame.image.load(f'img/{person}/{animation_type}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)


        self.image = self.animation_list[self.action][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        

    def move(self, moving_left, moving_right):
        dx, dy = 0, 0
       
        if moving_left:
            dx = -self.speed
            self.direction = -1
            self.flip = True
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False


        if self.jump and not self.in_air:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        self.vel_y += gravity
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy



    def updateAnimation(self):
        cooldown = 100
        self.image = self.animation_list[self.action][self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > cooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()

        if self.frameIndex >= len(self.animation_list[self.action]):
            self.frameIndex = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def updateAction(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()



Player = Soldier(200, 200, 3, 5, 'player')


running = True
while running:

    # draw
    draw_bg()
    Player.draw()
    Player.updateAnimation()
    Player.move(moving_left, moving_right)

    if Player.in_air:
        Player.updateAction(2) # 2 - jumping
    elif moving_left or moving_right:
        Player.updateAction(1)  # 1 - running
    else:
        Player.updateAction(0) # 0 idle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                Player.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    # display
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()


# 1. -Создание окна
# 2. -Создание класса солдата
# 3. -Создание метода draw
# 4. -Движение игрока в игре
# 5. -Создание класса move
# 6. -Направление спрайта
# 7. -Анимация