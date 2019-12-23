from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

"""This module exports the GDScript plugin class."""

class GDLint(Linter):
    cmd = 'gdscript-linter ${file}'
    multiline = False
    defaults = {
        'selector': 'source.gd, source.gdscript'
    }
