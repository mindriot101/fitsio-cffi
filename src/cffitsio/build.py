#!/usr/bin/env python
# -*- coding: utf-8 -*-


from cffi import FFI
ffi = FFI()

ffi.set_source('cffitsio._cfitsio',
        """
        #include <fitsio.h>

        static void report_error(int status) {
            fits_report_error(stderr, status);
        }

        """,
        libraries=['cfitsio'])

ffi.cdef("""
        typedef struct  {
            int filehandle;
            ...;
        } FITSfile;
        typedef struct {
            int HDUposition;
            ...;
        } fitsfile;

        int fits_open_file(fitsfile **fptr, const char *filename, int iomode, int *status);
        int fits_create_file(fitsfile **fptr, char *filename, int *status);
        int fits_create_img(fitsfile *fptr, int bitpix, int naxis, long *naxes, int *status);
        int fits_close_file(fitsfile *fptr, int *status);
        int fits_get_img_size(fitsfile *fptr, int maxdim, long *naxes, int *status);
        int fits_movnam_hdu(fitsfile *fptr, int hdutype, char *extname, int extver, int *status);
        void fits_get_errstatus(int status, char *err_text);
        static void report_error(int status);

        """)



if __name__ == '__main__':
    ffi.compile()
