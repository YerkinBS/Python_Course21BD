import pygame, time

global play_button, next_button, prev_button, music

play_button_img = pygame.image.load('images\\play.png')
next_button_img = pygame.transform.scale(pygame.image.load('images\\next.png'), play_button_img.get_size())
prev_button_img = pygame.transform.scale(pygame.image.load('images\\prev.png'), play_button_img.get_size())
pause_button_img = pygame.transform.scale(pygame.image.load('images\\pause.png'), play_button_img.get_size())

pygame.init()
SIZE = (400, 600)
screen = pygame.display.set_mode(SIZE)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('MP3 Player')

music = {
    1: 'Lil Peep - Star Shopping',
    2: 'Макс Корж - Малиновый закат',
    3: 'Migos (feat. Lil Uzi Vert) - Bad and Boujee',
    4: 'The Weeknd, Daft Punk - Starboy'
}

def player(num, in_pause, timestamp):
    if not in_pause:
        pygame.mixer_music.load('music\\' + music[num] + '.mp3')
        pygame.mixer_music.play()
    else:
        pygame.mixer_music.play(start=timestamp)
    

def player_status(num):
    artist_name = music[num][:music[num].find('-') - 1]
    song_name = music[num][music[num].find('-') + 2:]

    font = pygame.font.SysFont('Verdana', 20)
    song_name_result = font.render(song_name, True, (255, 255, 255))
    screen.blit(song_name_result, (10, 410))

    font = pygame.font.SysFont('Verdana', 16)
    artist_name_result = font.render(artist_name, True, (255, 255, 255))
    screen.blit(artist_name_result, (10, 433))

    try:
        album_cover = pygame.transform.scale(pygame.image.load('images\\' + music[num] + '.jpg'), (300, 300))
    except FileNotFoundError:
        album_cover = pygame.transform.scale(pygame.image.load('images\\' + music[num] + '.png'), (300, 300))
    screen.blit(album_cover, (50, 70)) 

    pygame.draw.rect(screen, (248, 164, 95), (47, 67, 303, 303), 3)


def main():
    running = True
    n_of_track = 1
    is_playing = False
    already_played = False
    paused = False
    time_stamp = int()
    last_time_stamp = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    already_played = False
                    if is_playing:
                        is_playing = False
                        paused = True
                        pygame.mixer.music.stop()
                    else:
                        player(n_of_track, paused, time_stamp + last_time_stamp)
                        is_playing = True
                        last_time_stamp = time_stamp
                        start_ticks = pygame.time.get_ticks()
                elif next_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track += 1
                    while n_of_track > len(music): n_of_track -= len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()
                elif prev_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track -= 1
                    while n_of_track < 1: n_of_track = len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()
        
        if is_playing: time_stamp = (pygame.time.get_ticks() - start_ticks) / 1000
        print(time_stamp if is_playing else 'not playing')
        screen.fill((238, 110, 71))
        pygame.draw.rect(screen, (255, 255, 255), (0, 470, 400, 400))
        if not is_playing and not already_played: play_button = screen.blit(play_button_img, (165, 500))
        else: pause_button = screen.blit(pause_button_img, (165, 500))
        next_button = screen.blit(next_button_img, (245, 500))
        prev_button = screen.blit(prev_button_img, (85, 500))
        pygame.draw.rect(screen, (248, 164, 95), (0, 0, 400, 471), 3)
        pygame.draw.rect(screen, (248, 164, 95), (0, 470, 400, 597), 3)

        if is_playing or paused: player_status(n_of_track)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()