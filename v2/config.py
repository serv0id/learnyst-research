# https://github.com/serv0id/learnyst-research
from enum import Enum

# Enums
class EncAlgo(Enum):
	NONE = 1
	AES = 2
	
# API Paths
V2_LSTDRM_URL = 'https://drm-u.learnyst.com/drmv2/lstdrm'
V2_WIDEVINE_URL = 'https://drm-u.learnyst.com/drmv2/lgdrm'
V2_PLAYREADY_URL = 'https://drm-u.learnyst.com/drmv2/playready' # taken from edge

# Secrets
INIT_AES_KEY = '2B735516481ED5361BF775AAC9CF2F31'
INIT_AES_IV = '1227F2F34367F60768F9F2592367FEF1'

STATIC_AES_KEY = b'gij834zbhu091jitbk29g6av90k4bjgy'