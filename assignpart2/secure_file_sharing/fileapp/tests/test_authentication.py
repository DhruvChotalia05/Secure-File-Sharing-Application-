"""
############################
#  File Name: test_authentication.py
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
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
class TestUserAuthentication:
    def test_successful_user_registration(self, client):
        """
        Test that a user can successfully register with valid credentials
        """
        registration_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        
        response = client.post(reverse('register'), registration_data)
        
        # Assert user is created and redirected to login
        assert response.status_code == 302
        assert User.objects.filter(username='testuser').exists()

    def test_invalid_registration(self, client):
        """
        Test registration with mismatched passwords
        """
        registration_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'DifferentPass456!'
        }
        
        response = client.post(reverse('register'), registration_data)
        
        # Assert registration fails
        assert response.status_code == 200
        assert not User.objects.filter(username='testuser').exists()

    def test_login_authentication(self, client):
        """
        Test user login with correct credentials
        """
        # Create a test user
        User.objects.create_user(username='loginuser', password='TestPass123!')
        
        login_data = {
            'username': 'loginuser',
            'password': 'TestPass123!'
        }
        
        response = client.post(reverse('login'), login_data)
        
        # Assert successful login and redirect
        assert response.status_code == 302

    def test_invalid_login(self, client):
        """
        Test login with incorrect credentials
        """
        login_data = {
            'username': 'nonexistentuser',
            'password': 'WrongPassword'
        }
        
        response = client.post(reverse('login'), login_data)
        
        # Assert login fails
        assert response.status_code == 200

    def test_logout(self, client, django_user_model):
        """
        Test user logout functionality
        """
        # Create and login a test user
        username = 'logoutuser'
        password = 'TestPass123!'
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)

        # Perform logout
        response = client.get(reverse('logout'))

        # Assert successful logout and redirection
        assert response.status_code == 302
        assert not client.session.get('_auth_user_id')