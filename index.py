#!/usr/bin/python

from gi.repository import Gtk

class pytry(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pytry")
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
        Gtk.Window.set_default_size(self, 500, 300)
# add a header Bar
        headerbar = Gtk.HeaderBar(title="Pytry || The door to the soul")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

#add a notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
# the add poem sector
        self.add_poem_grid = Gtk.Grid()

        self.add_poem_list_box = Gtk.ListBox()
        self.add_poem_list_box.set_selection_mode(Gtk.SelectionMode.NONE)

            # add title
        row = Gtk.ListBoxRow()
        self.add_poem_title_grid = Gtk.Grid()
        self.poem_title_label = Gtk.Label("Poem's\nTitle : ")
        self.poem_title_entry = Gtk.Entry()
        self.poem_title_entry.set_max_length(25)
        self.add_poem_title_grid.attach(self.poem_title_label, 1,1,1,1)
        self.add_poem_title_grid.attach_next_to(self.poem_title_entry, self.poem_title_label, Gtk.PositionType.RIGHT, 1,1)
        row.add(self.add_poem_title_grid)
        self.add_poem_list_box.add(row)

            #add name
        row = Gtk.ListBoxRow()
        self.add_poem_name_grid = Gtk.Grid()
        self.poem_name_label = Gtk.Label("Poet's\nName : ")
        self.poem_name_entry = Gtk.Entry()
        self.poem_name_entry.set_max_length(25)
        self.add_poem_name_grid.attach(self.poem_name_label, 1, 1,1,1)
        self.add_poem_name_grid.attach_next_to(self.poem_name_entry, self.poem_name_label, Gtk.PositionType.RIGHT,1, 1)
        row.add(self.add_poem_name_grid)
        self.add_poem_list_box.add(row)


            #add content
        row = Gtk.ListBoxRow()
        self.add_poem_content_grid = Gtk.Grid()
        self.poem_content_label = Gtk.Label("Poem ", xalign=0)
        self.poem_content_entry = Gtk.TextView()
        self.poem_content_entry.set_editable(True)
        self.poem_content_entry.set_cursor_visible(True)
        self.poem_content_entry.set_justification(Gtk.Justification.LEFT)
        self.poem_content_entry.set_wrap_mode(False)
        self.poem_content_buffer = self.poem_content_entry.get_buffer()
        self.poem_content_buffer.set_text("THis is some text inside the text view")
        self.add_poem_content_grid.attach(self.poem_content_label, 1,1,1,1)
        self.add_poem_content_grid.attach_next_to(self.poem_content_entry, self.poem_content_label, Gtk.PositionType.RIGHT, 1,1)
        row.add(self.add_poem_content_grid)
        self.add_poem_list_box.add(row)

        self.notebook.append_page(self.add_poem_list_box, Gtk.Label("Add a Poem"))




pyt = pytry()
pyt.show_all()
pyt.connect("delete-event", Gtk.main_quit)
Gtk.main()
