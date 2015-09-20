import pytest
import cffitsio
import os


@pytest.fixture
def test_dir():
    return os.path.join(
        os.path.dirname(__file__),
        'data')


@pytest.fixture
def test_file(test_dir):
    return os.path.join(test_dir, 'all.fits')


def test_create_file(tmpdir):
    filename = str(tmpdir.join('test.fits'))
    f = cffitsio.FitsFile.create(filename)
    assert os.path.isfile(filename)


def test_open_file(test_file):
    with cffitsio.open_fits(test_file) as infile:
        assert isinstance(infile, cffitsio.FitsFile)


def test_read_hdus(test_file):
    with cffitsio.open_fits(test_file) as infile:
        assert len(infile) == 3
