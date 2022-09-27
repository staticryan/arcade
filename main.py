import arcade

my_window = arcade.open_window(1000, 750, "Graph Paper")
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
arcade.start_render()

for xloc in range(50, 932, 80):
    arcade.draw_line(xloc, 50, xloc, 750, arcade.color.BRICK_RED, 5)

for yloc in range(50, 750, 80):
    arcade.draw_line(50, yloc, 932, yloc, arcade.color.BRICK_RED, 5)

arcade.finish_render()

arcade.run()
