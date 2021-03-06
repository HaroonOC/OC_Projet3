# Main file
# Help MacGyver to escape game, created by Haroon for P3 - OCR

# Map structure:
# '#': bloc
# '.': guardian

import pygame
from pygame.locals import *  # import all pygame constants

import loader
import game_class
import display
from constants import *


def main():
    pygame.init()
    # Setup the window (15*30, 15*30) : Resolution = 450,450
    screen = pygame.display.set_mode((map_length * tile_size, map_height * tile_size))

    config = loader.load_json("config.json")
    images = loader.Images(config)

    lvl = game_class.Level(loader.map_from_file("map"), config["items"])
    mac_gyver = game_class.Character(lvl, config["items"])

    display.draw(lvl, mac_gyver, images, screen)

    continue_game = True
    end_game = False

    # Main game loop
    print("Have fun !")
    while continue_game:
        for event in pygame.event.get():   # iteration in all events
            if event.type == QUIT:
                continue_game = False
            if event.type == KEYDOWN:
                if not end_game:
                    if event.key == K_LEFT:
                        mac_gyver.move_to(left)
                    elif event.key == K_RIGHT:
                        mac_gyver.move_to(right)
                    elif event.key == K_UP:
                        mac_gyver.move_to(up)
                    elif event.key == K_DOWN:
                        mac_gyver.move_to(down)

                    if mac_gyver.status() == WIN:
                        print("You win")
                    elif mac_gyver.status() == LOST:
                        print("You loose")

                    if mac_gyver.status() != IN_MAZE:
                        print("\nDo you want to replay (y/n) ?")
                        end_game = True
                else:
                    if event.key == K_y:
                        print("Again!")
                        mac_gyver.reset()
                        lvl.reset()
                        end_game = False
                    elif event.key == K_n:
                        continue_game = False

                display.draw(lvl, mac_gyver, images, screen)


if __name__ == "__main__":
    main()

