# school_management
Project Installation in Django Python:

1. Download python and install

2. Create Virtual Environment
 
  linux & mac os
  python3 -m venv environment_name
  Windows
  python -m venv environment_name
  
  >>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
  
3. >>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
4. >>>To Create superuser 
->python manage.py createsuperuser
	enter username, Email, password
	enter your password again
  
5. Migration & migrate:
-> Windows: python manage.py makemigrations
-> Linux: python3 manage.py makemigrations
-> Windows: python manage.py migrate
-> Linux: python3 manage.py migrate

6. Run development server:
-> Windows: python manage.py runserver
-> Linux: python3 manage.py runserver

7. Optional Databse Configuration:
  If you want other database server find and replace the below code of 'DATABASE' to preojects settings.py file
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'Your Database Name',
        'USER' : 'Database User Name',
        'PASSWORD' : 'Your Password',
        'HOST' : "Write down Host",
        'PORT' : 'Write down port',
                
    }
  }


User Manual: School Management System

1. Introduction
   The School Management System is an online application designed for school administrators and teachers to manage students' records, classes, and academic performance. This system is accessible through a web browser, and the user must have an internet connection to access it. The system has two user roles: the Administrator or the Super User, and the Teacher User.

2. Logging In
   To log in to the system, go to the login page and enter your username and password. If you are an admin, you will be redirected to the admin dashboard. If you are a teacher, you will be redirected to the teacher dashboard.

3. Administrator Dashboard
   The administrator dashboard is where the admin user can access and manage all the features and functionalities of the system. From this dashboard, the admin can:

   Add, edit, or delete classes
   Add, edit, or delete subjects
   Add, edit, or delete students
   Add, edit, or delete teachers
   Assign classes to teachers
   Assign subjects to classes
   View reports on student performance
   Generate reports on school performance
   
4. Adding a Student
   To add a student, go to the "Students" menu in the admin dashboard, then click "Add Student." 
   Fill in the required information, such as name, date of birth, and gender. 
   Select the class that the student will be enrolled in, and the system will automatically assign all subjects associated with that class.

5. Adding a Teacher
   To add a teacher, go to the "Teachers" menu in the admin dashboard, then click "Add Teacher."
   Fill in the required information, such as name, email, and phone number. Assign the teacher to a class, and the teacher will be able to access the class's data.

6. Teacher Dashboard
   The teacher dashboard is where the teacher user can manage the data that are assigned to them. From this dashboard, the teacher can:

   Add or delete marks to students of their class
   Print the Class Report, which shows the students' academic performance
   View the Class Performance Report, which shows the class's overall academic performance
   
   When adding marks to students system automatically providing the necessary input. 
   Once you have added marks to student of a subject, they will be removed from the list of students who need to be assigned marks.
   This will help you keep track of which students still need to be graded.

7. GPA Grading
   When the teacher adds marks to a student, the system automatically converts the marks to GPA grading. The grading system follows a standard scale of 5.0

8. Search Results
   From the "Search-Result" menu, any user can view their academic performance by selecting their name, class, or roll number.

9. Dashboard Filters
   On the dashboard, there are two dropdown menus: one for the class and one for the subject. 
   If you select "all" from the subject dropdown, the system will aggregate the results and display them.
  ![image](https://user-images.githubusercontent.com/43902599/224623739-d4707ad9-42b2-486e-810f-9405768c8b8b.png)


10. Logout
   To logout from the system, click on the "Logout" button located at the top right corner of the screen.
