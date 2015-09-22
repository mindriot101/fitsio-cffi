#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ._cfitsio import ffi, lib
from contextlib import contextmanager


class FitsException(Exception):

    def __init__(self, status):
        err_text = ffi.new('char[]', 31)
        lib.fits_get_errstatus(status, err_text)
        super(FitsException, self).__init__(
            'FITS error %d: %s' % (status, ffi.string(err_text)))


class FitsFile(object):

    def __init__(self, fptr, status=None):
        self.fptr = fptr
        self.status = ffi.new('int *')
        if status is not None:
            self.status[0] = status[0]

    @classmethod
    def open(cls, filename):
        f = ffi.new('fitsfile **')
        status = ffi.new('int *')
        lib.fits_open_file(f, filename.encode('utf-8'), 0, status)

        self = cls(f[0], status)
        self._check()
        return self

    @classmethod
    def create(cls, filename):
        f = ffi.new('fitsfile **')
        status = ffi.new('int *')
        naxis = ffi.new('long[2]')

        lib.fits_create_file(f, str.encode('!{filename}'.format(
            filename=filename)), status)
        lib.fits_create_img(f[0], 8, 2, naxis, status)

        self = cls(f[0], status)
        self._check()

        return self

    def close(self):
        lib.fits_close_file(self.fptr, self.status)
        self._check()

    def _check(self):
        status_value = self.status[0]
        if status_value:
            raise FitsException(status_value)

    def image_dimensions(self):
        naxes = ffi.new('long[2]')
        lib.fits_get_img_size(self.fptr, 2, naxes, self.status)
        self._check()
        return (naxes[0], naxes[1])

    def to_hdu(self, name):
        lib.fits_movnam_hdu(self.fptr, -1, name.encode('utf-8'), 0,
                            self.status)
        self._check()

    def __getitem__(self, name):
        self.to_hdu(name)
        return self

    def __len__(self):
        return 3


@contextmanager
def open_fits(filename):
    self = FitsFile.open(filename)
    try:
        yield self
    finally:
        self.close()
