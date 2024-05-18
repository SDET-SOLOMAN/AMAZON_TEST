import os
from dotenv import load_dotenv


class UserData:
    load_dotenv()
    email = os.environ["email"]
    password = os.environ["password"]
    incorrect_email = ['2345asdghjkk@gmail.com']


