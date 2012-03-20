import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

requires = [
    'docutils',
    'mongokit',        #Fork of MongoKit by same author is MongoLite
    'pymongo',
    'pyramid',
    'pyramid_beaker',
    'pyramid_debugtoolbar',
    'simplejson',
    'waitress',
    'webhelpers'
    ]

setup(name='piano',
      version='0.0',
      description='CMS built using Pyramid and MongoDB',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='KimJohn Quinn',
      author_email='kjq@logicdrop.com',
      url='www.logicdrop.com',
      keywords='pyramid mongodb beaker buildout cms',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="piano",
      entry_points = """\
      [paste.app_factory]
      main = piano:main
      """,
      )

