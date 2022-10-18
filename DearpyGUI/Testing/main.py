import dearpygui.dearpygui as dpg

dpg.create_context()


def logincallback():



with dpg.window(tag="Primary Window", label="login"):
    dpg.add_menu_bar()
    dpg.add_dummy()
    dpg.add_text("Username")
    dpg.add_same_line()
    user = dpg.add_input_text()
    dpg.add_text("Password")
    dpg.add_same_line()
    passw = dpg.add_input_text()
    dpg.add_text("                 ")
    dpg.add_same_line()
    dpg.add_button(label="Login", callback=logincallback)


dpg.create_viewport(title='Login...', width=300, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
