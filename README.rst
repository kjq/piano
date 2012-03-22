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

1. Install Python 2.7.2 x32

2. ``python bootstrap.py``

3. ``bin/buildout``

4. ``bin/buildout install sphinx``

5. ``bin/sphinx-build docs docs/_build``

Navigate to docs/_build.html/index.html to read.