try:
	from setuptools import setup 
except:
	from disutils.core import setup

import minervashadow_api


dependencies = ['Flask>=0.7.2', 'MarkupSafe']

setup(

	name='minervashadow_api',
	version=minervashadow_api.get_version(),
	description='OpenShift App to make the minervashadow_api available to the public',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minervashadow-api',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies,
	classifiers={
		'Development Status :: 1 - Alpha',
		'Intended Audience :: Developers',
		'NaturalLanguage :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
	}
)
