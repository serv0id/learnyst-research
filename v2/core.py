# https://github.com/serv0id/learnyst-research
import base64, json
import requests
from loguru import logger
from typing import Union

class V2Base(object):
	def __init__(self, request: str):
		self.request = request

	def set_parameters(self) -> bool:
		"""
		Try to set platform-specific params
		from the request itself.
		"""
		self.parse_envelope_DRMREQ(self.request)

	@staticmethod
	def parse_envelope_DRMREQ(request: str) -> Union[dict, None]:
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

		try:
			return json.loads(base64.b64decode(fixed_request.encode()))
		except:
			logger.error("Misformatted request! Are you sure this is v2?")
