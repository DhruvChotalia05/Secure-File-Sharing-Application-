"""
############################
#  File Name: test_file_operations.py
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
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from fileapp.models import File
from fileapp.utils import FileEncryptor


@pytest.mark.django_db
class TestFileOperations:

    @patch('fileapp.utils.FileEncryptor.encrypt_file')
    def test_file_upload(self, mock_encrypt_file, client, django_user_model):
        """
        Test successful file upload for authenticated user.
        Verifies that a file can be uploaded, encrypted, and saved.
        """
        # Create and login test user
        username = 'uploaduser'
        password = 'TestPass123!'
        user = django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)

        # Prepare a test file
        test_file = SimpleUploadedFile(
            name='test_file.txt', 
            content=b'Test file content', 
            content_type='text/plain'
        )

        # Mock encryption process
        mock_encrypt_file.return_value = 'mockedhash'

        # Upload the file
        response = client.post(reverse('upload_file'), {'files': test_file})
        
        # Verify the file was uploaded and saved
        assert response.status_code == 302
        assert File.objects.filter(user=user).exists()

        # Check the file hash (encryption)
        uploaded_file = File.objects.get(user=user)
        assert uploaded_file.file_hash == 'mockedhash'

    def test_unsupported_file_upload(self, client, django_user_model):
        """
        Test upload of unsupported file type.
        Verifies that unsupported file types are not allowed.
        """
        # Create and login test user
        username = 'unsupporteduser'
        password = 'TestPass123!'
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)

        # Prepare an unsupported file type
        unsupported_file = SimpleUploadedFile(
            name='test.exe', 
            content=b'Executable content', 
            content_type='application/x-msdownload'
        )

        # Attempt to upload unsupported file
        response = client.post(reverse('upload_file'), {'files': unsupported_file})
        
        # Verify upload is prevented
        assert response.status_code == 302
        assert not File.objects.filter(filename='test.exe').exists()

    @patch('fileapp.utils.FileEncryptor.decrypt_file')
    def test_file_download(self, mock_decrypt_file, client, django_user_model):
        """
        Test file download for file owner.
        Verifies that the file owner can download a file after decryption.
        """
        # Create and login test user
        username = 'downloaduser'
        password = 'TestPass123!'
        user = django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)

        # Create a test file
        test_file = SimpleUploadedFile(
            name='download_test.txt', 
            content=b'Download test content', 
            content_type='text/plain'
        )
        file_obj = File.objects.create(
            user=user, 
            filename='download_test.txt', 
            file=test_file,
            file_hash='mockedhash'
        )

        # Mock decryption
        mock_decrypt_file.return_value = ('/tmp/decrypted_file', 'mockedhash')

        # Attempt to download the file
        response = client.get(reverse('download_file', args=[file_obj.id]), follow=True)
        
        # Verify successful download
        assert response.status_code == 200

    def test_delete_file(self, client, django_user_model):
        """
        Test file deletion functionality.
        Verifies that the file owner can delete their file.
        """
        # Create and login test user
        username = 'deleteuser'
        password = 'TestPass123!'
        user = django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)

        # Create a test file
        test_file = SimpleUploadedFile(
            name='delete_test.txt', 
            content=b'Delete test content', 
            content_type='text/plain'
        )
        file_obj = File.objects.create(
            user=user, 
            filename='delete_test.txt', 
            file=test_file,
            file_hash='mockedhash'
        )

        # Attempt to delete the file
        response = client.post(reverse('delete_file', args=[file_obj.id]))
        
        # Verify successful deletion
        assert response.status_code == 302
        assert not File.objects.filter(id=file_obj.id).exists()
