import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window with Close Button")
        self.connect("destroy", Gtk.main_quit)

        self.button = Gtk.Button(label="Close")
        self.button.connect("clicked", self.on_close_button_clicked)

        self.add(self.button)

    def on_close_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()
