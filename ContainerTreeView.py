import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import container


class ContainerTreeView:
    def __init__(self):
        self.container_list_store = Gtk.ListStore(str, str, str)
        container_list = container.container_list()
        for item in container_list:
            self.container_list_store.append(list(item))
        
        self.treeview = Gtk.TreeView.new_with_model(self.container_list_store)

        for i, column_title in enumerate(['Container ID', 'Container Name', 'Container Status']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
    
    def get_treeview(self):
        return self.treeview