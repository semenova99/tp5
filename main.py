import arcade

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

        flag_x = 500-12.5
        flag_y = 152.5
        flag_height = 17.5

        # 60x40
        arcade.draw_lbwh_rectangle_outline(flag_x, flag_y, 25, flag_height, arcade.color.BLACK, 2)
        arcade.draw_lbwh_rectangle_filled(flag_x, flag_y, 25, flag_height/2, arcade.color.YELLOW)
        arcade.draw_lbwh_rectangle_filled(flag_x, flag_y + flag_height / 2, 25, flag_height / 2, arcade.color.BLUE)

        # water
        arcade.draw_lbwh_rectangle_filled(0, 0, SCREEN_WIDTH, 100, arcade.color.DARK_BLUE)

        # lighthouse
        arcade.draw_lbwh_rectangle_filled(110, 120, 60, 200, arcade.color.GRAY)
        squircle(90, 300, 60 + 40, 20, arcade.color.GRAY)
        arcade.draw_ellipse_filled(140, 335, 25, 20, arcade.color.GOLDEN_YELLOW)
        draw_lighthouse_bars()
        squircle(100, 350, 60 + 20, 5, arcade.color.GRAY)
        arcade.draw_arc_filled(140, 350, 60+20, 70, arcade.color.GRAY, 0, 180)

        # rocks
        arcade.draw_arc_filled(140, 100, 180, 50, arcade.color.DARK_SLATE_GRAY, 0, 180)
        arcade.draw_arc_filled(270, 100, 20, 15, arcade.color.DARK_SLATE_GRAY, 0, 180)

        # birds flying in triangle, 11 birds in total
        draw_bird(400, 300, arcade.color.BLACK)
        draw_bird(420, 320, arcade.color.BLACK)
        draw_bird(440, 340, arcade.color.BLACK)
        draw_bird(460, 360, arcade.color.BLACK)
        draw_bird(480, 380, arcade.color.BLACK)
        draw_bird(500, 400, arcade.color.BLACK) # middle of the triangle
        draw_bird(480, 420, arcade.color.BLACK)
        draw_bird(460, 440, arcade.color.BLACK)
        draw_bird(440, 460, arcade.color.BLACK)
        draw_bird(420, 480, arcade.color.BLACK)
        draw_bird(400, 500, arcade.color.BLACK)

        # moon
        draw_moon()


def draw_lighthouse_bars():
    start_x = 110
    end_x = 170
    count = 5
    for i in range(count + 1):
        x = start_x + i * ((end_x - start_x) / count)
        arcade.draw_line(x, 320, x, 350, arcade.color.GRAY, 3)


# DOCSTRING
def draw_moon():
    x, y = SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100
    arcade.draw_circle_filled(x, y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x - 10, y - 10, 10, arcade.color.LIGHT_SLATE_GRAY)
    arcade.draw_circle_filled(x - 15, y-5, 6, arcade.color.LIGHT_SLATE_GRAY)
    arcade.draw_ellipse_filled(x + 15, y + 15, 20, 10, arcade.color.LIGHT_SLATE_GRAY, 45)


def draw_bird(x, y, color):
    # a triangle type of shape, concave on the base
    arcade.draw_polygon_filled([(x, y), (x+2.5, y + 10), (x, y + 20), (x+10, y+10)], color)


def squircle(x, y, width, height, color):
    radius = height / 2
    arcade.draw_lbwh_rectangle_filled(x + radius, y, width - radius * 2, height, color)
    arcade.draw_circle_filled(x + radius, y + radius, radius, color)
    arcade.draw_circle_filled(x + width - radius, y + radius, radius, color)


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()


main()
