from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

"""This module exports the GDScript plugin class."""

class GDLint(Linter):
    cmd = 'gdscript-linter ${file}'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    multiline = False
    defaults = {
        'selector': 'source.gd, source.gdscript'
    }
