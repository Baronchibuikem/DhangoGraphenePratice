"""
    If you are running this code in production, change the 
    development_settings to production_settings.

    If you are running this code in a local pc, change the 
    production_settings to development_settings
"""
# uncomment this to use docker settings which is the same thing contained in the production setting
# from settings.docker import *

# Use this for running this project on your local machine
from settings.development_settings import *
print("------------------------------")
print("This is running on Sqlite Database")
print("------------------------------")


# uncomment this to use production settings
# from settings.production_settings import *
# print("------------------------------")
# print("This is running on Postgresql Database")
# print("------------------------------")
