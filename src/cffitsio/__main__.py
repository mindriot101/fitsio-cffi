from cffitsio import FitsFile, open_fits

if __name__ == '__main__':
    try:
        f = FitsFile.create('test.fits')
        f.close()

        fname = '/Users/simon/work/NGTS/pipeline/ZLP/zlp-flagging/testing/data/test.cat'
        with open_fits(fname) as infile:
            pass

    except FitsException as err:
        print(str(err))

