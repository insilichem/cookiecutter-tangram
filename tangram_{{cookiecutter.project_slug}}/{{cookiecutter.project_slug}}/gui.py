#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
# Python stdlib
import Tkinter as tk
import Pmw
# Chimera stuff
import chimera
# Own
from libtangram.ui import TangramBaseDialog, STYLES
from . import __version__


ui = None  # singleton
def showUI():
    if chimera.nogui:
        tk.Tk().withdraw()
    global ui
    if not ui:
        ui = {{cookiecutter.project_name}}Dialog()
    ui.enter()


class {{cookiecutter.project_name}}Dialog(TangramBaseDialog):

    buttons = ('OK', 'Close')
    default = None
    help = "https://github.com/insilichem/tangram_{{cookiecutter.project_slug}}"
    VERSION = __version__
    VERSION_URL = "https://api.github.com/repos/insilichem/tangram_{{cookiecutter.project_slug}}/releases/latest"

    def __init__(self, *args, **kwargs):
        # GUI init
        self.title = 'Tangram {{cookiecutter.project_title}}'
        self.controller = None

        # Fire up
        super({{cookiecutter.project_name}}Dialog, self).__init__(resizable=False, *args, **kwargs)

    def fill_in_ui(self, parent):
        pass
