# https://github.com/serv0id/learnyst-research
from json import JSONDecodeError
from typing import Union
import json
import base64
from loguru import logger

from Crypto.Cipher import AES
import v2.config as cfg


def parse_envelope_DRMREQ(request: str) -> Union[dict, None]:
    """
    Parses the outer envelope of the LSTDRM request sent by
    the browser (sent to the endpoint /lstdrm).
    """
    fixed_request = request[::-1][1:]

    # fix padding
    padding_int = len(fixed_request) % 4

    if padding_int == 2:
        fixed_request += "=="
    elif padding_int == 3:
        fixed_request += "="

    try:
        return json.loads(base64.b64decode(fixed_request.encode()))
    except JSONDecodeError:
        logger.error("Misformatted request! Are you sure this is v2?")


def get_signed_url(request: bytes) -> bytes:
    """
    Encrypt a JSON string containing course specific values 
    to be sent to learnyst servers to obtain a Signed URL 
    for content playback.
    """
    cipher = AES.new(cfg.SIGNED_URL_KEY,
                     AES.MODE_CTR,
                     initial_value=cfg.SIGNED_URL_IV,
                     nonce=b'')

    return base64.b64encode(cipher.encrypt(request))


def decrypt_signed_url(request: str) -> dict:
    """
    Decrypt a Base64 string sent to the Signed URL endpoint
    for information gatherning.
    """
    cipher = AES.new(cfg.SIGNED_URL_KEY,
                     AES.MODE_CTR,
                     initial_value=cfg.SIGNED_URL_IV,
                     nonce=b'')

    plain = cipher.decrypt(base64.b64decode(request.encode()))
    return json.loads(plain)
