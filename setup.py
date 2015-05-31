from setuptools import setup, find_packages

setup(
        name='cffitsio',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        setup_requires=['cffi>=1.0.0'],
        cffi_modules=['src/cffitsio/build.py:ffi'],
        install_requires=['cffi>=1.0.0'],
        )
