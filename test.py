import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window with Close Button")
        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(300, 200)  # Set the window size

        self.button = Gtk.Button(label="Close")
        self.button.connect("clicked", self.on_close_button_clicked)

        self.label = Gtk.Label()
        self.label.set_markup('<span foreground="red">This is a message in red.</span>')
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.set_size_request(-1, 100)  # Adjust the height here (100 in this example)

        box = Gtk.VBox()
        box.add(self.label)
        box.add(self.button)

        align = Gtk.Alignment(xalign=0.5, yalign=0.5, xscale=1.0, yscale=1.0)
        align.add(box)

        self.add(align)

        # Center the window on the screen
        self.set_position(Gtk.WindowPosition.CENTER)

    def on_close_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()
