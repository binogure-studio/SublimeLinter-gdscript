from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class GDLint(Linter):
    cmd = 'gdscript-linter ${args}'
    regex = r''
    multiline = False
    defaults = {
        'selector': 'source.gd'
    }
