import pygame, datetime
from math import sin, cos, pi

pygame.init()

mickey_mouse = pygame.transform.scale(pygame.image.load('mickey.png'), (int(574 * 1.3), int(485 * 1.3)))
right_hand = pygame.transform.scale(pygame.image.load('right hand.png'), (594 // 2, 322 // 2))
left_hand = pygame.transform.scale(pygame.image.load('left hand.png'), (770 // 2, 230 // 2))

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
POWDERBLUE = (176, 224, 230, 255)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)

SIZE = (800, 800)
center = (SIZE[0] / 2, SIZE[1] / 2)
clock_radius = 400

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Clock")
FPS = 60
clock = pygame.time.Clock()

digits = {
    1 : 'I',
    2 : 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII'
}

def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size)
    text = font.render(number, True, NAVY_BLUE)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + SIZE[0] / 2, -(y - SIZE[1] / 2)


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        pygame.draw.circle(screen, GREY, center, clock_radius - 10, 10)
        pygame.draw.circle(screen, POWDERBLUE, center, clock_radius - 20)
        pygame.draw.circle(screen, BLACK, center, 10)

        for number in range(1, 13):
            numbers(digits[number], 60, polar_to_cartesian(clock_radius - 80, number * 30))

        for number in range(0, 360, 6):
            if number % 5 != 0:
                pygame.draw.line(screen, GREY, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 30, number), 2)
            else:
                pygame.draw.line(screen, GREY, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 30, number), 6)

        screen.blit(mickey_mouse, (20, 30))

        current_date_time = datetime.datetime.now()
        minute = current_date_time.minute
        second = current_date_time.second

        ## Minutes
        theta = (minute + second / 60) * (360 / 60)
        blitRotate(screen, right_hand, center, (right_hand.get_width() / 2 + 110, left_hand.get_height() / 2 + 75), theta + 75)

        ## Seconds
        theta = second * (360 / 60)
        blitRotate(screen, left_hand, center, (left_hand.get_width() / 2 - 145, left_hand.get_height() / 2), theta - 87)

        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main()