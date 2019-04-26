from setuptools import setup

setup(name='csv_comparison_package',
      version='1.1',
      description='Compare two CSV files',
      url='https://github.jpl.nasa.gov/SQAGroup/csv_comparison_package',
      author='Saba Janamian',
      author_email='saba.janamian@jpl.nasa.gov',
      license='MIT',
      packages=['csv_comparison_package'],
      install_requires=[
          'chardet',
          'xlsxwriter',
          'pandas',
          'numpy',
          'pytest'
      ],
      zip_safe=False)
