import arcade
def drawBullseye():
    arcade.draw_circle_outline(800, 400, 201, arcade.color.CARMINE_RED, 425)
    arcade.draw_circle_filled(800, 400, 200, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(800, 400, 150, arcade.color.CARMINE_RED)
    arcade.draw_circle_filled(800, 400, 100, arcade.color.GHOST_WHITE)
    arcade.draw_circle_filled(800, 400, 50, arcade.color.CARMINE_RED)

arcade.open_window(1200, 700, "Lots of shapes")
arcade.set_background_color(arcade.color.CHERRY_BLOSSOM_PINK)

arcade.start_render()

arcade.draw_line_strip([(30, 40), (200, 30), (300, 200), (200, 300), (30, 40)], arcade.color.LIGHT_CYAN, 3)
arcade.draw_lrtb_rectangle_filled(320, 420, 300, 50, arcade.color.LIGHT_CYAN)
arcade.draw_xywh_rectangle_outline(10, 10, 550, 300, arcade.color.BONE, 8)

drawBullseye()

arcade.draw_triangle_filled(300, 600, 600, 600, 450, 350, arcade.color.AIR_FORCE_BLUE)
arcade.draw_triangle_outline(300, 600, 490, 250, 700, 700, arcade.color.BATTLESHIP_GREY)

arcade.finish_render()

arcade.run()
