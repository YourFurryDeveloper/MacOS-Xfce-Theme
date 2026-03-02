import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApp:
    def __init__(self):
        # Load UI file
        self.builder = Gtk.Builder()
        self.builder.add_from_file("layout.ui")

        # Get objects by ID
        self.window = self.builder.get_object("main_window")
        self.label = self.builder.get_object("main_label")
        self.button = self.builder.get_object("main_button")

        # Connect signals
        self.button.connect("clicked", self.on_button_clicked)
        self.window.connect("destroy", Gtk.main_quit)

        self.window.show_all()

    def on_button_clicked(self, button):
        self.label.set_text("Button Clicked!")

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()