import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'docutils',
    'mongokit', #Fork of MongoKit by same author is MongoLite
    'pymongo',
    'pyramid',
    'pyramid_beaker',
    'pyramid_debugtoolbar',
    'simplejson',
    'waitress',
    'webhelpers'
    ]

setup(name='piano',
      version='0.2',
      description='CMS built using Pyramid and MongoDB',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Office/Business",
        ],
      author='KimJohn Quinn',
      author_email='kjq@logicdrop.com',
      url='https://github.com/kjq/piano',
      keywords='pyramid mongodb beaker buildout cms',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="piano",
      entry_points="""\
      [paste.app_factory]
      main = piano:main
      """,
      )

