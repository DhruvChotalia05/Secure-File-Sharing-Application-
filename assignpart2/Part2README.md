"""
############################
#  File Name: Part2README.md
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


Setup

Software Requirements
Python 3.8+ Django 3.2+ pip package manager

Required Dependencies

1. Django
2. python-dotenv
3. cryptography
4. pytest-django
5. pytest-cov

Installation Dependencies
Run the following command to install dependencies:
pip install django cryptography python-dotenv pytest-django pytest-cov


To generate test Report 
1. Go to file app directory
2. Run the following command 
   pytest --cov=fileapp tests/

After running the tests with the above command, pytest will generate a report in the terminal, showing the status of each test and the overall coverage for the fileapp directory.