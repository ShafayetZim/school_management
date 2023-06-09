# school_management
<b>Project Installation in Django Python:</b>

1. Download python and install

2. Create Virtual Environment<br />
linux & mac os: python3 -m venv environment_name<br />
Windows: python -m venv environment_name
  
3. Activate Environment<br />
  #Linux & mac os<br />
  ->source environment_name/bin/activate<br />
  #Windows<br />
  ->environment_name\Scripts\activate
  
4. Install Django<br />
 #linux & mac os<br />
 ->pip3 install django<br />
 #Windows<br />
 ->pip install django
 
5. To Create superuser <br />
->python manage.py createsuperuser
	enter username, Email, password
	enter your password again
  
6. Migration & migrate:<br />
-> Windows: python manage.py makemigrations<br />
-> Linux: python3 manage.py makemigrations<br />
-> Windows: python manage.py migrate<br />
-> Linux: python3 manage.py migrate

7. Run development server: <br />
-> Windows: python manage.py runserver<br />
-> Linux: python3 manage.py runserver

8. Optional Databse Configuration:<br />
  If you want other database server find and replace the below code of 'DATABASE' to preojects settings.py file<br />
  DATABASES = {<br />
    'default': {<br />
        'ENGINE': 'django.db.backends.#databaseservername#',<br />
        'NAME': 'Your Database Name',<br />
        'USER' : 'Database User Name',<br />
        'PASSWORD' : 'Your Password',<br />
        'HOST' : "Write down Host",<br />
        'PORT' : 'Write down port',<br />
                
    }<br />
  }<br />
  
9. Users:<br />
<b>Existing Superuser:</b><br />
username: sms<br />
password: 123<br />

<b>Existing teacher:</b><br />
username: teacher1<br />
password: sms#2023<br />
username: teacher2<br />
password: sms#2023<br />


<b>User Manual: School Management System</b>

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
   
6. Assign class
   After adding all setup data, then click "Assign-Class."
   Fill in the required information, such as CLass, Subject, Teacher and academic year. Here you can see all assigned class and view all student assigned to it.    

7. Teacher Dashboard
   The teacher dashboard is where the teacher user can manage the data that are assigned to them. From this dashboard, the teacher can:

   Add or delete marks to students of their class
   Print the Class Report, which shows the students' academic performance
   View the Class Performance Report, which shows the class's overall academic performance
   
   When adding marks to students system automatically providing the necessary input. 
   Once you have added marks to student of a subject, they will be removed from the list of students who need to be assigned marks.
   This will help you keep track of which students still need to be graded.

8. GPA Grading
   When the teacher adds marks to a student, the system automatically converts the marks to GPA grading. The grading system follows a standard scale of 5.0
   ![image](https://user-images.githubusercontent.com/43902599/224626999-82c12bbf-26bd-4e85-8ec5-24ce05c002b1.png)



9. Search Results
   From the "Search-Result" menu, any user can view their academic performance by selecting their name, class, or roll number.

10. Dashboard Filters
   On the dashboard, there are two dropdown menus: one for the class and one for the subject. 
   If you select "all" from the subject dropdown, the system will aggregate the results and display them.
  ![image](https://user-images.githubusercontent.com/43902599/224623739-d4707ad9-42b2-486e-810f-9405768c8b8b.png)


11. Logout
   To logout from the system, click on the "Logout" button located at the top right corner of the screen.
