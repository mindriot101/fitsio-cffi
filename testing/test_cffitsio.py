import pytest
import cffitsio
import os


@pytest.fixture
def test_dir():
    return os.path.join(
        os.path.dirname(__file__),
        'data')

def test_create_file(tmpdir):
    filename = str(tmpdir.join('test.fits'))
    f = cffitsio.FitsFile.create(filename)
    assert os.path.isfile(filename)


def test_open_file(test_dir):
    filename = os.path.join(test_dir, 'all.fits')
    with cffitsio.open_fits(filename) as infile:
        assert isinstance(infile, cffitsio.FitsFile)
