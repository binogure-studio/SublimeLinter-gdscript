from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

"""This module exports the GDScript plugin class."""

class GDLint(Linter):
  # cmd = 'gdscript-linter ${file}'

  regex = r'^.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
  multiline = False
  defaults = {
      'selector': 'source.gd, source.gdscript'
  }

  def cmd(self):
    settings = self.settings
    command = ['gdscript-linter']

    if 'root_folder' in settings:
      command.extend(['-p', settings.get('root_folder')])

    command.append(self.filename)

    return command
