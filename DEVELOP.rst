Using the development buildout
==============================

Create a virtualenv in the package::

    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg


Running tests
-------------

    $ tox

list all tox environments:

    $ tox -l
    py27-Plone43
    py27-Plone51
    py27-Plone52
    py37-Plone52
    build_instance
    code-analysis
    lint-py27
    lint-py37
    coverage-report

run a specific tox env:

    $ tox -e py37-Plone52

Generate bundle
---------------

To generate a new bundle, make sure you have a Plone instance running and create a new Plone site with the id "Plone" where you enable this addon.
After that, stop the instance and run  the folowing command in the Terminal.

    $ ./bin/plone-compile-resources -b anonymouseditpatterns-bundle
