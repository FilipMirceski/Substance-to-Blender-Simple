# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Substance to Blender Simple",
    "author" : "FKJ",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Material"
}

from . import create_material_ui
from . import import_file
from . import create_mat

#auto_load.init()

def register():
    create_material_ui.register()
    import_file.register()
    create_mat.register()



def unregister():
    create_material_ui.unregister()
    import_file.unregister()
    create_mat.unregister()



if __name__ == "__main__":
	register()
