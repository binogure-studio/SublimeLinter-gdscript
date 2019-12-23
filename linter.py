from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class GDLint(Linter):
    cmd = 'gdscript-linter ${args}'
    defaults = {
        'selector': 'source.gd'
    }
