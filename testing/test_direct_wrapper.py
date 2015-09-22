import os
import pytest

from cffitsio._cfitsio import ffi, lib


@pytest.fixture
def fits_open_file(test_file):
    f = ffi.new('fitsfile **')
    status = ffi.new('int *')
    lib.fits_open_file(f, test_file, 0, status)
    assert status[0] == 0
    return (f, status)


def test_create_file(tmpdir):
    filename = str(tmpdir.join('test.fits'))
    f = ffi.new('fitsfile **')
    status = ffi.new('int *')
    lib.fits_create_file(f, filename, status)
    assert status[0] == 0
    assert os.path.isfile(filename)


def test_open_file(test_file):
    f = ffi.new('fitsfile **')
    status = ffi.new('int *')
    lib.fits_open_file(f, test_file, 0, status)
    assert status[0] == 0


def test_close_file(test_file):
    f = ffi.new('fitsfile **')
    status = ffi.new('int *')
    lib.fits_open_file(f, test_file, 0, status)
    assert status[0] == 0
    lib.fits_close_file(f[0], status)
    assert status[0] == 0


def test_get_hdu_num(fits_open_file):
    f, status = fits_open_file
    # Should be open on the first hdu
    hdunum = ffi.new('int *')
    lib.fits_get_hdu_num(f[0], hdunum)
    assert hdunum[0] == 1


def test_fits_movabs_hdu(fits_open_file):
    f, status = fits_open_file
    exttype = ffi.new('int *')
    lib.fits_movabs_hdu(f[0], 2, exttype, status)

    hdunum = ffi.new('int *')
    lib.fits_get_hdu_num(f[0], hdunum)
    assert hdunum[0] == 2
