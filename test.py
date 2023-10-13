import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window with Close Button")
        self.connect("destroy", Gtk.main_quit)

        self.button = Gtk.Button(label="Close")
        self.button.connect("clicked", self.on_close_button_clicked)

        self.label = Gtk.Label()
        self.label.set_markup('<span foreground="red">This is a message in red.</span>')
        self.label.set_justify(Gtk.Justification.CENTER)

        # Create a vertical box and add the label and button
        box = Gtk.VBox()
        box.add(self.label)
        box.add(self.button)

        self.add(box)

    def on_close_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()
