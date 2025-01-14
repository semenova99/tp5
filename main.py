import arcade
import random
import math
import colorsys

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 580

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.counter = 0
    def on_update(self, delta_time):
        self.counter += delta_time * 1000
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        arcade.draw_lbwh_rectangle_filled(0, 0, SCREEN_WIDTH, 100, arcade.color.DARK_BLUE)
        arcade.draw_lbwh_rectangle_filled(110, 120, 60, 200, arcade.color.LIGHT_GRAY)
        arcade.draw_arc_filled(140, 100, 180, 50, arcade.color.DARK_SLATE_GRAY, 0, 180)
        arcade.draw_arc_filled(270, 100, 20, 15, arcade.color.DARK_SLATE_GRAY, 0, 180)

        draw_moon()

# DOCSTRING
def draw_moon():
    x, y = SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100
    arcade.draw_circle_filled(x, y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x - 10, y- 10, 10, arcade.color.LIGHT_SLATE_GRAY)
    arcade.draw_circle_filled(x - 15, y-5, 6, arcade.color.LIGHT_SLATE_GRAY)

def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()


main()