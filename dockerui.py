import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Unity', '7.0')
from gi.repository import Gtk, Unity, Dbusmenu
import docker
import sys

# Local imports
from ContainerTreeView import ContainerTreeView
import container


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Docker Containers", application=app)
        self.set_default_size(200, 100)
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        container_tree_view = ContainerTreeView()
        self.grid.add(container_tree_view.get_treeview())

class MyApplication(Gtk.Application):
    def __init__(self,):
        Gtk.Application.__init__(self)        
        container.launcher_menu()
    
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()
    
    def do_startup(self):
        Gtk.Application.do_startup(self)
    


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
