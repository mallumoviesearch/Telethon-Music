import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14623143"))
    API_HASH = os.environ.get("API_HASH", "51ee2679d47d66aed5795876afc67622")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2144257146:AAEQC6BEjEr674aisQYzMUbLsSXyTahJIcY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBu3HXp6-aUeaJVlJyZZmXP6yrVLViSQee0enfYcRoKvpNLC7H6kRj-0iDh8rZJpmnNaqQPHEoOxlSvXqhyhMUangTpSHyGBTvLPYMj8eS5yc3mFLPmyyJj4TpOwtak6ISeOLi3XNc4a2izyCOf3P6V3-Q3c4ph3E4Ly03ZcJj9u2Nx8Nk0s1bRqpn6TMjFNo7zlfitYWcVi1sq_P6gA5SdrU2fwmllrRGSesn_Ddr5TB4tMPLaaGei98L1po70Zq1Or5zgiXV231KYdApzLV1sijcXFO_QiOBAJq6JwF7trUfSPxegB1vvZZoxeWTEuRCsh_w_IoH0OaWvVGdIT39qUM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
