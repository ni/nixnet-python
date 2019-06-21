Maintaining nixnet
==================

Cutting a release
-----------------

Update the version

#. ``nixnet/VERSION``
#. ``README.rst``
#. Create release notes (`clog-cli <https://github.com/clog-tool/clog-cli/releases>`__ can help)
#. ``git clean -ndx`` to see what files to clean up
#. ``git clean -fdx`` to clean up files
#. Include release notes in commit messaage
#. Publish a PR

Tagging a release

#. (on master) ``git tag -a v<X>.<Y>.<Z>`` with the release notes as the message
#. ``git push <UPSTREAM> master --tag v<X>.<Y>.<Z>``

Uploading packages

#. ``rm -Rf dist``
#. ``python setup.py sdist``
#. ``python setup.py bdist_wheel --universal``
#. ``twine upload dist/*``
