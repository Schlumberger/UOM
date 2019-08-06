"""Python Package setup."""
from setuptools import setup


def requirements():
    """Requirement from source."""
    with open('requirements.txt', 'r') as fil:
        return fil.read().splitlines()


def readme():
    """Readme from source."""
    with open('README.md', 'r') as fil:
        return fil.read()

setup(name='uom',
      version='0.3.3',
      description='Unit of Measure conversion tool',
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Customer Service',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Information Analysis'],
      keywords='uom unit measurement measure energistics oilfield',
      url='http://github.com/schlumberger/UOM',
      author='Velizar VESSELINOV',
      author_email='vvesselinov@slb.com',
      license='MIT',
      packages=['uom'],
      install_requires=requirements(),
      test_suite='uom.tests',
      entry_points={
          'console_scripts': ['uom_convert_value=uom.cmd_line:cmd_convert',
                              'uom_base_unit=uom.cmd_line:cmd_base_unit'],
      },
      include_package_data=True,
      zip_safe=False)
