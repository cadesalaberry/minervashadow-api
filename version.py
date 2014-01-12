VERSION = (0, 0, 1, 'alpha', 0)

def get_version(version=None):
	"""
	Returns a PEP 386-compliant version number from VERSION.
	"""
	
	main_version, sub_version = '', ''

	if version is None:
		version = VERSION
	else:
		assert len(version) == 5
		assert version[3] in ('alpha', 'beta', 'rc', 'final')
		

	parts = 2 if version[2] == 0 else 3
	main_version = '.'.join(str(x) for x in version[:parts])

	if version[3] != 'final':
		mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
		sub_version = mapping[version[3]] + str(version[4])
	else:
		pass

	return str(main_version + sub_version)