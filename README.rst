===========
Piano
===========

Piano is an work-in-progress for building dynamic CMS-like sites 
consisting of componentized parts (such as pages or widgets) which can be 
assembled and configured at runtime.

It also is an evolving example demonstrating:

* Pyramid
* Traversal
* Buildout
* MongoDB and MongoKit
* Sphinx documentation


Installation
=========================

Buildout Setup
---------------------------
1. Install Python 2.7.2 x32

2. ``python bootstrap.py``

	.. warning:: Press <ENTER> after a seeing the buildout script is generated (don't know 
		why this hangs but been like that forever on Windows).

3. ``bin/buildout``


Generating Documentation
-------------------------------
1. ``bin/buildout install sphinx``

2. ``bin/sphinx-build docs docs/_build``

3. Navigate to docs/_build.html/index.html to read.



For more detailed information: 
==============================
* `Documentation on PyPi <http://packages.python.org/​piano>`_

* `Source on GitHub <https://github.com/kjq/piano>`_