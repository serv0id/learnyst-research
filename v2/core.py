# https://github.com/serv0id/learnyst-research
import base64, json
import requests
from loguru import logger
from typing import Union
from v2.config import *

class V2Base(object):
	def __init__(self, request: str):
		self.request = request
		
		# Session-specific values
		self.version = None
		self.school_id = None
		self.student_id = None
		
		self.content_id = None
		self.content_path = None
		
		self.license_request = None
		self.app_type = None
		
		# Default
		self.enc_type = EncAlgo.NONE # default
		self.is_paid = False # default

		self.set_parameters()
	
	def set_parameters(self) -> None:
		"""
		Try to set platform-specific params
		from the request itself.
		"""
		envelope = self.parse_envelope_DRMREQ(self.request)
		get_param = lambda param: envelope[param] if envelope.get(param) is not None else '' 

		self.version = get_param("version")
		self.school_id = get_param("schoolId")
		self.student_id = get_param("studentId")
		self.content_id = get_param("contentId")
		self.content_path = get_param("contentPath")
		self.app_type = get_param("appType")
		
		if get_param("encAlgo") == "aes":
			self.enc_type = EncAlgo.AES

		if get_param("isPaid") == 1:
			self.is_paid = True

		# TODO: Figure out other parameters

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