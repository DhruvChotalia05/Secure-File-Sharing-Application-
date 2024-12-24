# Reflection
Study your assignment part1 solution, reread the related part of the course notes, and ensure you have understood the concepts covered by this assignment. Write your answer here to the assignment questions (Check the assignment instructions)

We, Dhruv Chotalia and MitKumarPatel(mention your names), declare that the attached Assignment is our own work in accordance with the Seneca Academic Policy. We have not copied any part of this Assignment, manually or electronically, from any other source, including websites, unless specified as references. We have not distributed our work to other students.

Understanding Requirements:

Q1)How did you interpret the requirements for this assignment, and were there any points where clarification was needed? How did you address any uncertainties?

A1)The assignment required creating a secure file-sharing application with functionalities like user authentication, file upload, encryption, and sharing. We began by breaking these requirements into smaller, manageable tasks:

1) Setting up user registration and authentication using Django’s built-in tools.
2) Implementing secure file upload and download mechanisms.
3) Incorporating encryption to safeguard files.
4) Enabling file sharing with proper access control for authorized users only.

This modular approach helped me address each aspect systematically.


Some areas needed clarification,

1) We researched popular encryption methods and chose AES (Advanced Encryption Standard) due to its reliability and security.
2) We implemented file type validation using Django’s FileExtensionValidator to restrict uploads to specific file formats.

Design Choices:

Q2)What considerations influenced your choice of Django for developing this application? Were there any alternatives you considered, and why did you ultimately choose Django?

A2)Django was the framework of choice because of its built-in tools that aligned perfectly with the assignment’s needs:

1) Authentication: Django provides a robust, built-in user authentication system, saving time and effort.
2) Security: Django’s middleware protects against common vulnerabilities like SQL injection, CSRF, and XSS.
3) ORM: The ORM simplifies database management, allowing for seamless queries without writing raw SQL.

We briefly considered Flask, but its lack of built-in features for authentication and security would have required additional setup, making Django the more efficient choice.

Q3)How did you structure your application’s components (e.g., user authentication, file upload, encryption) to ensure scalability and ease of maintenance?

A3)Application Structure:

1) User Authentication: Used Django’s User model for registration and login. Redirects and feedback messages improved the user experience.
2) File Upload: File uploads were managed through the FileField in a dedicated File model. Encryption was applied when files were uploaded.
3) File Sharing: Sharing was implemented using a FileShare model, linking specific files to authorized users.
4) Scalability and Maintenance: Each feature was modularized:
Encryption and file handling were handled by utility functions.
Access control checks were abstracted into reusable methods

Encryption and Security

Q4) Why is encryption critical in this file-sharing application? How did you implement encryption, and what challenges did you encounter?

A4) Importance of Encryption:
Encryption is essential to protect sensitive data in storage or transit. Without encryption, unauthorized users gaining access to the server could view or misuse stored files. AES encryption ensures confidentiality and integrity.

Implementation:
How It Was Done: AES encryption was applied when files were uploaded, with decryption occurring during downloads. Keys were managed securely, and file hashes verified integrity.
Challenges:
Managing large file encryption required optimizing memory usage.
Debugging decryption failures due to mismatched keys or corrupted data took additional effort.

Q5)How does your application control access to files, and what measures prevent unauthorized access to sensitive information?

A5)Access Control:

1) Only the file owner or authorized users (via the FileShare model) could access shared files.
2) Strict checks, such as if request.user == file_instance.owner, ensured no unauthorized access.

Code Modularity and Organization

Q6) How did you ensure that your code is modular and organized? What are the benefits of this approach for future development or when adding new features?

A6) Ensuring Modularity:

The application was split into logical components:
1) Models (File, FileShare) for database operations.
2) Views for handling user requests.
3) Utility functions for encryption and decryption tasks.
4) Templates were kept minimal and focused on rendering content.

Benefits:

1) Ease of Maintenance: Adding features like file versioning or additional encryption algorithms would be straightforward.
2) Code Reusability: Functions like encryption/decryption and error handling can be repurposed for other projects.

Q7) Which parts of the code do you consider most reusable, and why?

A7) Modular models and access control methods are adaptable for other applications requiring user-based permissions. Also all the css html files.

Error Handling:

Q8) What error-handling strategies did you incorporate to improve the user experience? How did you handle cases like incorrect passwords, unauthorized access, or unsupported file types?

A8) Strategies Incorporated:

Used try-except blocks to catch exceptions during encryption, decryption, and file uploads.
Validated user inputs at multiple levels (e.g., form validation, model constraints).
Django’s messaging framework provided clear feedback for errors like unsupported file types or incorrect passwords.

Examples:

Incorrect Passwords: During registration, errors like mismatched passwords were displayed inline, guiding users to resolve issues.
Unauthorized Access: Redirected unauthorized users with error messages.
Unsupported File Types: File uploads were restricted to allowed types with clear error messages for invalid attempts.

Reflecting on Secure Coding Practices

Q9) What secure coding practices did you apply, and how do they protect against common vulnerabilities such as SQL injection and XSS?

A9) Practices Applied:

SQL Injection Prevention: Used Django ORM to build queries safely.
XSS Protection: Sanitized inputs, and Django automatically escapes outputs in templates.
CSRF Protection: Django’s CSRF middleware ensured safe form submissions.
Encryption: Files were securely encrypted and decrypted using AES.

Q10) How would you rate the security of your application, and what improvements could you make if given more time?

A10) Security Rating:
The application is secure against common vulnerabilities but could be enhanced with:

Two-factor authentication for added login security.
Logging and monitoring unusual access patterns.
Rate-limiting login attempts to prevent brute-force attacks.

GitHub Codespace Utilization

Q11) How did working in GitHub Codespace support your development process? Were there any limitations or advantages compared to local development?

A11) Advantages:

Consistency: The pre-configured environment eliminated issues caused by dependency mismatches.
Accessibility: Enabled seamless development from any machine with an internet connection.
Integration: Simplified version control and collaboration with GitHub.
Limitations:

Performance: Codespace performance was sometimes slower compared to local setups.
Customization: Certain advanced configurations (e.g., database tuning) were more challenging in the cloud.



Name	          Task(s)
1.Mitkumar Patel  setting.py and views.py and report , reflection 
2.Dhruv Chotalia  All html and CSS ,forms.py and forms.py and report, relflection

