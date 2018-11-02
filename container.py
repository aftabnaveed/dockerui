import gi
gi.require_version('Unity', '7.0')
from gi.repository import Unity, Dbusmenu
import docker


import docker

client = docker.from_env()
containers = client.containers.list()

def container_list():
    container_list = []
    for container in containers:
        container_list.append(tuple([container.short_id, container.name, container.status]))
    return container_list

def launcher_menu():
     # We also want a quicklist 
    launcher = Unity.LauncherEntry.get_for_desktop_id ("dockerui.desktop")
    launcher.set_property("count", len(containers))
    launcher.set_property("count_visible", True)
    ql = Dbusmenu.Menuitem.new ()

    for container in containers:
        item = Dbusmenu.Menuitem.new ()
        item.property_set (Dbusmenu.MENUITEM_PROP_LABEL, container.name)
        item.property_set_bool (Dbusmenu.MENUITEM_PROP_VISIBLE, True)
        ql.child_append (item)

    launcher.set_property("quicklist", ql)

