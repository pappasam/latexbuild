# Change Log

All notable changes to this project will be documented in this file.

## [0.2.2] - 2017-04-05

* Revise latex string escape functionality to not try to escape objects that are not Python strings.
  * Thanks Brindesable!

## [0.2.1] - 2016-04-24

* Change DOCX build process to first build PDF to generate complete aux file THEN run laetx2rtf.

## [0.2.0] - 2016-04-24

* Added support for building Microsoft Word (.docx) files using latex2rtf

## [0.1.1] - 2016-04-16

* Fixed spelling errors in README

## [0.1.0] - 2016-04-16

* Add printing of STDOUT and STDERR to console for easier debugging of Latex processes
* Escape input Python strings for Latex
* Recursively clean dictionary / list input for Jinja2 templates

## [0.0.1] - 2016-04-14

* Project initialized and uploaded to pypi
