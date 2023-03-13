from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User
from data_set.models import ClassStudent, Teacher, ActiveClass, Subject, Class, Student


class SaveClass(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text="Class Name Field is required.")

    class Meta:
        model = Class
        fields = ('name',)

    def clean_name(self):
        id = self.instance.id if not self.instance == None else 0
        try:
            if id.isnumeric() and id > 0:
                name = Class.objects.exclude(id=id).get(name=self.cleaned_data['name'])
            else:
                name = Class.objects.get(name=self.cleaned_data['name'])
        except:
            return self.cleaned_data['name']
        raise forms.ValidationError(f'{name.name} Class Already Exists.')


class SaveSubject(forms.ModelForm):
    level = forms.Select(
        attrs={'class': 'form-control form-control-sm rounded-0', 'value': '', 'id': 'id_level'}
    )
    name = forms.CharField(max_length=250,help_text = "Subject Name Field is required.")

    class Meta:
        model= Subject
        fields = ('name', 'level')

    def clean_class(self):
        level = self.cleaned_data['level']
        try:
            lvl = Class.objects.get(id=level)
            return lvl
        except:
            raise forms.ValidationError(f'Class value is invalid.')


class SaveStudent(forms.ModelForm):
    first_name = forms.CharField(max_length=250, help_text="Name Field is required.")
    level = forms.Select(
        attrs={'class': 'form-control form-control-sm rounded-0', 'value': '', 'id': 'id_level'}
    )

    class Meta:
        model = Student
        fields = ('student_code', 'level', 'first_name', 'last_name', 'gender', 'dob', 'contact')

    def clean_student_code(self):
        code = self.cleaned_data['student_code']
        try:
            if not self.instance.id is None:
                student = Student.objects.exclude(id=self.instance.id).get(student_code=code)
            else:
                student = Student.objects.get(student_code=code)
        except:
            return code
        raise forms.ValidationError(f"Student Code {code} already exists.")


class SaveActiveClass(forms.ModelForm):
    assigned_teacher = forms.Select(
        attrs={'class': 'form-control form-control-sm rounded-0', 'value': '', 'id': 'id_assigned_teacher'}
    )
    assigned_class = forms.Select(
        attrs={'class': 'form-control form-control-sm rounded-0', 'value': '', 'id': 'id_assigned_class'}
    )
    assigned_subject = forms.Select(
        attrs={'class': 'form-control form-control-sm rounded-0', 'value': '', 'id': 'id_assigned_subject'}
    )
    year = forms.CharField(max_length=250,help_text = "Academic Year Field is required.")

    class Meta:
        model = ActiveClass
        fields = ('assigned_teacher', 'assigned_class', 'assigned_subject', 'year')

    def clean(self):
        cleaned_data = super().clean()
        assigned_class = cleaned_data.get('assigned_class')
        assigned_subject = cleaned_data.get('assigned_subject')
        assigned_teacher = cleaned_data.get('assigned_teacher')

        # Check that the combination of assigned_class, assigned_subject, and assigned_teacher is unique
        if assigned_class and assigned_subject and assigned_teacher:
            active_classes = ActiveClass.objects.filter(
                assigned_class=assigned_class,
                assigned_subject=assigned_subject,
                assigned_teacher=assigned_teacher
            )
            if self.instance:
                active_classes = active_classes.exclude(pk=self.instance.pk)
            if active_classes.exists():
                raise forms.ValidationError('This combination of assigned class, subject, and teacher is already assigned.')

        return cleaned_data


class SaveClassStudent(forms.ModelForm):
    classIns = forms.IntegerField()
    student = forms.IntegerField()

    class Meta:
        model = ClassStudent
        fields = ('classIns', 'student', 'mark', 'assigned_class', 'subject')

    def clean_classIns(self):
        cid = self.cleaned_data['classIns']
        try:
            classIns = ActiveClass.objects.get(id=cid)
            return classIns
        except:
            raise forms.ValidationError("Active Class ID is Invalid.")

    def clean_student(self):
        student_id = self.cleaned_data['student']
        _class = ActiveClass.objects.get(id=self.data.get('classIns'))
        student = Student.objects.get(id=student_id)
        try:
            cs = ClassStudent.objects.get(classIns=_class, student=student)
            if len(cs) > 0:
                raise forms.ValidationError(f"Student already exists in the Class List.")
        except:
            return student


class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text="The email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateTeacher(UserChangeForm):
    username = forms.CharField(max_length=250, help_text="The username field is required.")
    email = forms.EmailField(max_length=250, help_text="The email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(UpdateTeacher, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.user.id).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        print(self.user.id)
        try:
            user = User.objects.exclude(id=self.user.id).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(max_length=250, help_text="The Username field is required.")
    email = forms.EmailField(max_length=250, help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateProfileMeta(forms.ModelForm):
    dob = forms.DateField(help_text="The Birthday field is required.")
    contact = forms.CharField(max_length=250, help_text="The Contact field is required.")

    class Meta:
        model = Teacher
        fields = ('dob', 'contact', 'gender')


class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}),
        label="Confirm New Password")

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UpdateProfileAvatar(forms.ModelForm):
    avatar = forms.ImageField(help_text="The Avatar field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = Teacher
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs['instance']
        kwargs['instance'] = self.user.profile
        super(UpdateProfileAvatar, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        if not self.user.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError("Password is Incorrect")


class AddAvatar(forms.ModelForm):
    avatar = forms.ImageField(help_text="The Avatar field is required.")

    class Meta:
        model = Teacher
        fields = ('avatar',)