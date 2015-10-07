from PyQt5 import uic
from subprocess import call


def compile_ui_files():
    uic.compileUiDir('/home/aurelien/sketchbook/arbo/src/gui', recurse=True, from_imports=True, execute=True, resource_suffix='')

    call(['pyrcc5', 'src/gui/icons/icons_rc.qrc', '-o', 'src/gui/icons/icons_rc.py'],
         cwd='/home/aurelien/sketchbook/arbo')


# Execute when importing module
compile_ui_files()



