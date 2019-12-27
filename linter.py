from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

"""This module exports the GDScript plugin class."""

class GDLint(Linter):
  # cmd = 'gdscript-linter ${file}'
  cmd = None

  regex = r'^.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
  multiline = False
  defaults = {
      'selector': 'source.gd, source.gdscript'
  }

  def cmd(self):
    command = ['gdscript-linter']

    if 'root_folder' in self.settings:
      command.append('-p')
      command.append(self.settings.get('root_folder'))

    command.append(self.filename)

    return command
