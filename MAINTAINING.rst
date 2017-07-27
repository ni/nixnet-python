Maintaining nixnet
==================

Cutting a release
-----------------

Update the version

#. ``nixnet/VERSION``
#. Create release notes (``clog-cli`` can help)
#. Include release notes in commit messaage
#. Publish a PR

Tagging a release

#. (on master) ``git tag -a <VERSION>`` with the release notes as the message
#. ``git push --tags <UPSTREAM>``

Uploading packages

#. ``rm -Rf dist``
#. ``python setup.py sdist``
#. ``python setup.py bdist_wheel --universal``
#. ``twine upload dist/*``
