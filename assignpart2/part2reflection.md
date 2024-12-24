We, Dhruv Chotalia and MitKumarPatel(mention your names), declare that the attached Assignment is our own work in accordance with the Seneca Academic Policy. We have not copied any part of this Assignment, manually or electronically, from any other source, including websites, unless specified as references. We have not distributed our work to other students.

Importance of Testing

Q1) Why is testing critical for a secure file-sharing application, especially in the context of sensitive data? How does it enhance the application's reliability and security?

Ans)Testing is essential for a secure file-sharing application as it rigorously verifies security mechanisms to protect sensitive data, identifies vulnerabilities to prevent data breaches, ensures the seamless functionality of authentication, encryption, and access control, and validates the application's robustness in handling diverse user interactions and edge cases.
Key security enhancements include ensuring data integrity during file transfers, confirming the reliability of user authentication processes, validating encryption and decryption mechanisms, and maintaining proper access control and file-sharing permissions.

Q2) What advantages does automated testing offer over manual testing for this project?

Ans) Automated testing offers consistent and repeatable execution, enabling rapid validation across various scenarios and thorough coverage of edge cases. It delivers immediate feedback on code changes, minimizes human error, and supports continuous integration and deployment. Over time, it proves cost-effective for maintenance, facilitates comprehensive regression testing, and provides detailed error reporting and debugging insights.

Test Case Design

Q1) How did you determine which features and scenarios to prioritize in your unit tests? Which areas did you found most challenging to test?

Ans) Test case prioritization focuses on core authentication flows, including user registration, login/logout mechanisms, and password validation. It also emphasizes critical file operations such as uploading, downloading, encryption/decryption, and file sharing. 
The most challenging areas to test involve encryption and decryption processes, simulating complex user interactions, mocking external dependencies, addressing edge cases in file sharing, and ensuring thorough security coverage.

Q2) Describe how you balanced positive and negative test cases. Why is it important to test both valid and invalid scenarios (e.g., valid/invalid logins, authorized/unauthorized file access)?

Ans) A balanced testing approach includes positive test cases to ensure the system functions as expected, validates successful user interactions, and confirms proper system behavior. Negative test cases focus on assessing responses to invalid inputs, validating error handling, and identifying potential security vulnerabilities. This approach is crucial for uncovering security weaknesses, ensuring robust error handling, preventing unexpected behaviors, validating input mechanisms, and enhancing the application's overall resilience.

Testing for Security

Q1) How did you test for security-related issues, such as unauthorized access and data integrity? What specific tests did you implement to ensure that encryption and access control were functioning correctly?

Ans) Security testing strategies leverage Django-specific features such as built-in CSRF protection, an authentication system, and permission-based access control. Key tests include preventing unauthorized file access by ensuring users access only their files and verifying file sharing permissions. Encryption integrity is validated by checking file hash preservation and ensuring encryption/decryption work correctly. Authentication tests focus on invalid login attempts and password complexity, while file upload restrictions address malicious file types and size limits. Django mechanisms like @login_required decorators, user authentication backends, secure session management, clickjacking protection, and password hashing further reinforce application security.

Q2) How did your tests help identify any vulnerabilities or areas where your application might be susceptible to attacks, like SQL injection or XSS?

Ans) We conducted thorough testing to identify potential vulnerabilities or areas where our application might be susceptible to attacks, such as SQL injection or XSS. By implementing Django's user authentication system and testing it rigorously, we were able to verify that it effectively prevents unauthorized access and guards against common vulnerabilities. This helped us ensure that critical security mechanisms are functioning as intended and provided insights into areas that required additional attention or improvement.

Using Pytest or Other Testing Tools:

Q1) How did using pytest or another testing tool contribute to your testing process? What did you find useful or challenging about configuring pytest for this assignment?

Ans) Using pytest significantly contributed to our testing process by simplifying test writing, automating test discovery, and providing clear and concise assertions. We found its fixture management and mocking capabilities particularly useful for setting up and isolating dependencies during tests. Configuring pytest for this assignment was straightforward, but we did face some challenges, such as integrating database tests with @pytest.mark.django_db and ensuring compatibility with the Django testing framework. Despite these challenges, pytest's detailed error reporting and parameterized testing features made it easier to validate edge cases and verify application behavior thoroughly.

Q2) What insights did the pytest score provide about your code quality? If you did not reach the target score, what changes would you consider to improve it?

Ans)Pytest provides valuable insights by identifying code coverage gaps, highlighting potential opportunities for refactoring, verifying the implementation of security best practices, ensuring comprehensive feature testing, and offering metrics on test effectiveness. Improvement strategies include increasing test coverage, adding more edge case scenarios, implementing more granular testing, enhancing error handling tests, and validating complex interaction scenarios.

Reflection on Secure Coding and Testing Practices

Q1) What testing techniques or secure coding practices did you apply that helped protect the application from common vulnerabilities?

Ans) Secure coding practices involve thorough input validation, encrypting sensitive data, implementing strict access control, ensuring secure file handling, protecting against common web vulnerabilities, handling errors properly, and logging critical operations. In Django, key security features include its user authentication system, password hashing, CSRF protection, SQL injection prevention, and secure session management to strengthen application security.

Q2) How confident are you in the security and reliability of your application after completing these tests, and what future practices would you consider for more advanced testing?

Ans) We are confident in the security and reliability of our application, as we implemented multiple layers of security, such as Django's user authentication system, password hashing, CSRF protection, and input validation. We conducted comprehensive testing using pytest to verify the functionality and security of our application, which allowed us to identify and address potential vulnerabilities. While we are confident in the current state of security, we acknowledge that continuous monitoring, regular testing, and updates are essential to maintain and strengthen the application’s security and reliability over time.
