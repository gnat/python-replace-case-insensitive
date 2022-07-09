def str_ireplace(data, target, replacement='', default=False):
	"""
	Case-insensitive version of string replace.
	Does not use regex in order to prevent redos attack.
	Return default (False) if there is an issue.
	"""
	try:
		data = str(data)
		target = str(target)
		replacement = str(replacement)
		# Required.
		if not data or not target:
			return default
	except:
		return default
	# Cache for speed.
	data_lower = data.lower()
	target_lower = target.lower()
	target_length = len(target)
	replacement_length = len(replacement)
	position = 0
	# Keep finding target until it does not exist.
	while (index := data_lower.find(target_lower, position)) != -1:
		# Add replacement and remove target.
		data_lower = data_lower[:index] + replacement + data_lower[index+target_length:]
		data = data[:index] + replacement + data[index+target_length:]
		# Don't find what we've already replaced.
		position = index+replacement_length
	return data
