#!/usr/bin/env python

import os
from setuptools import setup
import sys

import cupy_setup_build


if sys.version_info[:3] == (3, 5, 0):
    if not int(os.getenv('CUPY_PYTHON_350_FORCE', '0')):
        msg = """
CuPy does not work with Python 3.5.0.

We strongly recommend to use another version of Python.
If you want to use CuPy with Python 3.5.0 at your own risk,
set 1 to CUPY_PYTHON_350_FORCE environment variable."""
        print(msg)
        sys.exit(1)


setup_requires = [
    'fastrlock>=0.3',
]
install_requires = [
    'numpy>=1.9.0',
    'six>=1.9.0',
    'fastrlock>=0.3',
]

package_data = {
    'cupy': [
        'core/include/cupy/complex/arithmetic.h',
        'core/include/cupy/complex/catrig.h',
        'core/include/cupy/complex/catrigf.h',
        'core/include/cupy/complex/ccosh.h',
        'core/include/cupy/complex/ccoshf.h',
        'core/include/cupy/complex/cexp.h',
        'core/include/cupy/complex/cexpf.h',
        'core/include/cupy/complex/clog.h',
        'core/include/cupy/complex/clogf.h',
        'core/include/cupy/complex/complex.h',
        'core/include/cupy/complex/complex_inl.h',
        'core/include/cupy/complex/cpow.h',
        'core/include/cupy/complex/cproj.h',
        'core/include/cupy/complex/csinh.h',
        'core/include/cupy/complex/csinhf.h',
        'core/include/cupy/complex/csqrt.h',
        'core/include/cupy/complex/csqrtf.h',
        'core/include/cupy/complex/ctanh.h',
        'core/include/cupy/complex/ctanhf.h',
        'core/include/cupy/complex/math_private.h',
        'core/include/cupy/carray.cuh',
        'core/include/cupy/complex.cuh',
        'core/include/cupy/atomics.cuh',
        'cuda/cupy_thrust.cu',
    ],
}

package_data['cupy'] += cupy_setup_build.prepare_wheel_libs()

package_name = cupy_setup_build.get_package_name()
long_description = cupy_setup_build.get_long_description()
ext_modules = cupy_setup_build.get_ext_modules()
build_ext = cupy_setup_build.custom_build_ext
sdist = cupy_setup_build.sdist_with_cython

here = os.path.abspath(os.path.dirname(__file__))
# Get __version__ variable
exec(open(os.path.join(here, 'cupy', '_version.py')).read())

setup(
    name=package_name,
    version=__version__,  # NOQA
    description='CuPy: NumPy-like API accelerated with CUDA',
    long_description=long_description,
    author='Seiya Tokui',
    author_email='tokui@preferred.jp',
    url='https://docs-cupy.chainer.org/',
    license='MIT License',
    packages=[
        'cupy',
        'cupy.binary',
        'cupy.core',
        'cupy.creation',
        'cupy.cuda',
        'cupy.cuda.memory_hooks',
        'cupy.ext',
        'cupy.fft',
        'cupy.indexing',
        'cupy.io',
        'cupy.linalg',
        'cupy.logic',
        'cupy.manipulation',
        'cupy.math',
        'cupy.padding',
        'cupy.prof',
        'cupy.random',
        'cupy.sorting',
        'cupy.sparse',
        'cupy.sparse.linalg',
        'cupy.statistics',
        'cupy.testing',
        'cupyx',
        'cupyx.scipy',
        'cupyx.scipy.ndimage',
        'cupyx.scipy.sparse',
        'cupyx.scipy.sparse.linalg',
        'cupyx.scipy.special',
        'cupyx.scipy.linalg',
        'cupyx.linalg',
        'cupyx.linalg.sparse'
    ],
    package_data=package_data,
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=['mock',
                   'pytest'],
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext,
              'sdist': sdist},
)
