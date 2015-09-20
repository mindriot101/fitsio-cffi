import pytest

import cffitsio

def test_image_dimensions(test_hdulist):
    hdu = test_hdulist['image']
    assert hdu.image_dimensions() == (100, 100)
