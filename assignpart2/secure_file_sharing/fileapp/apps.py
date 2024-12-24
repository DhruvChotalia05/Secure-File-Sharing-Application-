"""
############################
#  File Name: apps.py
#  Group Number: 11
#  Group Members Names : Dhruv Chotalia and Mitkumar Patel
#  Group Members Seneca Email : dchotalia@myseneca.ca , mdpatel38@myseneca.ca
#  Date : 2024-11-20
#  Authenticity Declaration :
#  I declare this submission is the result of our group work and has not been
#  shared with any other groups/students or 3rd party content provider. This submitted
#  piece of work is entirely of my own creation.
############################
"""

from django.apps import AppConfig

# Define the configuration for the 'fileapp' application
class FileappConfig(AppConfig):

    # Specify the type of auto-generated primary key fields for models
    default_auto_field = "django.db.models.BigAutoField"
    
    # Set the name of the application
    name = "fileapp"
