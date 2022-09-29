import arcade

arcade.open_window(1200, 700, "Lots of shapes")
arcade.set_background_color(arcade.color.CHERRY_BLOSSOM_PINK)

arcade.start_render()

arcade.draw_line_strip([(30, 40), (200, 30), (300, 200), (200, 300), (30, 40)], arcade.color.LIGHT_CYAN, 3)
arcade.draw_lrtb_rectangle_filled(320, 420, 300, 50, arcade.color.LIGHT_CYAN)
arcade.draw_xywh_rectangle_outline(10, 10, 550, 300, arcade.color.BONE, 8)

arcade.finish_render()

arcade.run()