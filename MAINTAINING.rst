Maintaining nixnet
==================

Cutting a release
-----------------

Update the version

#. ``pyproject.toml``
#. ``nixnet/VERSION``
#. ``README.rst``
#. Create release notes (`clog-cli <https://github.com/clog-tool/clog-cli/releases>`__ can help)
#. ``git clean -ndx`` to see what files to clean up
#. ``git clean -fdx`` to clean up files
#. Include release notes in commit messaage
#. Publish a PR

Tagging a release

#. (on main) ``git tag -a v<X>.<Y>.<Z>`` with the release notes as the message
#. ``git push <UPSTREAM> main --tag v<X>.<Y>.<Z>``
#. Go to https://github.com/ni/nixnet-python/releases
#. The new release should be there, but it will be poorly formatted.
#. Draft a new release. Use the same tag version. You don't need to attach any new files.

Uploading packages to PyPI

#. ``poetry config pypi-token.pypi <PyPI API token>`` (only need to be done once)
#. ``rm -Rf dist``
#. ``poetry publish --build``
