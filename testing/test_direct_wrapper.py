import os

from cffitsio._cfitsio import ffi, lib


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


def test_get_hdu_num(test_file):
    f = ffi.new('fitsfile **')
    status = ffi.new('int *')
    lib.fits_open_file(f, test_file, 0, status)
    assert status[0] == 0
    # Should be open on the first hdu
    hdunum = ffi.new('int *')
    lib.fits_get_hdu_num(f[0], hdunum)
    assert hdunum[0] == 1
