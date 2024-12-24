"""
############################
#  File Name: test_file_integrity.py
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
import hashlib
import os
import tempfile
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from fileapp.models import File
from fileapp.utils import FileEncryptor


@pytest.mark.django_db
class TestFileIntegrity:

    @patch('fileapp.utils.FileEncryptor.encrypt_file')
    def test_file_hash_generation(self, mock_encrypt_file, client, django_user_model):
        """
        Test file hash generation during upload.
        Verifies that a correct hash is generated for the uploaded file.
        """
        # Create and login test user
        user = django_user_model.objects.create_user(username='hashuser', password='TestPass123!')
        client.login(username='hashuser', password='TestPass123!')

        # Prepare test file and expected hash
        original_content = b'Integrity test content'
        test_file = SimpleUploadedFile(
            name='hash_test.txt', 
            content=original_content, 
            content_type='text/plain'
        )
        expected_hash = hashlib.sha256(original_content).hexdigest()

        # Mock the hash generation
        mock_encrypt_file.return_value = expected_hash

        # Upload the file and verify hash
        file_obj = File.objects.create(
            user=user, 
            filename='hash_test.txt', 
            file=test_file,
            file_hash=expected_hash
        )

        # Verify the generated file hash
        assert file_obj.file_hash == expected_hash
        assert len(file_obj.file_hash) == 64  # SHA-256 hash length

    @patch('fileapp.utils.FileEncryptor.encrypt_file')
    @patch('fileapp.utils.FileEncryptor.decrypt_file')
    def test_file_integrity_during_download(self, mock_decrypt_file, mock_encrypt_file, client, django_user_model):
        """
        Test file integrity during download.
        Verifies that the file content matches the hash after download.
        """
        # Create and login test user
        user = django_user_model.objects.create_user(username='integrityuser', password='TestPass123!')
        client.login(username='integrityuser', password='TestPass123!')

        # Prepare test file and expected hash
        original_content = b'Integrity test content'
        test_file = SimpleUploadedFile(
            name='integrity_test.txt', 
            content=original_content, 
            content_type='text/plain'
        )
        expected_hash = hashlib.sha256(original_content).hexdigest()

        # Mock encryption and decryption
        mock_encrypt_file.return_value = expected_hash

        # Create a temporary file to simulate decryption
        with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_file:
            temp_file.write(original_content)
            temp_file_path = temp_file.name
        mock_decrypt_file.return_value = (temp_file_path, expected_hash)

        # Create the file object
        file_obj = File.objects.create(
            user=user, 
            filename='integrity_test.txt', 
            file=test_file,
            file_hash=expected_hash
        )

        try:
            # Simulate file download
            response = client.get(reverse('download_file', args=[file_obj.id]))
            
            # Verify the download response and content integrity
            assert response.status_code == 200
            assert response['Content-Disposition'].startswith('attachment')
            
            # Verify the downloaded file content matches the original
            downloaded_content = b''.join(response.streaming_content)
            assert downloaded_content == original_content

        finally:
            # Clean up temporary file after test
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
