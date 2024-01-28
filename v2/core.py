# https://github.com/serv0id/learnyst-research
import base64
import json
from typing import Union

from loguru import logger

from v2.config import *
from .. import utils


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
        self.enc_type = EncAlgo.NONE  # default
        self.is_paid = False  # default

        self.set_parameters()

    def set_parameters(self) -> None:

        envelope = utils.parse_envelope_DRMREQ(self.request)
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
