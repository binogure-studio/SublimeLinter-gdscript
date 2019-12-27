This is a template. For "how to make a linter", please check [the HOWTO](HOWTO.md).

-----------------------------------------------------------------

SublimeLinter-contrib-gdscript
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-gdscript.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-gdscript)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [gdscript](https://github.com/binogure-studio/SublimeLinter-gdscript). It will be used with files that have the “gdscript” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `gdscript` is installed on your system.

In order for `gdscript` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

|Setting|Description    |
|:------|:--------------|
|root   |Path to the root folder that contains the engine.cfg file|
