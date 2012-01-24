from setuptools import setup, find_packages
import os

version = '1.2.2'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (read('README.txt')
                    + '\n' +
                    read('js', 'spin', 'test_spin.js.txt')
                    + '\n' +
                    read('CHANGES.txt'))

setup(name='js.spin',
      version=version,
      description="Fanstatic packaging of spin.js",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Fanstatic Developers',
      author_email='fanstatic@googlegroups.com',
      license='BSD',
      packages=find_packages(),namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['hgtools'],
      install_requires=['fanstatic',
                        'setuptools',],
      entry_points={'fanstatic.libraries': ['spin.js = js.spin:library',],},)
      