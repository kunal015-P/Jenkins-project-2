import os


class Config:
    APP_NAME = "Python CI App"
    DEBUG = os.getenv("DEBUG", "False") == "True"
