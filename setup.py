#! /usr/bin/env python

import sys
import os
import setuptools
import numpy
from numpy.distutils.core import setup
from setuptools import find_packages

DISTNAME = 'hiDF'
DESCRIPTION = "hiDF"
URL = "https://github.com/anonymousICDM2021/DM487"
MAINTAINER = 'anonymousICDM2021'
MAINTAINER_EMAIL = 'anonymous'
LICENSE = 'new BSD'
VERSION = '0.1.0'


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.add_subpackage('hiDF')

    return config

if __name__ == "__main__":

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    os.chdir(local_path)
    sys.path.insert(0, local_path)
    setup(configuration=configuration,
          name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          packages=find_packages(),
          include_package_data=True,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: C',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'
            ],
          install_requires=[
              "numpy",
              "scipy",
              "scikit-learn>=0.22",
              "cython",
              "pyfpgrowth",
              "pyspark",
              "pyyaml",
              "pydotplus",
          ],
          setup_requires=["cython"])
