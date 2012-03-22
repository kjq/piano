Installation
------------

Setting up the environment
##########################
1. Uninstall Python
	If you have not used virtualenv or buildout your eggs are probably
	weirded out.

2. Install Python 2.7.2 x32
	x64 had issues at the time for me on different environments.

3. Set ``PYTHONHOME``				
	Where you installed Python

4. Checkout code someplace 		
	I used /work/piano


Installation using Buildout
###########################
1. Go into the directory you checked the code into.
	If there is *no* bootstrap.py file then use WGET to fetch it.
	
	wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

2. ``python bootstrap.py``

	.. warning:: Press <ENTER> after a seeing the buildout script is generated (don't know 
		why this hangs but been like that forever on Windows).

3. ``bin/buildout``
	After running the buildout command for the first time you only need to run
	it again when dependencies change.


Install MongoDB on Unix
##########################
1. ``bin/buildout install mongodb``


Install MongoDB on Windows
##########################
1. ``bin/buildout install mongodb-winXX`` (64 or 32)

.. note:: You only need to do this when you first setup your environment.


Generating Sphinx Documentation
###############################
1. ``bin/buildout install sphinx``

2. ``bin/sphinx-build docs docs/_build``
