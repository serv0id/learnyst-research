# Import and call this module from an external code to use it.
# https://github.com/serv0id/learnyst-research

import base64, json

def parse_envelope_DRMREQ(request: str) -> dict:
	"""
	Parses the outer envelope of the LSTDRM request sent by
	the browser (sent to the endpoint /lstdrm).
	"""
	fixed_request = request[::-1][1:]

	# fix padding
	padding_int = len(fixed_request) % 4
	
	if (padding_int == 2):
		fixed_request += "=="
	elif (padding_int == 3):
		fixed_request += "="

	return json.loads(base64.b64decode(fixed_request.encode()))

