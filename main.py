import pygame
import time
import os
import random
pygame.font.init()

# screen play
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # WIN is window where the game will run
pygame.display.set_caption("Star Wars Rebells")


# loading images

# enemy ship
Red_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
Green_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
Blue_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
Yellow_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# loading Lasers

red_laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
green_laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blue_laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellow_laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# loading background
        # we have used the transform and scale function to fit the background image onto the window.
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# abstract class
class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0

    def draw(self, window):
        # pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))         this was just for testing
        WIN.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


# class player , player is going to inherit form ship, means it will have all the attriute of the ship class meaning
# it will be a ship and its a player ship

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = Yellow_space_ship
        self.laser_img = yellow_laser
        self.mask = pygame.mask.from_surface(self.ship_img)  # what this does is that it will us where pixels are in the
            # image so when we do collision it will only tell that collision happen is the ship is realy there , so basically
            # to make it look good

        self.max_health = health        # storing the players initial , max health


# class enemy

class Enemy(Ship):
    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health = 100)

# The Main Function

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    player_veleocity = 5
    main_font = pygame.font.SysFont("comicsans", 20)
    clock = pygame.time.Clock()

    player = Player(300, 600)

    # this function is inside the function because by doing this we won't have to pass a whole lot parameters cause this function
    # will inherit all the variable inside the main functio ( parent function)
    def redraw_window():
        """ Deales with all the drawings that are going the screen """

        # how this works:
            # so basically everything is being drawn at the top of each thing , like first we draw background so that
            # anything thta could be there is now covered by the background and now we can draw our player on the background

        # for pygames top left cornre is (0,0) and x and y both increases in their direction ,
        # meaning if we move towards left x will increase and if we move down then y will also increase.
        WIN.blit(bg,(0, 0))     # blit is used to draw on the window

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,0,0))        # 1 just is there , and then the tupple is for RGB color
        level_label = main_font.render(f"Level: {level}", 1, (255,255, 0))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() -10,10))

        player.draw(window=WIN)

        pygame.display.update()


    while run:
        clock.tick(FPS)     # so that the game run in same speed on the computers
        redraw_window()
        for events in pygame.event.get():       # so that you can check if user have pressed any button or someting
                                                # this for loop will run 60 times every second.

            # checking if user has quit the game
            if events.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_veleocity > 0:     # left
            player.x -= player_veleocity
        if keys[pygame.K_RIGHT] and player.x + player_veleocity + player.get_width() < WIDTH:    # right
            player.x += player_veleocity
        if keys[pygame.K_UP] and player.y - player_veleocity > 0:       # up
            player.y -= player_veleocity
        if keys[pygame.K_DOWN] and player.y + player_veleocity + player.get_height() < HEIGHT:     # down
            player.y += player_veleocity

        # alternate keys
        if keys[pygame.K_a] and player.x - player_veleocity < WIDTH:       # left
            player.x -= player_veleocity
        if keys[pygame.K_d] and player.x + player_veleocity < WIDTH:       # right
            player.x += player_veleocity
        if keys[pygame.K_w] and player.y - player_veleocity < WIDTH:       # up
            player.y -= player_veleocity
        if keys[pygame.K_s] and player.y + player_veleocity < WIDTH:       # down
            player.y += player_veleocity




if __name__ == '__main__':
    main()





