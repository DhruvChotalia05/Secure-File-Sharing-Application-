"""
############################
#  File Name: test_file_sharing.py
#  Group Number: 11
#  Group Members Names : Dhruv Chotalia and Mitkumar Patel
#  Group Members Seneca Email : dchotalia@myseneca.ca , mdpatel38@myseneca.ca
#  Date : 2024-12-06
#  Authenticity Declaration :
#  I declare this submission is the result of our group work and has not been
#  shared with any other groups/students or 3rd party content provider. This submitted
#  piece of work is entirely of my own creation.
############################
"""
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from fileapp.models import File, FileShare

@pytest.mark.django_db
class TestFileSharing:

    def test_file_share(self, client, django_user_model):
        """
        Test file sharing between users.
        Verifies that a file can be successfully shared between two users.
        """
        # Create test users
        owner = django_user_model.objects.create_user(username='fileowner', password='Pass123!')
        recipient = django_user_model.objects.create_user(username='recipient', password='Pass456!')

        # Log in as file owner
        client.login(username='fileowner', password='Pass123!')

        # Create a test file
        test_file = SimpleUploadedFile(
            name='share_test.txt',
            content=b'Sharing test content',
            content_type='text/plain'
        )
        file_obj = File.objects.create(
            user=owner,
            filename='share_test.txt',
            file=test_file,
            is_encrypted=True
        )

        # Share the file with recipient
        share_data = {'username': 'recipient'}
        response = client.post(reverse('share_file', args=[file_obj.id]), share_data)

        # Verify file sharing was successful
        assert response.status_code == 302  # Redirect to success page
        assert FileShare.objects.filter(file=file_obj, shared_with=recipient).exists()

    def test_duplicate_file_share(self, client, django_user_model):
        """
        Test attempting to share a file that's already been shared.
        Verifies that sharing the same file multiple times does not create duplicates.
        """
        # Create test users
        owner = django_user_model.objects.create_user(username='fileowner', password='Pass123!')
        recipient = django_user_model.objects.create_user(username='recipient', password='Pass456!')

        # Log in as file owner
        client.login(username='fileowner', password='Pass123!')

        # Create a test file
        test_file = SimpleUploadedFile(
            name='duplicate_share_test.txt',
            content=b'Duplicate sharing test content',
            content_type='text/plain'
        )
        file_obj = File.objects.create(
            user=owner,
            filename='duplicate_share_test.txt',
            file=test_file,
            is_encrypted=True
        )

        # First share
        share_data = {'username': 'recipient'}
        client.post(reverse('share_file', args=[file_obj.id]), share_data)

        # Attempt to share again
        response = client.post(reverse('share_file', args=[file_obj.id]), share_data)

        # Verify that file is not shared again
        assert response.status_code == 200  # Same page, possibly with a warning
        assert FileShare.objects.filter(file=file_obj, shared_with=recipient).count() == 1

    def test_unauthorized_file_access(self, client, django_user_model):
        """
        Test that unauthorized users cannot access shared files.
        Verifies that a user who has not been granted access cannot download a file.
        """
        # Create test users
        file_owner = django_user_model.objects.create_user(username='owner', password='Pass123!')
        authorized_user = django_user_model.objects.create_user(username='authorized', password='Pass456!')
        unauthorized_user = django_user_model.objects.create_user(username='unauthorized', password='Pass789!')

        # Create a test file
        test_file = SimpleUploadedFile(
            name='private_file.txt',
            content=b'Private content',
            content_type='text/plain'
        )
        file_obj = File.objects.create(
            user=file_owner,
            filename='private_file.txt',
            file=test_file,
            is_encrypted=True
        )

        # Share file with authorized user
        FileShare.objects.create(
            file=file_obj,
            shared_by=file_owner,
            shared_with=authorized_user
        )

        # Try downloading as unauthorized user
        client.login(username='unauthorized', password='Pass789!')
        response = client.get(reverse('download_file', args=[file_obj.id]))

        # Verify access is denied for unauthorized user
        assert response.status_code == 302  # Redirect to file list with error message
