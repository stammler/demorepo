Unit Tests & Code Coverage
==========================

The units tests for this project are stored in the ``tests/`` directory.



Prerequisites
-------------

To run the unit tests ``pytest`` needs to be installed. For analysis
on code coverage, additionally ``pytest-cov`` needs to be installed.
This can be done with pip:

.. code-block:: console

   $ pip install pytest pytest-cov



Unit Tests
----------

To run the unit tests, simply run

.. code-block:: console

   $ pytest

in the base directory of the repository. The output will then look:
like this

.. code-block:: console

   ================================== test session starts ===================================
   platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
   rootdir: /mnt/c/Users/sebas/physics/repos/sphinx_demo
   configfile: pyproject.toml
   plugins: cov-5.0.0
   collected 9 items
   
   tests/test_arithmetic.py ....                                                       [ 44%]
   tests/test_inputs.py .....                                                          [100%]
   
   =================================== 9 passed in 0.35s ====================================



Code Coverage
-------------

Code coverage will additionally test if every line of the software is covered
by a unit test. To run the unit tests with code coverage simply type:

.. code-block:: console

   $ pytest --cov=calculator

The result will the look like this:

.. code-block:: console

   ================================== test session starts ===================================
   platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
   rootdir: /home/username/demorepo
   configfile: pyproject.toml
   plugins: cov-5.0.0
   collected 9 items

   tests/test_arithmetic.py ....                                                      [ 44%]
   tests/test_inputs.py .....                                                         [100%]

   ---------- coverage: platform linux, python 3.12.3-final-0 -----------
   Name                           Stmts   Miss  Cover
   --------------------------------------------------
   calculator/__init__.py             3      0   100%
   calculator/calculator.py          22      0   100%
   calculator/utils/__init__.py       2      0   100%
   calculator/utils/utils.py          3      0   100%
   --------------------------------------------------
   TOTAL                             30      0   100%
   
   
   =================================== 9 passed in 1.39s ====================================

`pytest-cov` can also report code coverage with html files. To enable this
run:

.. code-block:: console

   $ pytest --cov=calculator --cov-report=html

The report can then be accessed in the ``htmlcov`` directory. This
is especially useful to inspect which lines of code either failed
or are not covered by unit tests.