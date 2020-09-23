def replace_ci(data, target, replacement=''):
	# Sanity.
	try:
		data = str(data)
		target = str(target)
		replacement = str(replacement)
	except:
		return False
	# Requirements.
	if not all([data, target]):
		return False
	# Prepare data.
	data_lower = data.lower()
	target_lower = target.lower()
	target_length = len(target)
	replacement_length = len(replacement)
	start = 0
	# Keep finding target until it does not exist.
	while (index := data_lower.find(target_lower, start)) != -1:
		# Remove target.
		data_lower = data_lower[:index] + data_lower[index+target_length:]
		data = data[:index] + data[index+target_length:]  
		# Add replacement.
		data_lower = data_lower[:index] + replacement + data_lower[index:]
		data = data[:index] + replacement + data[index:]
		# Don't find what we've already replaced.
		start = index+replacement_length
	return data
