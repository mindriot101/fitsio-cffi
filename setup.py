from setuptools import setup

setup(
        name='example',
        py_modules=['example'],
        setup_requires=['cffi>=1.0.0'],
        cffi_modules=['example_build.py:ffi'],
        install_requires=['cffi>=1.0.0'],
        )
