from importlib.metadata import PackageNotFoundError, version

import pytest

from aldenv import __version__


def test_version_matches_metadata():
    """`aldenv.__version__` is the single source of truth for the version,
    so the installed distribution metadata has to agree with it."""
    try:
        installed = version("aldenv")
    except PackageNotFoundError:
        pytest.skip("aldenv is not installed; nothing to compare against")
    assert __version__ == installed
