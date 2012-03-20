Buildout Usage
--------------

General commands
################
* ``bin/python``
	Runs python with project environment setup

* ``bin/test``
	Runs test cases 

* ``bin/buildout install pydev``
	Configures PyDev project for Eclipse (close/open project in Eclipse 
	afterwards)


Running the MongoDB Server
##########################
In order to connect to the MongoDB you will have to start the server first.

.. note:: Windows ONLY - do in a seperate DOS window from 'serve'

* Start
	``bin/buildout install mongod-win``

* Stop
	<CTRL-C> a couple of times


Running the Web Server
######################
In order to interact with the site you will have to start the server first.

* ``bin/serve``
	Runs the server on port 8080

* ``bin/pserve development.ini``
	Runs the server using a specified settings file.