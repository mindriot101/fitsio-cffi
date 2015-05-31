from cffitsio import FitsFile
import os

def test_create_file(tmpdir):
    filename = str(tmpdir.join('test.fits'))
    f = FitsFile.create(filename)
    assert os.path.isfile(filename)
