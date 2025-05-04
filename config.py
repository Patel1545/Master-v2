import os

class Config(object):
    BOT_TOKEN = os.environ.get("8195022474:AAHIyxQ9jlRj3DOeAUmjwTsL_mrymOEjlLg")
    API_ID = int(os.environ.get("29267685"))
    API_HASH = os.environ.get("9aea863501d41261e6c75ad565b6e1e1")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(7916516048) for user_id in VIP_USER]
