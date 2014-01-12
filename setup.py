try:
	from setuptools import setup 
except:
	from disutils.core import setup

import version


dependencies = ['Flask>=0.7.2', 'MarkupSafe']

setup(

	name='minervashadow_api',
	version=version.get_version(),
	description='OpenShift App to make the minervashadow-api available to the public',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minervashadow-api',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies
)