.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/smc/master/docs/pics/smc.jpg
	:target: https://www.pololu.com/product/1373
	:width: 300px

Pololu Simple Motor Controller
=======================================

.. image:: https://travis-ci.org/MomsFriendlyRobotCompany/smc.svg?branch=master
    :target: https://travis-ci.org/MomsFriendlyRobotCompany/smc
.. image:: https://img.shields.io/pypi/v/smc.svg
    :target: https://github.com/MomsFriendlyRobotCompany/smc
.. image:: https://img.shields.io/pypi/l/smc.svg
    :target: https://github.com/MomsFriendlyRobotCompany/smc
.. image:: https://img.shields.io/pypi/pyversions/smc.svg
    :target:  https://pypi.python.org/pypi/smc/

This is a python driver library for the Pololu series of Simple Motor Controllers.


Install
---------

::

	pip install smc

Usage
-------

.. code-block:: python

	from smc import SMC
	import time

	mc = SMC('/dev/ttyUSB0', 115200)
	# open serial port and exit safe mode
	mc.init()

	# drive using 12b mode
	mc.speed(1000)
	time.sleep(3)
	mc.speed(-1000)
	time.sleep(3)

	# drive using 7b mode
	mc.speed7b(100)
	time.sleep(3)
	mc.speed7b(-100)
	time.sleep(3)

	# and stop motor
	mc.stop()


Board
----------

.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/smc/master/docs/pics/smc-back.jpg
	:width: 300px

.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/smc/master/docs/pics/smc-io.jpg
	:width: 300px

.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/smc/master/docs/pics/smc-wiring.jpg
	:width: 300px

MIT License
--------------

**Copyright (c) 2017 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
