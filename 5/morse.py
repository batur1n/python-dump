def encode_morze(text):
	code = {'A': '^_^^^',			'B': '^^^_^_^_^',		'C': '^^^_^_^^^_^',		'D': '^^^_^_^',
			'E': '^',				'F': '^_^_^^^_^',		'G': '^^^_^^^_^',		'H': '^_^_^_^',
			'I': '^_^',				'J': '^_^^^_^^^_^^^',	'K': '^^^_^_^^^',		'L': '^_^^^_^_^',
			'M': '^^^_^^^',			'N': '^^^_^',			'O': '^^^_^^^_^^^',		'P': '^_^^^_^^^_^',
			'Q': '^^^_^^^_^_^^^',	'R': '^_^^^_^',			'S': '^_^_^',			'T': '^^^',
			'U': '^_^_^^^',			'V': '^_^_^_^^^',		'W': '^_^^^_^^^',		'X': '^^^_^_^_^^^',
			'Y': '^^^_^_^^^_^^^',	'Z': '^^^_^^^_^_^',

			'0': '^^^_^^^_^^^_^^^_^^^', '1': '^_^^^_^^^_^^^_^^^', '2': '^_^_^^^_^^^_^^^',
			'3': '^_^_^_^^^_^^^',		'4': '^_^_^_^_^^^',       '5': '^_^_^_^_^',
			'6': '^^^_^_^_^_^',			'7': '^^^_^^^_^_^_^',     '8': '^^^_^^^_^^^_^_^', '9': '^^^_^^^_^^^_^^^_^',
			' ': '_'}
	return '___'.join(code.get(i.upper()) for i in text)

print(encode_morze('Morze code'))
print
print(encode_morze('Prometheus'))
print
print(encode_morze('SOS'))
print
print(encode_morze('1'))
print
