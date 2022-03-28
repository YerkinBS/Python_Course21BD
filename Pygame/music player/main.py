import pygame

play_button = pygame.image.load('play.png')
next_button = pygame.transform.scale(pygame.image.load('next.png'), play_button.get_size())
prev_button = pygame.transform.scale(pygame.image.load('prev.png'), play_button.get_size())

pygame.init()
SIZE = (400, 600)
screen = pygame.display.set_mode(SIZE)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('MP3 Player')

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((238, 110, 71))
        pygame.draw.rect(screen, (255, 255, 255), (0, 470, 400, 400))
        screen.blit(play_button, (165, 500))
        screen.blit(next_button, (245, 500))
        screen.blit(prev_button, (85, 500))

        pygame.display.flip()
    pygame.quit()


main()