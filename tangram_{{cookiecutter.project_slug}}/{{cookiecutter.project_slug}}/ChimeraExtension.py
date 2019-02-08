#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
import chimera

class {{cookiecutter.project_name}}Extension(chimera.extension.EMO):

    def name(self):
        return 'Tangram {{cookiecutter.project_title}}'

    def description(self):
        return "{{cookiecutter.project_description}}"

    def categories(self):
        return ['InsiliChem']

    def icon(self):
        return

    def activate(self):
        self.module('gui').showUI()


chimera.extension.manager.registerExtension({{cookiecutter.project_name}}Extension(__file__))