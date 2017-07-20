Maintaining nixnet
==================

Cutting a release
-----------------

Update the version

#. ``nixnet/VERSION``
#. ``docs/conf.py``'s ``version`` and ``release`` fields
#. Create PR

Tagging a release

#. Create release notes (``clog-cli`` can help)
#. (on master) ``git tag -a <VERSION>`` with the release notes as the message
#. ``git push --tags <UPSTREAM>``

Uploading packages

#. ``rm -Rf dist``
#. ``python setup.py sdist``
#. ``python setup.py bdist_wheel --universal``
#. ``twine upload dist/*``
