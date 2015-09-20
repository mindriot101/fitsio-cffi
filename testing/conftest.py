import os
import pytest
import cffitsio


@pytest.fixture
def test_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture
def test_file(test_dir):
    return os.path.join(test_dir, 'all.fits')


@pytest.yield_fixture
def test_hdulist(test_file):
    with cffitsio.open_fits(test_file) as infile:
        yield infile
