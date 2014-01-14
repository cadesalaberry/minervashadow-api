try:
	from setuptools import setup 
except:
	from disutils.core import setup

import version


dependencies = ['Flask>=0.7.2', 'MarkupSafe', 'minervashadow']

dependency_links = [
'https://pypi.python.org/pypi/minervashadow',
'https://github.com/cadesalaberry/minervashadow'
'git+https://github.com/cadesalaberry/minervashadow.git'
'https://github.com/cadesalaberry/minervashadow/tarball/master#egg=minervashadow-0.0.3a1'
]

setup(

	name='minervashadow_api',
	version=version.get_version(),
	description='A JSON API to the aging minerva website.',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minervashadow-api',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies,
	dependency_links=dependency_links,
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Natural Language :: French',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Framework :: Flask'
	]
)