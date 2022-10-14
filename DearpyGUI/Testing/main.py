import dearpygui.dearpygui as dpg

dpg.create_context()


with dpg.window(tag="Primary Window", label="Tutorial"):
    dpg.add_text(label="hello")

dpg.create_viewport(title='Login...', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()