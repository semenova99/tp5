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

        # boat
        arcade.draw_arc_filled(500, 115, 140, 50, arcade.color.BARN_RED, 0, 180, 180)
        arcade.draw_line(500, 115, 500, 190, arcade.color.BARN_RED, 4)
        arcade.draw_triangle_filled(500, 190, 550, 130, 450, 130, arcade.color.ANTI_FLASH_WHITE)
        arcade.draw_text("UKRAINE", 500-50, 137.5, arcade.color.COOL_BLACK, 10, 100, "center", "Californian FB", True)

        flag_x=500-12.5
        flag_y=152.5
        flag_height=17.5
        #60x40
        arcade.draw_lbwh_rectangle_outline(flag_x, flag_y, 25, flag_height, arcade.color.BLACK, 2)
        arcade.draw_lbwh_rectangle_filled(flag_x, flag_y, 25, flag_height/2, arcade.color.YELLOW)

        # water
        arcade.draw_lbwh_rectangle_filled(0, 0, SCREEN_WIDTH, 100, arcade.color.DARK_BLUE)


        # lighthouse
        arcade.draw_lbwh_rectangle_filled(110, 120, 60, 200, arcade.color.LIGHT_GRAY)
        squircle(90, 300, 60 + 40, 20, arcade.color.LIGHT_GRAY)
        arcade.draw_ellipse_filled(140, 335, 25, 20, arcade.color.GOLDEN_YELLOW)
        draw_lighthouse_bars()
        squircle(100, 350, 60 + 20, 5, arcade.color.LIGHT_GRAY)
        arcade.draw_arc_filled(140, 350, 60+20, 70, arcade.color.LIGHT_GRAY, 0, 180)

        # rocks
        arcade.draw_arc_filled(140, 100, 180, 50, arcade.color.DARK_SLATE_GRAY, 0, 180)
        arcade.draw_arc_filled(270, 100, 20, 15, arcade.color.DARK_SLATE_GRAY, 0, 180)


        # moon
        draw_moon()

def draw_lighthouse_bars():
    start_x = 110
    end_x = 170
    count = 5
    for i in range(count + 1):
        x = start_x + i * ((end_x - start_x) / count)
        arcade.draw_line(x, 320, x, 350, arcade.color.LIGHT_GRAY, 3)


# DOCSTRING
def draw_moon():
    x, y = SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100
    arcade.draw_circle_filled(x, y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x - 10, y- 10, 10, arcade.color.LIGHT_SLATE_GRAY)
    arcade.draw_circle_filled(x - 15, y-5, 6, arcade.color.LIGHT_SLATE_GRAY)

def squircle(x, y, width, height, color):
    radius = height / 2
    arcade.draw_lbwh_rectangle_filled(x + radius, y, width - radius * 2, height, color)
    arcade.draw_circle_filled(x + radius, y + radius, radius, color)
    arcade.draw_circle_filled(x + width - radius, y + radius, radius, color)

def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()


main()