import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window with Close Button")
        self.connect("destroy", Gtk.main_quit)

        self.button = Gtk.Button(label="Close")
        self.button.connect("clicked", self.on_close_button_clicked)

        self.label = Gtk.Label()
        self.label.set_markup('<span foreground="red" font_desc="24">This is a message in red with a larger font.</span>')
        self.label.set_justify(Gtk.Justification.CENTER)

        # Create a vertical box and add the label and button
        box = Gtk.VBox()
        box.add(self.label)
        box.add(self.button)

        # Create an Alignment container to center the box
        align = Gtk.Alignment(xalign=0.5, yalign=0.5, xscale=1.0, yscale=1.0)
        align.add(box)

        self.add(align)

    def on_close_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()

