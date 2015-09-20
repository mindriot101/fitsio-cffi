import os
import pytest

import cffitsio


def test_create_file(tmpdir):
    filename = str(tmpdir.join('test.fits'))
    f = cffitsio.FitsFile.create(filename)
    assert os.path.isfile(filename)


def test_open_file(test_hdulist):
    assert isinstance(test_hdulist, cffitsio.FitsFile)


def test_read_hdus(test_hdulist):
    assert len(test_hdulist) == 3
