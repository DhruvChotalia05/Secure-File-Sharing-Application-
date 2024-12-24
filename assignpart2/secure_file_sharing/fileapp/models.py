"""
############################
#  File Name: models.py
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


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model representing a file uploaded by a user
class File(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # ForeignKey relationship to the User model; if the user is deleted, their files are also deleted
    file = models.FileField(
        upload_to='encrypted_files/'
    )  # FileField to store the uploaded file; files are saved in the 'encrypted_files/' directory
    filename = models.CharField(
        max_length=255
    )  # Stores the name of the file as a string with a max length of 255 characters
    upload_date = models.DateTimeField(
        default=timezone.now
    )  # Timestamp for when the file was uploaded, defaults to the current time
    file_hash = models.CharField(
        max_length=64
    )  # Stores the SHA-256 hash of the file for integrity or encryption purposes
    is_encrypted = models.BooleanField(
        default=True
    )  # Boolean to indicate whether the file is encrypted

    def __str__(self):
        
        return self.filename

# Model representing the sharing of a file between users
class FileShare(models.Model):
    file = models.ForeignKey(
        File, on_delete=models.CASCADE
    )  # ForeignKey relationship to the File model; if the file is deleted, the share record is also deleted
    shared_by = models.ForeignKey(
        User, related_name='shared_files', on_delete=models.CASCADE
    )  # User who shares the file
    shared_with = models.ForeignKey(
        User, related_name='received_files', on_delete=models.CASCADE
    )  # User with whom the file is shared
    shared_date = models.DateTimeField(
        default=timezone.now
    )  # Timestamp for when the file was shared, defaults to the current time

    def __str__(self):
        
        return f"{self.file.filename} shared with {self.shared_with.username}"
