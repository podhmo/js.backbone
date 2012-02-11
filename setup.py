from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an incrementing integer.
# For example, a packaging bugfix release version 0.9.4 of the js.jquery package would be version 0.9.4-1 .

version = '0.9.1-4'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (read('README.txt')
                    + '\n' +
                    read('js', 'backbone', 'test_backbone.js.txt')
                    + '\n' +
                    read('CHANGES.txt'))

setup(name='js.backbone',
      version=version,
      description="Fanstatic packaging of backbone.js",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='podhmo podhmo',
      author_email='podhmo@example.jp',
      url="https://github.com/podhmo/js.backbone",
      license='BSD',
      packages=find_packages(),namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['hgtools'],
      install_requires=['fanstatic',
                        'setuptools',
                        'js.underscore'],
      entry_points={'fanstatic.libraries': ['backbone.js = js.backbone:library',],},)
