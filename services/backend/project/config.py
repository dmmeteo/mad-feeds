# project/config.py
import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    MONGODB_DB = os.environ.get('DATABASE_NAME')
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    MONGODB_DB = os.environ.get('DATABASE_TEST_NAME')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    MONGODB_DB = os.environ.get('DATABASE_NAME')
    MONGODB_USERNAME = os.environ.get('DATABASE_NAME')
    MONGODB_PASSWORD = os.environ.get('DATABASE_NAME')
