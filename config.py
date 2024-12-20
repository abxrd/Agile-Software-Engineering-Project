import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = ('postgresql://neondb_owner:aAqfh58BHuLG@ep-restless-glitter-a2ab5pov-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require')

    # Uncomment below line when running locally and comment out line 5
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///Software-Engineering-Aglie-Project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False