#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App(Gtk.Window):

    def main_box(self, spacing, border_width):
        self.mainBox = Gtk.VBox(spacing=spacing)
        self.mainBox.set_border_width(border_width)
        self.add(self.mainBox)

    def button(self, label, onclick:callable):
        b = Gtk.Button(label= label)
        b.connect("clicked", onclick)
        self.mainBox.pack_start(b, True, True, 0)

    def __init__(self):
        super().__init__(title="PyGTK hello")
        self.set_default_size(400,0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", self.quit)

        self.main_box(spacing= 10, border_width= 10)
        self.button(label= "Print title", onclick= self.onbutton1)
        self.button(label= "Button2", onclick= self.onbutton2)
        self.button(label= "Quit", onclick= self.quit)

    def onbutton1(self, eventer):
        self.diagnose(eventer)

    def onbutton2(self, eventer):
        self.diagnose(eventer)
         

    def quit(self, eventer):
        self.diagnose(eventer)
        Gtk.main_quit()

    def diagnose(self, eventer):
        if isinstance(eventer, Gtk.Button): 
            print(f"Button {eventer.get_label()}")
        elif eventer==self:
            print("Window event")
        else:
            print(eventer)

    def run(self):
        self.show_all()
        Gtk.main()

if __name__=="__main__":
    App().run()
    