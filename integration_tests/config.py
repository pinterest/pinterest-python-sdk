import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_BOARD_ID = os.environ.get('DEFAULT_BOARD_ID', "")
DEFAULT_BOARD_NAME = os.environ.get('DEFAULT_BOARD_NAME', "")
DEFAULT_PIN_ID = os.environ.get('DEFAULT_PIN_ID', "")
DEFAULT_BOARD_SECTION_ID = os.environ.get('DEFAULT_BOARD_SECTION_ID', "")
OWNER_USER_ID = os.environ.get('OWNER_USER_ID', "")
DEFAULT_AD_ACCOUNT_ID = os.environ.get('DEFAULT_AD_ACCOUNT_ID', "")
DEFAULT_AD_ID = os.environ.get('DEFAULT_AD_ID', "")
DEFAULT_AD_GROUP_ID = os.environ.get('DEFAULT_AD_GROUP_ID', "")
DEFAULT_CAMPAIGN_ID = os.environ.get('DEFAULT_CAMPAIGN_ID', "")
