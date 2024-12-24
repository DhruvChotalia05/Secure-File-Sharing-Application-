"""
############################
#  File Name: test_utils.py
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
import os
import pytest
import tempfile
import hashlib
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from fileapp.utils import FileEncryptor 

# Fixture to create and manage a temporary .env file for testing
@pytest.fixture
def temp_env_file():
    """Create a temporary .env file for testing"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.env') as temp_env:
        temp_env_path = temp_env.name
    
    # Store the current environment variable state
    original_env = os.getenv('FERNET_KEY')
    
    # Set the temporary .env file path for testing
    os.environ['ENV_FILE'] = temp_env_path
    
    yield temp_env_path  # Provide the temp env file path for the test
    
    # Clean up after the test
    os.unlink(temp_env_path)
    if original_env:
        os.environ['FERNET_KEY'] = original_env
    else:
        os.environ.pop('FERNET_KEY', None)
    os.environ.pop('ENV_FILE', None)

# Fixture to create a sample file for testing encryption and decryption
@pytest.fixture
def sample_file():
    """Create a sample file for testing"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        test_content = b"This is a test file for encryption and decryption."
        temp_file.write(test_content.decode())
        temp_file_path = temp_file.name
    
    yield temp_file_path  # Provide the sample file path for the test
    
    # Clean up after the test
    os.unlink(temp_file_path)



# Test the key generation functionality
def test_generate_key():
    """Test key generation method"""
    key = FileEncryptor.generate_key()
    
    # Verify key is valid and saved to the .env file
    assert key is not None
    assert isinstance(key, bytes)
    
    load_dotenv()  # Load environment variables
    saved_key = os.getenv(FileEncryptor.ENV_KEY_NAME)
    assert saved_key is not None

# Test the full file encryption and decryption process
def test_encrypt_decrypt_file(sample_file):
    """Test encryption and decryption cycle"""
    # Read the original file content and generate its hash
    with open(sample_file, 'rb') as f:
        original_content = f.read()
        original_hash = hashlib.sha256(original_content).hexdigest()
    
    # Encrypt the file and verify the content is changed
    file_hash = FileEncryptor.encrypt_file(sample_file)
    with open(sample_file, 'rb') as f:
        encrypted_content = f.read()
    
    assert encrypted_content != original_content  # Ensure encryption altered the content
    assert file_hash == original_hash  # Verify the file hash consistency
    
    # Decrypt the file and verify the content matches the original
    decrypted_path, decrypted_hash = FileEncryptor.decrypt_file(sample_file)
    with open(decrypted_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == original_content  # Ensure decryption restored the original content
    assert decrypted_hash == original_hash  # Ensure the hashes match
    
    # Clean up temporary decrypted file
    os.unlink(decrypted_path)
