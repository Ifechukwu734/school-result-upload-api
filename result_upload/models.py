from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission 
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager
import uuid
# Create your models here.



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True)
    phone_number = models.CharField(max_length=20, default='')
    first_name = models.CharField(max_length=200, )
    last_name = models.CharField(max_length=200, )
    department = models.CharField(max_length=200, default='')
    level = models.CharField(default='100', max_length=3)
    matric_number = models.CharField(default='', max_length=20)
    profile_image = models.ImageField(upload_to='image/', null=True, default='', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_set', blank=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.matric_number:
            number = str(uuid.uuid4().int)[:4]
            self.matric_number = '2022/SC/' + number
        super().save(*args, **kwargs)
    



class ComputerScience100Level(models.Model):
    SEMESTER = (
        ('First semester', 'First semester'),
        ('Second semester', 'Second semester')
    )
    SESSION = (
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026')
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225, default='')
    last_name = models.CharField(max_length=225, default='')
    semester = models.CharField(choices=SEMESTER, default='', max_length=100)
    session = models.CharField(max_length=9, choices=SESSION, default='')
    level = models.CharField(max_length=3, default='100')
    course_code_1 = models.CharField(max_length=50, default='nil')
    course_title_1 = models.CharField(max_length=200, default='nil')
    course_1_credit_load = models.IntegerField(default=0)
    attendance_score_1 = models.IntegerField(default=0)
    inception_quiz_score_1 = models.IntegerField(default=0)
    midsemester_test_score_1 = models.IntegerField(default=0)
    exam_score_1 = models.IntegerField(default=0)
    total_score_1 = models.IntegerField(default=0)
    grade_1 = models.CharField(max_length=3, default='nil') 
    course_code_2 = models.CharField(max_length=50, default='nil')
    course_title_2 = models.CharField(max_length=200, default='nil')
    course_2_credit_load = models.IntegerField(default=0)
    attendance_score_2 = models.IntegerField(default=0)
    inception_quiz_score_2 = models.IntegerField(default=0)
    midsemester_test_score_2 = models.IntegerField(default=0)
    exam_score_2 = models.IntegerField(default=0)
    total_score_2 = models.IntegerField(default=0)
    grade_2 = models.CharField(max_length=3, default='nil')
    course_code_3 = models.CharField(max_length=50, default='nil')
    course_title_3 = models.CharField(max_length=200, default='nil')
    course_3_credit_load = models.IntegerField(default=0)
    attendance_score_3 = models.IntegerField(default=0)
    inception_quiz_score_3 = models.IntegerField(default=0)
    midsemester_test_score_3 = models.IntegerField(default=0)
    exam_score_3 = models.IntegerField(default=0)
    total_score_3 = models.IntegerField(default=0)
    grade_3 = models.CharField(max_length=3, default='nil') 
    course_code_4 = models.CharField(max_length=50, default='nil')
    course_title_4 = models.CharField(max_length=200, default='nil')
    course_4_credit_load = models.IntegerField(default=0)
    attendance_score_4 = models.IntegerField(default=0)
    inception_quiz_score_4 = models.IntegerField(default=0)
    midsemester_test_score_4 = models.IntegerField(default=0)
    exam_score_4 = models.IntegerField(default=0)
    total_score_4 = models.IntegerField(default=0)
    grade_4 = models.CharField(max_length=3, default='nil')
    course_code_5 = models.CharField(max_length=50, default='nil')
    course_title_5 = models.CharField(max_length=200, default='nil')
    course_5_credit_load = models.IntegerField(default=0)
    attendance_score_5 = models.IntegerField(default=0)
    inception_quiz_score_5 = models.IntegerField(default=0)
    midsemester_test_score_5 = models.IntegerField(default=0)
    exam_score_5 = models.IntegerField(default=0)
    total_score_5 = models.IntegerField(default=0)
    grade_5 = models.CharField(max_length=3, default='nil')
    course_code_6 = models.CharField(max_length=50, default='nil')
    course_title_6 = models.CharField(max_length=200, default='nil')
    course_6_credit_load = models.IntegerField(default=0)
    attendance_score_6 = models.IntegerField(default=0)
    inception_quiz_score_6 = models.IntegerField(default=0)
    midsemester_test_score_6 = models.IntegerField(default=0)
    exam_score_6 = models.IntegerField(default=0)
    total_score_6 = models.IntegerField(default=0)
    grade_6 = models.CharField(max_length=3, default='nil')
    course_code_7 = models.CharField(max_length=50, default='nil')
    course_title_7 = models.CharField(max_length=200, default='nil')
    course_7_credit_load = models.IntegerField(default=0)
    attendance_score_7 = models.IntegerField(default=0)
    inception_quiz_score_7 = models.IntegerField(default=0)
    midsemester_test_score_7 = models.IntegerField(default=0)
    exam_score_7 = models.IntegerField(default=0)
    total_score_7 = models.IntegerField(default=0)
    grade_7 = models.CharField(max_length=3, default='nil')
    course_code_8 = models.CharField(max_length=50, default='nil')
    course_title_8 = models.CharField(max_length=200, default='nil')
    course_8_credit_load = models.IntegerField(default=0)
    attendance_score_8 = models.IntegerField(default=0)
    inception_quiz_score_8 = models.IntegerField(default=0)
    midsemester_test_score_8 = models.IntegerField(default=0)
    exam_score_8 = models.IntegerField(default=0)
    total_score_8 = models.IntegerField(default=0)
    grade_8 = models.CharField(max_length=3, default='nil')
    course_code_9 = models.CharField(max_length=50, default='nil')
    course_title_9 = models.CharField(max_length=200, default='nil')
    course_9_credit_load = models.IntegerField(default=0)
    attendance_score_9 = models.IntegerField(default=0)
    inception_quiz_score_9 = models.IntegerField(default=0)
    midsemester_test_score_9 = models.IntegerField(default=0)
    exam_score_9 = models.IntegerField(default=0)
    total_score_9 = models.IntegerField(default=0)
    grade_9 = models.CharField(max_length=3, default='nil')
    course_code_10 = models.CharField(max_length=50, default='nil')
    course_title_10 = models.CharField(max_length=200, default='nil')
    course_10_credit_load = models.IntegerField(default=0)
    attendance_score_10 = models.IntegerField(default=0)
    inception_quiz_score_10 = models.IntegerField(default=0)
    midsemester_test_score_10 = models.IntegerField(default=0)
    exam_score_10 = models.IntegerField(default=0)
    total_score_10 = models.IntegerField(default=0)
    grade_10 = models.CharField(max_length=3, default='nil')
    course_code_11 = models.CharField(max_length=50, default='nil')
    course_title_11 = models.CharField(max_length=200, default='nil')
    course_11_credit_load = models.IntegerField(default=0)
    attendance_score_11 = models.IntegerField(default=0)
    inception_quiz_score_11 = models.IntegerField(default=0)
    midsemester_test_score_11 = models.IntegerField(default=0)
    exam_score_11 = models.IntegerField(default=0)
    total_score_11 = models.IntegerField(default=0)
    grade_11 = models.CharField(max_length=3, default='nil')
    course_code_12 = models.CharField(max_length=50, default='nil')
    course_title_12 = models.CharField(max_length=200, default='nil')
    course_12_credit_load = models.IntegerField(default=0)
    attendance_score_12 = models.IntegerField(default=0)
    inception_quiz_score_12 = models.IntegerField(default=0)
    midsemester_test_score_12 = models.IntegerField(default=0)
    exam_score_12 = models.IntegerField(default=0)
    total_score_12 = models.IntegerField(default=0)
    grade_12 = models.CharField(max_length=3, default='nil')
    course_code_13 = models.CharField(max_length=50, default='nil')
    course_title_13 = models.CharField(max_length=200, default='nil')
    course_13_credit_load = models.IntegerField(default=0)
    attendance_score_13 = models.IntegerField(default=0)
    inception_quiz_score_13 = models.IntegerField(default=0)
    midsemester_test_score_13 = models.IntegerField(default=0)
    exam_score_13 = models.IntegerField(default=0)
    total_score_13 = models.IntegerField(default=0)
    grade_13 = models.CharField(max_length=3, default='nil')
    gpa = models.DecimalField(default=0, max_digits=10, decimal_places=1)
    average_score = models.DecimalField(default=0, max_digits=10, decimal_places=1)


    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.total_score_1 = self.attendance_score_1 + self.inception_quiz_score_1 + self.midsemester_test_score_1 + self.exam_score_1
        self.total_score_2 = self.attendance_score_2 + self.inception_quiz_score_2 + self.midsemester_test_score_2 + self.exam_score_2
        self.total_score_3 = self.attendance_score_3 + self.inception_quiz_score_3 + self.midsemester_test_score_3 + self.exam_score_3
        self.total_score_4 = self.attendance_score_4 + self.inception_quiz_score_4 + self.midsemester_test_score_4 + self.exam_score_4
        self.total_score_5 = self.attendance_score_5 + self.inception_quiz_score_5 + self.midsemester_test_score_5 + self.exam_score_5
        self.total_score_6 = self.attendance_score_6 + self.inception_quiz_score_6 + self.midsemester_test_score_6 + self.exam_score_6
        self.total_score_7 = self.attendance_score_7 + self.inception_quiz_score_7 + self.midsemester_test_score_7 + self.exam_score_7
        self.total_score_8 = self.attendance_score_8 + self.inception_quiz_score_8 + self.midsemester_test_score_8 + self.exam_score_8
        self.total_score_9 = self.attendance_score_9 + self.inception_quiz_score_9 + self.midsemester_test_score_9 + self.exam_score_9
        self.total_score_10 = self.attendance_score_10 + self.inception_quiz_score_10 + self.midsemester_test_score_10 + self.exam_score_10
        self.total_score_11 = self.attendance_score_11 + self.inception_quiz_score_11 + self.midsemester_test_score_11 + self.exam_score_11
        self.total_score_12 = self.attendance_score_12 + self.inception_quiz_score_12 + self.midsemester_test_score_12 + self.exam_score_12
        self.total_score_13 = self.attendance_score_13 + self.inception_quiz_score_13 + self.midsemester_test_score_13 + self.exam_score_13

        
        if self.course_code_1 != 'nil':
            self.average_score = self.total_score_1/1
        if self.course_code_2 != 'nil':
            self.average_score = self.total_score_2 + self.total_score_1 / 2
        if self.course_code_3 != 'nil':
            self.average_score = self.total_score_3 + self.total_score_2 + self.total_score_3 / 3
        if self.course_code_4 != 'nil':
            self.average_score = self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 4
        if self.course_code_5 != 'nil':
            self.average_score = self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 5
        if self.course_code_6 != 'nil':
            self.average_score = self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 6
        if self.course_code_7 != 'nil':
            self.average_score = self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 7
        if self.course_code_8 != 'nil':
            self.average_score = self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 8
        if self.course_code_9 != 'nil':
            self.average_score = self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 9
        if self.course_code_10 != 'nil':
            self.average_score = self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 10
        if self.course_code_11 != 'nil':
            self.average_score = self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 11
        if self.course_code_12 != 'nil':
            self.average_score = self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 12
        if self.course_code_13 != 'nil':
            self.average_score = self.total_score_13 + self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 13
        


        load_1 = 0
        if self.total_score_1 >= 70 and self.total_score_1 <= 100:
            self.grade_1 = 'A'
            load_1 += 5 * self.course_1_credit_load
        elif self.total_score_1 >= 60 and self.total_score_1 <= 69:
            self.grade_1 = 'B'
            load_1 += 4 * self.course_1_credit_load
        elif self.total_score_1 >= 50 and self.total_score_1 <= 59:
            self.grade_1 = 'C'
            load_1 += 3 * self.course_1_credit_load
        elif self.total_score_1 >= 45 and self.total_score_1 <= 49:
            self.grade_1 = 'D'
            load_1 += 2 * self.course_1_credit_load
        elif self.total_score_1 >= 44 and self.total_score_1 <= 40:
            self.grade_1 = 'E'
            load_1 += 1 * self.course_1_credit_load
        else:
            self.grade_1 = 'F'
            load_1 += 0 * self.course_1_credit_load


        load_2 = 0
        if self.total_score_2 >= 70 and self.total_score_2 <= 100:
            self.grade_2 = 'A'
            load_2 += 5 * self.course_2_credit_load
        elif self.total_score_2 >= 60 and self.total_score_2 <= 69:
            self.grade_2 = 'B'
            load_2 += 4 * self.course_2_credit_load
        elif self.total_score_2 >= 50 and self.total_score_2 <= 59:
            self.grade_2 = 'C'
            load_2 += 3 * self.course_2_credit_load
        elif self.total_score_2 >= 45 and self.total_score_2 <= 49:
            self.grade_2 = 'D'
            load_2 += 2 * self.course_2_credit_load
        elif self.total_score_2 >= 44 and self.total_score_2 <= 40:
            self.grade_2 = 'E'
            load_2 += 1 * self.course_2_credit_load
        else:
            self.grade_2 = 'F'
            load_2 += 0 * self.course_2_credit_load

        
        load_3 = 0
        if self.total_score_3 >= 70 and self.total_score_3 <= 100:
            self.grade_3 = 'A'
            load_3 += 5 * self.course_3_credit_load
        elif self.total_score_3 >= 60 and self.total_score_3 <= 69:
            self.grade_3 = 'B'
            load_3 += 4 * self.course_3_credit_load
        elif self.total_score_3 >= 50 and self.total_score_3 <= 59:
            self.grade_3 = 'C'
            load_3 += 3 * self.course_3_credit_load
        elif self.total_score_3 >= 45 and self.total_score_3 <= 49:
            self.grade_3 = 'D'
            load_3 += 2 * self.course_3_credit_load
        elif self.total_score_3 >= 44 and self.total_score_3 <= 40:
            self.grade_3 = 'E'
            load_3 += 1 * self.course_3_credit_load
        else:
            self.grade_3 = 'F'
            load_3 += 0 * self.course_3_credit_load


        load_4 = 0
        if self.total_score_4 >= 70 and self.total_score_4 <= 100:
            self.grade_4 = 'A'
            load_4 += 5 * self.course_4_credit_load
        elif self.total_score_4 >= 60 and self.total_score_4 <= 69:
            self.grade_4 = 'B'
            load_4 += 4 * self.course_4_credit_load
        elif self.total_score_4 >= 50 and self.total_score_4 <= 59:
            self.grade_4 = 'C'
            load_4 += 3 * self.course_4_credit_load
        elif self.total_score_4 >= 45 and self.total_score_4 <= 49:
            self.grade_4 = 'D'
            load_4 += 2 * self.course_4_credit_load
        elif self.total_score_4 >= 44 and self.total_score_4 <= 40:
            self.grade_4 = 'E'
            load_4 += 1 * self.course_4_credit_load
        else:
            self.grade_4 = 'F'
            load_4 += 0 * self.course_4_credit_load


        load_5 = 0
        if self.total_score_5 >= 70 and self.total_score_5 <= 100:
            self.grade_5 = 'A'
            load_5 += 5 * self.course_5_credit_load
        elif self.total_score_5 >= 60 and self.total_score_5 <= 69:
            self.grade_5 = 'B'
            load_5 += 4 * self.course_5_credit_load
        elif self.total_score_5 >= 50 and self.total_score_5 <= 59:
            self.grade_5 = 'C'
            load_5 += 3 * self.course_5_credit_load
        elif self.total_score_5 >= 45 and self.total_score_5 <= 49:
            self.grade_5 = 'D'
            load_5 += 2 * self.course_5_credit_load
        elif self.total_score_5 >= 44 and self.total_score_5 <= 40:
            self.grade_5 = 'E'
            load_5 += 1 * self.course_5_credit_load
        else:
            self.grade_5 = 'F'
            load_5 += 0 * self.course_5_credit_load
        

        load_6 = 0
        if self.total_score_6 >= 70 and self.total_score_6 <= 100:
            self.grade_6 = 'A'
            load_6 += 5 * self.course_6_credit_load
        elif self.total_score_6 >= 60 and self.total_score_6 <= 69:
            self.grade_6 = 'B'
            load_6 += 4 * self.course_6_credit_load
        elif self.total_score_6 >= 50 and self.total_score_6 <= 59:
            self.grade_6 = 'C'
            load_6 += 3 * self.course_6_credit_load
        elif self.total_score_6 >= 45 and self.total_score_6 <= 49:
            self.grade_6 = 'D'
            load_6 += 2 * self.course_6_credit_load
        elif self.total_score_6 >= 44 and self.total_score_6 <= 40:
            self.grade_6 = 'E'
            load_6 += 1 * self.course_6_credit_load
        else:
            self.grade_6 = 'F'
            load_6 += 0 * self.course_6_credit_load

        
        load_7 = 0
        if self.total_score_7 >= 70 and self.total_score_7 <= 100:
            self.grade_7 = 'A'
            load_7 += 5 * self.course_7_credit_load
        elif self.total_score_7 >= 60 and self.total_score_7 <= 69:
            self.grade_7 = 'B'
            load_7 += 4 * self.course_7_credit_load
        elif self.total_score_7 >= 50 and self.total_score_7 <= 59:
            self.grade_7 = 'C'
            load_7 += 3 * self.course_7_credit_load
        elif self.total_score_7 >= 45 and self.total_score_7 <= 49:
            self.grade_7 = 'D'
            load_7 += 2 * self.course_7_credit_load
        elif self.total_score_7 >= 44 and self.total_score_7 <= 40:
            self.grade_7 = 'E'
            load_7 += 1 * self.course_7_credit_load
        else:
            self.grade_7 = 'F'
            load_7 += 0 * self.course_7_credit_load

        
        load_8 = 0
        if self.total_score_8 >= 70 and self.total_score_8 <= 100:
            self.grade_8 = 'A'
            load_8 += 5 * self.course_8_credit_load
        elif self.total_score_8 >= 60 and self.total_score_8 <= 69:
            self.grade_8 = 'B'
            load_8 += 4 * self.course_8_credit_load
        elif self.total_score_8 >= 50 and self.total_score_8 <= 59:
            self.grade_8 = 'C'
            load_8 += 3 * self.course_8_credit_load
        elif self.total_score_8 >= 45 and self.total_score_8 <= 49:
            self.grade_8 = 'D'
            load_8 += 2 * self.course_8_credit_load
        elif self.total_score_8 >= 44 and self.total_score_8 <= 40:
            self.grade_8 = 'E'
            load_8 += 1 * self.course_8_credit_load
        else:
            self.grade_8 = 'F'
            load_8 += 0 * self.course_8_credit_load

        
        load_9 = 0
        if self.total_score_9 >= 70 and self.total_score_9 <= 100:
            self.grade_9 = 'A'
            load_9 += 5 * self.course_9_credit_load
        elif self.total_score_9 >= 60 and self.total_score_9 <= 69:
            self.grade_9 = 'B'
            load_9 += 4 * self.course_9_credit_load
        elif self.total_score_9 >= 50 and self.total_score_9 <= 59:
            self.grade_9 = 'C'
            load_9 += 3 * self.course_9_credit_load
        elif self.total_score_9 >= 45 and self.total_score_9 <= 49:
            self.grade_9 = 'D'
            load_9 += 2 * self.course_9_credit_load
        elif self.total_score_9 >= 44 and self.total_score_9 <= 40:
            self.grade_9 = 'E'
            load_9 += 1 * self.course_9_credit_load
        else:
            self.grade_9 = 'F'
            load_9 += 0 * self.course_9_credit_load


        load_10 = 0
        if self.total_score_10 >= 70 and self.total_score_10 <= 100:
            self.grade_10 = 'A'
            load_10 += 5 * self.course_10_credit_load
        elif self.total_score_10 >= 60 and self.total_score_10 <= 69:
            self.grade_10 = 'B'
            load_10 += 4 * self.course_10_credit_load
        elif self.total_score_10 >= 50 and self.total_score_10 <= 59:
            self.grade_10 = 'C'
            load_10 += 3 * self.course_10_credit_load
        elif self.total_score_10 >= 45 and self.total_score_10 <= 49:
            self.grade_10 = 'D'
            load_10 += 2 * self.course_10_credit_load
        elif self.total_score_10 >= 44 and self.total_score_10 <= 40:
            self.grade_10 = 'E'
            load_10 += 1 * self.course_10_credit_load
        else:
            self.grade_10 = 'F'
            load_10 += 0 * self.course_10_credit_load

        
        load_11 = 0
        if self.total_score_11 >= 70 and self.total_score_11 <= 100:
            self.grade_11 = 'A'
            load_11 += 5 * self.course_11_credit_load
        elif self.total_score_11 >= 60 and self.total_score_11 <= 69:
            self.grade_11 = 'B'
            load_11 += 4 * self.course_11_credit_load
        elif self.total_score_11 >= 50 and self.total_score_11 <= 59:
            self.grade_11 = 'C'
            load_11 += 3 * self.course_11_credit_load
        elif self.total_score_11 >= 45 and self.total_score_11 <= 49:
            self.grade_11 = 'D'
            load_11 += 2 * self.course_11_credit_load
        elif self.total_score_11 >= 44 and self.total_score_11 <= 40:
            self.grade_11 = 'E'
            load_11 += 1 * self.course_11_credit_load
        else:
            self.grade_11 = 'F'
            load_11 += 0 * self.course_11_credit_load

        
        load_12 = 0
        if self.total_score_12 >= 70 and self.total_score_12 <= 100:
            self.grade_12 = 'A'
            load_12 += 5 * self.course_12_credit_load
        elif self.total_score_12 >= 60 and self.total_score_12 <= 69:
            self.grade_12 = 'B'
            load_12 += 4 * self.course_12_credit_load
        elif self.total_score_12 >= 50 and self.total_score_12 <= 59:
            self.grade_12 = 'C'
            load_12 += 3 * self.course_12_credit_load
        elif self.total_score_12 >= 45 and self.total_score_12 <= 49:
            self.grade_12 = 'D'
            load_12 += 2 * self.course_12_credit_load
        elif self.total_score_12 >= 44 and self.total_score_12 <= 40:
            self.grade_12 = 'E'
            load_12 += 1 * self.course_12_credit_load
        else:
            self.grade_12 = 'F'
            load_12 += 0 * self.course_12_credit_load

        
        load_13 = 0
        if self.total_score_13 >= 70 and self.total_score_13 <= 100:
            self.grade_13 = 'A'
            load_13 += 5 * self.course_13_credit_load
        elif self.total_score_13 >= 60 and self.total_score_13 <= 69:
            self.grade_13 = 'B'
            load_13 += 4 * self.course_13_credit_load
        elif self.total_score_13 >= 50 and self.total_score_13 <= 59:
            self.grade_13 = 'C'
            load_13 += 3 * self.course_13_credit_load
        elif self.total_score_13 >= 45 and self.total_score_13 <= 49:
            self.grade_13 = 'D'
            load_13 += 2 * self.course_13_credit_load
        elif self.total_score_13 >= 44 and self.total_score_13 <= 40:
            self.grade_13 = 'E'
            load_13 += 1 * self.course_13_credit_load
        else:
            self.grade_13 = 'F'
            load_13 += 0 * self.course_13_credit_load


        gpa = load_13 + load_12 + load_11 + load_10 + load_9 + load_8 + load_7 + load_6 + load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load + self.course_6_credit_load + self.course_7_credit_load + self.course_8_credit_load + self.course_9_credit_load + self.course_10_credit_load + self.course_11_credit_load + + self.course_12_credit_load + + self.course_13_credit_load
        self.gpa = gpa/total_credit_load
        super().save(*args, **kwargs)




class ComputerScience200Level(models.Model):
    SEMESTER = (
        ('First semester', 'First semester'),
        ('Second semester', 'Second semester')
    )
    SESSION = (
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026')
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225, default='')
    last_name = models.CharField(max_length=225, default='')
    semester = models.CharField(choices=SEMESTER, default='', max_length=100)
    session = models.CharField(max_length=9, choices=SESSION, default='')
    level = models.CharField(max_length=3, default='200')
    course_code_1 = models.CharField(max_length=50, default='nil')
    course_title_1 = models.CharField(max_length=200, default='nil')
    course_1_credit_load = models.IntegerField(default=0)
    attendance_score_1 = models.IntegerField(default=0)
    inception_quiz_score_1 = models.IntegerField(default=0)
    midsemester_test_score_1 = models.IntegerField(default=0)
    exam_score_1 = models.IntegerField(default=0)
    total_score_1 = models.IntegerField(default=0)
    grade_1 = models.CharField(max_length=3, default='nil') 
    course_code_2 = models.CharField(max_length=50, default='nil')
    course_title_2 = models.CharField(max_length=200, default='nil')
    course_2_credit_load = models.IntegerField(default=0)
    attendance_score_2 = models.IntegerField(default=0)
    inception_quiz_score_2 = models.IntegerField(default=0)
    midsemester_test_score_2 = models.IntegerField(default=0)
    exam_score_2 = models.IntegerField(default=0)
    total_score_2 = models.IntegerField(default=0)
    grade_2 = models.CharField(max_length=3, default='nil')
    course_code_3 = models.CharField(max_length=50, default='nil')
    course_title_3 = models.CharField(max_length=200, default='nil')
    course_3_credit_load = models.IntegerField(default=0)
    attendance_score_3 = models.IntegerField(default=0)
    inception_quiz_score_3 = models.IntegerField(default=0)
    midsemester_test_score_3 = models.IntegerField(default=0)
    exam_score_3 = models.IntegerField(default=0)
    total_score_3 = models.IntegerField(default=0)
    grade_3 = models.CharField(max_length=3, default='nil') 
    course_code_4 = models.CharField(max_length=50, default='nil')
    course_title_4 = models.CharField(max_length=200, default='nil')
    course_4_credit_load = models.IntegerField(default=0)
    attendance_score_4 = models.IntegerField(default=0)
    inception_quiz_score_4 = models.IntegerField(default=0)
    midsemester_test_score_4 = models.IntegerField(default=0)
    exam_score_4 = models.IntegerField(default=0)
    total_score_4 = models.IntegerField(default=0)
    grade_4 = models.CharField(max_length=3, default='nil')
    course_code_5 = models.CharField(max_length=50, default='nil')
    course_title_5 = models.CharField(max_length=200, default='nil')
    course_5_credit_load = models.IntegerField(default=0)
    attendance_score_5 = models.IntegerField(default=0)
    inception_quiz_score_5 = models.IntegerField(default=0)
    midsemester_test_score_5 = models.IntegerField(default=0)
    exam_score_5 = models.IntegerField(default=0)
    total_score_5 = models.IntegerField(default=0)
    grade_5 = models.CharField(max_length=3, default='nil')
    course_code_6 = models.CharField(max_length=50, default='nil')
    course_title_6 = models.CharField(max_length=200, default='nil')
    course_6_credit_load = models.IntegerField(default=0)
    attendance_score_6 = models.IntegerField(default=0)
    inception_quiz_score_6 = models.IntegerField(default=0)
    midsemester_test_score_6 = models.IntegerField(default=0)
    exam_score_6 = models.IntegerField(default=0)
    total_score_6 = models.IntegerField(default=0)
    grade_6 = models.CharField(max_length=3, default='nil')
    course_code_7 = models.CharField(max_length=50, default='nil')
    course_title_7 = models.CharField(max_length=200, default='nil')
    course_7_credit_load = models.IntegerField(default=0)
    attendance_score_7 = models.IntegerField(default=0)
    inception_quiz_score_7 = models.IntegerField(default=0)
    midsemester_test_score_7 = models.IntegerField(default=0)
    exam_score_7 = models.IntegerField(default=0)
    total_score_7 = models.IntegerField(default=0)
    grade_7 = models.CharField(max_length=3, default='nil')
    course_code_8 = models.CharField(max_length=50, default='nil')
    course_title_8 = models.CharField(max_length=200, default='nil')
    course_8_credit_load = models.IntegerField(default=0)
    attendance_score_8 = models.IntegerField(default=0)
    inception_quiz_score_8 = models.IntegerField(default=0)
    midsemester_test_score_8 = models.IntegerField(default=0)
    exam_score_8 = models.IntegerField(default=0)
    total_score_8 = models.IntegerField(default=0)
    grade_8 = models.CharField(max_length=3, default='nil')
    course_code_9 = models.CharField(max_length=50, default='nil')
    course_title_9 = models.CharField(max_length=200, default='nil')
    course_9_credit_load = models.IntegerField(default=0)
    attendance_score_9 = models.IntegerField(default=0)
    inception_quiz_score_9 = models.IntegerField(default=0)
    midsemester_test_score_9 = models.IntegerField(default=0)
    exam_score_9 = models.IntegerField(default=0)
    total_score_9 = models.IntegerField(default=0)
    grade_9 = models.CharField(max_length=3, default='nil')
    course_code_10 = models.CharField(max_length=50, default='nil')
    course_title_10 = models.CharField(max_length=200, default='nil')
    course_10_credit_load = models.IntegerField(default=0)
    attendance_score_10 = models.IntegerField(default=0)
    inception_quiz_score_10 = models.IntegerField(default=0)
    midsemester_test_score_10 = models.IntegerField(default=0)
    exam_score_10 = models.IntegerField(default=0)
    total_score_10 = models.IntegerField(default=0)
    grade_10 = models.CharField(max_length=3, default='nil')
    course_code_11 = models.CharField(max_length=50, default='nil')
    course_title_11 = models.CharField(max_length=200, default='nil')
    course_11_credit_load = models.IntegerField(default=0)
    attendance_score_11 = models.IntegerField(default=0)
    inception_quiz_score_11 = models.IntegerField(default=0)
    midsemester_test_score_11 = models.IntegerField(default=0)
    exam_score_11 = models.IntegerField(default=0)
    total_score_11 = models.IntegerField(default=0)
    grade_11 = models.CharField(max_length=3, default='nil')
    course_code_12 = models.CharField(max_length=50, default='nil')
    course_title_12 = models.CharField(max_length=200, default='nil')
    course_12_credit_load = models.IntegerField(default=0)
    attendance_score_12 = models.IntegerField(default=0)
    inception_quiz_score_12 = models.IntegerField(default=0)
    midsemester_test_score_12 = models.IntegerField(default=0)
    exam_score_12 = models.IntegerField(default=0)
    total_score_12 = models.IntegerField(default=0)
    grade_12 = models.CharField(max_length=3, default='nil')
    course_code_13 = models.CharField(max_length=50, default='nil')
    course_title_13 = models.CharField(max_length=200, default='nil')
    course_13_credit_load = models.IntegerField(default=0)
    attendance_score_13 = models.IntegerField(default=0)
    inception_quiz_score_13 = models.IntegerField(default=0)
    midsemester_test_score_13 = models.IntegerField(default=0)
    exam_score_13 = models.IntegerField(default=0)
    total_score_13 = models.IntegerField(default=0)
    grade_13 = models.CharField(max_length=3, default='nil')
    gpa = models.DecimalField(default=0, max_digits=10, decimal_places=1)
    average_score = models.DecimalField(default=0, max_digits=10, decimal_places=1)


    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.total_score_1 = self.attendance_score_1 + self.inception_quiz_score_1 + self.midsemester_test_score_1 + self.exam_score_1
        self.total_score_2 = self.attendance_score_2 + self.inception_quiz_score_2 + self.midsemester_test_score_2 + self.exam_score_2
        self.total_score_3 = self.attendance_score_3 + self.inception_quiz_score_3 + self.midsemester_test_score_3 + self.exam_score_3
        self.total_score_4 = self.attendance_score_4 + self.inception_quiz_score_4 + self.midsemester_test_score_4 + self.exam_score_4
        self.total_score_5 = self.attendance_score_5 + self.inception_quiz_score_5 + self.midsemester_test_score_5 + self.exam_score_5
        self.total_score_6 = self.attendance_score_6 + self.inception_quiz_score_6 + self.midsemester_test_score_6 + self.exam_score_6
        self.total_score_7 = self.attendance_score_7 + self.inception_quiz_score_7 + self.midsemester_test_score_7 + self.exam_score_7
        self.total_score_8 = self.attendance_score_8 + self.inception_quiz_score_8 + self.midsemester_test_score_8 + self.exam_score_8
        self.total_score_9 = self.attendance_score_9 + self.inception_quiz_score_9 + self.midsemester_test_score_9 + self.exam_score_9
        self.total_score_10 = self.attendance_score_10 + self.inception_quiz_score_10 + self.midsemester_test_score_10 + self.exam_score_10
        self.total_score_11 = self.attendance_score_11 + self.inception_quiz_score_11 + self.midsemester_test_score_11 + self.exam_score_11
        self.total_score_12 = self.attendance_score_12 + self.inception_quiz_score_12 + self.midsemester_test_score_12 + self.exam_score_12
        self.total_score_13 = self.attendance_score_13 + self.inception_quiz_score_13 + self.midsemester_test_score_13 + self.exam_score_13

        
        if self.course_code_1 != 'nil':
            self.average_score = self.total_score_1/1
        if self.course_code_2 != 'nil':
            self.average_score = self.total_score_2 + self.total_score_1 / 2
        if self.course_code_3 != 'nil':
            self.average_score = self.total_score_3 + self.total_score_2 + self.total_score_3 / 3
        if self.course_code_4 != 'nil':
            self.average_score = self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 4
        if self.course_code_5 != 'nil':
            self.average_score = self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 5
        if self.course_code_6 != 'nil':
            self.average_score = self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 6
        if self.course_code_7 != 'nil':
            self.average_score = self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 7
        if self.course_code_8 != 'nil':
            self.average_score = self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 8
        if self.course_code_9 != 'nil':
            self.average_score = self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 9
        if self.course_code_10 != 'nil':
            self.average_score = self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 10
        if self.course_code_11 != 'nil':
            self.average_score = self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 11
        if self.course_code_12 != 'nil':
            self.average_score = self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 12
        if self.course_code_13 != 'nil':
            self.average_score = self.total_score_13 + self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 13
        


        load_1 = 0
        if self.total_score_1 >= 70 and self.total_score_1 <= 100:
            self.grade_1 = 'A'
            load_1 += 5 * self.course_1_credit_load
        elif self.total_score_1 >= 60 and self.total_score_1 <= 69:
            self.grade_1 = 'B'
            load_1 += 4 * self.course_1_credit_load
        elif self.total_score_1 >= 50 and self.total_score_1 <= 59:
            self.grade_1 = 'C'
            load_1 += 3 * self.course_1_credit_load
        elif self.total_score_1 >= 45 and self.total_score_1 <= 49:
            self.grade_1 = 'D'
            load_1 += 2 * self.course_1_credit_load
        elif self.total_score_1 >= 44 and self.total_score_1 <= 40:
            self.grade_1 = 'E'
            load_1 += 1 * self.course_1_credit_load
        else:
            self.grade_1 = 'F'
            load_1 += 0 * self.course_1_credit_load


        load_2 = 0
        if self.total_score_2 >= 70 and self.total_score_2 <= 100:
            self.grade_2 = 'A'
            load_2 += 5 * self.course_2_credit_load
        elif self.total_score_2 >= 60 and self.total_score_2 <= 69:
            self.grade_2 = 'B'
            load_2 += 4 * self.course_2_credit_load
        elif self.total_score_2 >= 50 and self.total_score_2 <= 59:
            self.grade_2 = 'C'
            load_2 += 3 * self.course_2_credit_load
        elif self.total_score_2 >= 45 and self.total_score_2 <= 49:
            self.grade_2 = 'D'
            load_2 += 2 * self.course_2_credit_load
        elif self.total_score_2 >= 44 and self.total_score_2 <= 40:
            self.grade_2 = 'E'
            load_2 += 1 * self.course_2_credit_load
        else:
            self.grade_2 = 'F'
            load_2 += 0 * self.course_2_credit_load

        
        load_3 = 0
        if self.total_score_3 >= 70 and self.total_score_3 <= 100:
            self.grade_3 = 'A'
            load_3 += 5 * self.course_3_credit_load
        elif self.total_score_3 >= 60 and self.total_score_3 <= 69:
            self.grade_3 = 'B'
            load_3 += 4 * self.course_3_credit_load
        elif self.total_score_3 >= 50 and self.total_score_3 <= 59:
            self.grade_3 = 'C'
            load_3 += 3 * self.course_3_credit_load
        elif self.total_score_3 >= 45 and self.total_score_3 <= 49:
            self.grade_3 = 'D'
            load_3 += 2 * self.course_3_credit_load
        elif self.total_score_3 >= 44 and self.total_score_3 <= 40:
            self.grade_3 = 'E'
            load_3 += 1 * self.course_3_credit_load
        else:
            self.grade_3 = 'F'
            load_3 += 0 * self.course_3_credit_load


        load_4 = 0
        if self.total_score_4 >= 70 and self.total_score_4 <= 100:
            self.grade_4 = 'A'
            load_4 += 5 * self.course_4_credit_load
        elif self.total_score_4 >= 60 and self.total_score_4 <= 69:
            self.grade_4 = 'B'
            load_4 += 4 * self.course_4_credit_load
        elif self.total_score_4 >= 50 and self.total_score_4 <= 59:
            self.grade_4 = 'C'
            load_4 += 3 * self.course_4_credit_load
        elif self.total_score_4 >= 45 and self.total_score_4 <= 49:
            self.grade_4 = 'D'
            load_4 += 2 * self.course_4_credit_load
        elif self.total_score_4 >= 44 and self.total_score_4 <= 40:
            self.grade_4 = 'E'
            load_4 += 1 * self.course_4_credit_load
        else:
            self.grade_4 = 'F'
            load_4 += 0 * self.course_4_credit_load


        load_5 = 0
        if self.total_score_5 >= 70 and self.total_score_5 <= 100:
            self.grade_5 = 'A'
            load_5 += 5 * self.course_5_credit_load
        elif self.total_score_5 >= 60 and self.total_score_5 <= 69:
            self.grade_5 = 'B'
            load_5 += 4 * self.course_5_credit_load
        elif self.total_score_5 >= 50 and self.total_score_5 <= 59:
            self.grade_5 = 'C'
            load_5 += 3 * self.course_5_credit_load
        elif self.total_score_5 >= 45 and self.total_score_5 <= 49:
            self.grade_5 = 'D'
            load_5 += 2 * self.course_5_credit_load
        elif self.total_score_5 >= 44 and self.total_score_5 <= 40:
            self.grade_5 = 'E'
            load_5 += 1 * self.course_5_credit_load
        else:
            self.grade_5 = 'F'
            load_5 += 0 * self.course_5_credit_load
        

        load_6 = 0
        if self.total_score_6 >= 70 and self.total_score_6 <= 100:
            self.grade_6 = 'A'
            load_6 += 5 * self.course_6_credit_load
        elif self.total_score_6 >= 60 and self.total_score_6 <= 69:
            self.grade_6 = 'B'
            load_6 += 4 * self.course_6_credit_load
        elif self.total_score_6 >= 50 and self.total_score_6 <= 59:
            self.grade_6 = 'C'
            load_6 += 3 * self.course_6_credit_load
        elif self.total_score_6 >= 45 and self.total_score_6 <= 49:
            self.grade_6 = 'D'
            load_6 += 2 * self.course_6_credit_load
        elif self.total_score_6 >= 44 and self.total_score_6 <= 40:
            self.grade_6 = 'E'
            load_6 += 1 * self.course_6_credit_load
        else:
            self.grade_6 = 'F'
            load_6 += 0 * self.course_6_credit_load

        
        load_7 = 0
        if self.total_score_7 >= 70 and self.total_score_7 <= 100:
            self.grade_7 = 'A'
            load_7 += 5 * self.course_7_credit_load
        elif self.total_score_7 >= 60 and self.total_score_7 <= 69:
            self.grade_7 = 'B'
            load_7 += 4 * self.course_7_credit_load
        elif self.total_score_7 >= 50 and self.total_score_7 <= 59:
            self.grade_7 = 'C'
            load_7 += 3 * self.course_7_credit_load
        elif self.total_score_7 >= 45 and self.total_score_7 <= 49:
            self.grade_7 = 'D'
            load_7 += 2 * self.course_7_credit_load
        elif self.total_score_7 >= 44 and self.total_score_7 <= 40:
            self.grade_7 = 'E'
            load_7 += 1 * self.course_7_credit_load
        else:
            self.grade_7 = 'F'
            load_7 += 0 * self.course_7_credit_load

        
        load_8 = 0
        if self.total_score_8 >= 70 and self.total_score_8 <= 100:
            self.grade_8 = 'A'
            load_8 += 5 * self.course_8_credit_load
        elif self.total_score_8 >= 60 and self.total_score_8 <= 69:
            self.grade_8 = 'B'
            load_8 += 4 * self.course_8_credit_load
        elif self.total_score_8 >= 50 and self.total_score_8 <= 59:
            self.grade_8 = 'C'
            load_8 += 3 * self.course_8_credit_load
        elif self.total_score_8 >= 45 and self.total_score_8 <= 49:
            self.grade_8 = 'D'
            load_8 += 2 * self.course_8_credit_load
        elif self.total_score_8 >= 44 and self.total_score_8 <= 40:
            self.grade_8 = 'E'
            load_8 += 1 * self.course_8_credit_load
        else:
            self.grade_8 = 'F'
            load_8 += 0 * self.course_8_credit_load

        
        load_9 = 0
        if self.total_score_9 >= 70 and self.total_score_9 <= 100:
            self.grade_9 = 'A'
            load_9 += 5 * self.course_9_credit_load
        elif self.total_score_9 >= 60 and self.total_score_9 <= 69:
            self.grade_9 = 'B'
            load_9 += 4 * self.course_9_credit_load
        elif self.total_score_9 >= 50 and self.total_score_9 <= 59:
            self.grade_9 = 'C'
            load_9 += 3 * self.course_9_credit_load
        elif self.total_score_9 >= 45 and self.total_score_9 <= 49:
            self.grade_9 = 'D'
            load_9 += 2 * self.course_9_credit_load
        elif self.total_score_9 >= 44 and self.total_score_9 <= 40:
            self.grade_9 = 'E'
            load_9 += 1 * self.course_9_credit_load
        else:
            self.grade_9 = 'F'
            load_9 += 0 * self.course_9_credit_load


        load_10 = 0
        if self.total_score_10 >= 70 and self.total_score_10 <= 100:
            self.grade_10 = 'A'
            load_10 += 5 * self.course_10_credit_load
        elif self.total_score_10 >= 60 and self.total_score_10 <= 69:
            self.grade_10 = 'B'
            load_10 += 4 * self.course_10_credit_load
        elif self.total_score_10 >= 50 and self.total_score_10 <= 59:
            self.grade_10 = 'C'
            load_10 += 3 * self.course_10_credit_load
        elif self.total_score_10 >= 45 and self.total_score_10 <= 49:
            self.grade_10 = 'D'
            load_10 += 2 * self.course_10_credit_load
        elif self.total_score_10 >= 44 and self.total_score_10 <= 40:
            self.grade_10 = 'E'
            load_10 += 1 * self.course_10_credit_load
        else:
            self.grade_10 = 'F'
            load_10 += 0 * self.course_10_credit_load

        
        load_11 = 0
        if self.total_score_11 >= 70 and self.total_score_11 <= 100:
            self.grade_11 = 'A'
            load_11 += 5 * self.course_11_credit_load
        elif self.total_score_11 >= 60 and self.total_score_11 <= 69:
            self.grade_11 = 'B'
            load_11 += 4 * self.course_11_credit_load
        elif self.total_score_11 >= 50 and self.total_score_11 <= 59:
            self.grade_11 = 'C'
            load_11 += 3 * self.course_11_credit_load
        elif self.total_score_11 >= 45 and self.total_score_11 <= 49:
            self.grade_11 = 'D'
            load_11 += 2 * self.course_11_credit_load
        elif self.total_score_11 >= 44 and self.total_score_11 <= 40:
            self.grade_11 = 'E'
            load_11 += 1 * self.course_11_credit_load
        else:
            self.grade_11 = 'F'
            load_11 += 0 * self.course_11_credit_load

        
        load_12 = 0
        if self.total_score_12 >= 70 and self.total_score_12 <= 100:
            self.grade_12 = 'A'
            load_12 += 5 * self.course_12_credit_load
        elif self.total_score_12 >= 60 and self.total_score_12 <= 69:
            self.grade_12 = 'B'
            load_12 += 4 * self.course_12_credit_load
        elif self.total_score_12 >= 50 and self.total_score_12 <= 59:
            self.grade_12 = 'C'
            load_12 += 3 * self.course_12_credit_load
        elif self.total_score_12 >= 45 and self.total_score_12 <= 49:
            self.grade_12 = 'D'
            load_12 += 2 * self.course_12_credit_load
        elif self.total_score_12 >= 44 and self.total_score_12 <= 40:
            self.grade_12 = 'E'
            load_12 += 1 * self.course_12_credit_load
        else:
            self.grade_12 = 'F'
            load_12 += 0 * self.course_12_credit_load

        
        load_13 = 0
        if self.total_score_13 >= 70 and self.total_score_13 <= 100:
            self.grade_13 = 'A'
            load_13 += 5 * self.course_13_credit_load
        elif self.total_score_13 >= 60 and self.total_score_13 <= 69:
            self.grade_13 = 'B'
            load_13 += 4 * self.course_13_credit_load
        elif self.total_score_13 >= 50 and self.total_score_13 <= 59:
            self.grade_13 = 'C'
            load_13 += 3 * self.course_13_credit_load
        elif self.total_score_13 >= 45 and self.total_score_13 <= 49:
            self.grade_13 = 'D'
            load_13 += 2 * self.course_13_credit_load
        elif self.total_score_13 >= 44 and self.total_score_13 <= 40:
            self.grade_13 = 'E'
            load_13 += 1 * self.course_13_credit_load
        else:
            self.grade_13 = 'F'
            load_13 += 0 * self.course_13_credit_load


        gpa = load_13 + load_12 + load_11 + load_10 + load_9 + load_8 + load_7 + load_6 + load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load + self.course_6_credit_load + self.course_7_credit_load + self.course_8_credit_load + self.course_9_credit_load + self.course_10_credit_load + self.course_11_credit_load + + self.course_12_credit_load + + self.course_13_credit_load
        self.gpa = gpa/total_credit_load
        super().save(*args, **kwargs)







class ComputerScience300Level(models.Model):
    SEMESTER = (
        ('First semester', 'First semester'),
        ('Second semester', 'Second semester')
    )
    SESSION = (
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026')
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225, default='')
    last_name = models.CharField(max_length=225, default='')
    semester = models.CharField(choices=SEMESTER, default='', max_length=100)
    session = models.CharField(max_length=9, choices=SESSION, default='')
    level = models.CharField(max_length=3, default='300')
    course_code_1 = models.CharField(max_length=50, default='nil')
    course_title_1 = models.CharField(max_length=200, default='nil')
    course_1_credit_load = models.IntegerField(default=0)
    attendance_score_1 = models.IntegerField(default=0)
    inception_quiz_score_1 = models.IntegerField(default=0)
    midsemester_test_score_1 = models.IntegerField(default=0)
    exam_score_1 = models.IntegerField(default=0)
    total_score_1 = models.IntegerField(default=0)
    grade_1 = models.CharField(max_length=3, default='nil') 
    course_code_2 = models.CharField(max_length=50, default='nil')
    course_title_2 = models.CharField(max_length=200, default='nil')
    course_2_credit_load = models.IntegerField(default=0)
    attendance_score_2 = models.IntegerField(default=0)
    inception_quiz_score_2 = models.IntegerField(default=0)
    midsemester_test_score_2 = models.IntegerField(default=0)
    exam_score_2 = models.IntegerField(default=0)
    total_score_2 = models.IntegerField(default=0)
    grade_2 = models.CharField(max_length=3, default='nil')
    course_code_3 = models.CharField(max_length=50, default='nil')
    course_title_3 = models.CharField(max_length=200, default='nil')
    course_3_credit_load = models.IntegerField(default=0)
    attendance_score_3 = models.IntegerField(default=0)
    inception_quiz_score_3 = models.IntegerField(default=0)
    midsemester_test_score_3 = models.IntegerField(default=0)
    exam_score_3 = models.IntegerField(default=0)
    total_score_3 = models.IntegerField(default=0)
    grade_3 = models.CharField(max_length=3, default='nil') 
    course_code_4 = models.CharField(max_length=50, default='nil')
    course_title_4 = models.CharField(max_length=200, default='nil')
    course_4_credit_load = models.IntegerField(default=0)
    attendance_score_4 = models.IntegerField(default=0)
    inception_quiz_score_4 = models.IntegerField(default=0)
    midsemester_test_score_4 = models.IntegerField(default=0)
    exam_score_4 = models.IntegerField(default=0)
    total_score_4 = models.IntegerField(default=0)
    grade_4 = models.CharField(max_length=3, default='nil')
    course_code_5 = models.CharField(max_length=50, default='nil')
    course_title_5 = models.CharField(max_length=200, default='nil')
    course_5_credit_load = models.IntegerField(default=0)
    attendance_score_5 = models.IntegerField(default=0)
    inception_quiz_score_5 = models.IntegerField(default=0)
    midsemester_test_score_5 = models.IntegerField(default=0)
    exam_score_5 = models.IntegerField(default=0)
    total_score_5 = models.IntegerField(default=0)
    grade_5 = models.CharField(max_length=3, default='nil')
    course_code_6 = models.CharField(max_length=50, default='nil')
    course_title_6 = models.CharField(max_length=200, default='nil')
    course_6_credit_load = models.IntegerField(default=0)
    attendance_score_6 = models.IntegerField(default=0)
    inception_quiz_score_6 = models.IntegerField(default=0)
    midsemester_test_score_6 = models.IntegerField(default=0)
    exam_score_6 = models.IntegerField(default=0)
    total_score_6 = models.IntegerField(default=0)
    grade_6 = models.CharField(max_length=3, default='nil')
    course_code_7 = models.CharField(max_length=50, default='nil')
    course_title_7 = models.CharField(max_length=200, default='nil')
    course_7_credit_load = models.IntegerField(default=0)
    attendance_score_7 = models.IntegerField(default=0)
    inception_quiz_score_7 = models.IntegerField(default=0)
    midsemester_test_score_7 = models.IntegerField(default=0)
    exam_score_7 = models.IntegerField(default=0)
    total_score_7 = models.IntegerField(default=0)
    grade_7 = models.CharField(max_length=3, default='nil')
    course_code_8 = models.CharField(max_length=50, default='nil')
    course_title_8 = models.CharField(max_length=200, default='nil')
    course_8_credit_load = models.IntegerField(default=0)
    attendance_score_8 = models.IntegerField(default=0)
    inception_quiz_score_8 = models.IntegerField(default=0)
    midsemester_test_score_8 = models.IntegerField(default=0)
    exam_score_8 = models.IntegerField(default=0)
    total_score_8 = models.IntegerField(default=0)
    grade_8 = models.CharField(max_length=3, default='nil')
    course_code_9 = models.CharField(max_length=50, default='nil')
    course_title_9 = models.CharField(max_length=200, default='nil')
    course_9_credit_load = models.IntegerField(default=0)
    attendance_score_9 = models.IntegerField(default=0)
    inception_quiz_score_9 = models.IntegerField(default=0)
    midsemester_test_score_9 = models.IntegerField(default=0)
    exam_score_9 = models.IntegerField(default=0)
    total_score_9 = models.IntegerField(default=0)
    grade_9 = models.CharField(max_length=3, default='nil')
    course_code_10 = models.CharField(max_length=50, default='nil')
    course_title_10 = models.CharField(max_length=200, default='nil')
    course_10_credit_load = models.IntegerField(default=0)
    attendance_score_10 = models.IntegerField(default=0)
    inception_quiz_score_10 = models.IntegerField(default=0)
    midsemester_test_score_10 = models.IntegerField(default=0)
    exam_score_10 = models.IntegerField(default=0)
    total_score_10 = models.IntegerField(default=0)
    grade_10 = models.CharField(max_length=3, default='nil')
    course_code_11 = models.CharField(max_length=50, default='nil')
    course_title_11 = models.CharField(max_length=200, default='nil')
    course_11_credit_load = models.IntegerField(default=0)
    attendance_score_11 = models.IntegerField(default=0)
    inception_quiz_score_11 = models.IntegerField(default=0)
    midsemester_test_score_11 = models.IntegerField(default=0)
    exam_score_11 = models.IntegerField(default=0)
    total_score_11 = models.IntegerField(default=0)
    grade_11 = models.CharField(max_length=3, default='nil')
    course_code_12 = models.CharField(max_length=50, default='nil')
    course_title_12 = models.CharField(max_length=200, default='nil')
    course_12_credit_load = models.IntegerField(default=0)
    attendance_score_12 = models.IntegerField(default=0)
    inception_quiz_score_12 = models.IntegerField(default=0)
    midsemester_test_score_12 = models.IntegerField(default=0)
    exam_score_12 = models.IntegerField(default=0)
    total_score_12 = models.IntegerField(default=0)
    grade_12 = models.CharField(max_length=3, default='nil')
    course_code_13 = models.CharField(max_length=50, default='nil')
    course_title_13 = models.CharField(max_length=200, default='nil')
    course_13_credit_load = models.IntegerField(default=0)
    attendance_score_13 = models.IntegerField(default=0)
    inception_quiz_score_13 = models.IntegerField(default=0)
    midsemester_test_score_13 = models.IntegerField(default=0)
    exam_score_13 = models.IntegerField(default=0)
    total_score_13 = models.IntegerField(default=0)
    grade_13 = models.CharField(max_length=3, default='nil')
    gpa = models.DecimalField(default=0, max_digits=10, decimal_places=1)
    average_score = models.DecimalField(default=0, max_digits=10, decimal_places=1)


    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.total_score_1 = self.attendance_score_1 + self.inception_quiz_score_1 + self.midsemester_test_score_1 + self.exam_score_1
        self.total_score_2 = self.attendance_score_2 + self.inception_quiz_score_2 + self.midsemester_test_score_2 + self.exam_score_2
        self.total_score_3 = self.attendance_score_3 + self.inception_quiz_score_3 + self.midsemester_test_score_3 + self.exam_score_3
        self.total_score_4 = self.attendance_score_4 + self.inception_quiz_score_4 + self.midsemester_test_score_4 + self.exam_score_4
        self.total_score_5 = self.attendance_score_5 + self.inception_quiz_score_5 + self.midsemester_test_score_5 + self.exam_score_5
        self.total_score_6 = self.attendance_score_6 + self.inception_quiz_score_6 + self.midsemester_test_score_6 + self.exam_score_6
        self.total_score_7 = self.attendance_score_7 + self.inception_quiz_score_7 + self.midsemester_test_score_7 + self.exam_score_7
        self.total_score_8 = self.attendance_score_8 + self.inception_quiz_score_8 + self.midsemester_test_score_8 + self.exam_score_8
        self.total_score_9 = self.attendance_score_9 + self.inception_quiz_score_9 + self.midsemester_test_score_9 + self.exam_score_9
        self.total_score_10 = self.attendance_score_10 + self.inception_quiz_score_10 + self.midsemester_test_score_10 + self.exam_score_10
        self.total_score_11 = self.attendance_score_11 + self.inception_quiz_score_11 + self.midsemester_test_score_11 + self.exam_score_11
        self.total_score_12 = self.attendance_score_12 + self.inception_quiz_score_12 + self.midsemester_test_score_12 + self.exam_score_12
        self.total_score_13 = self.attendance_score_13 + self.inception_quiz_score_13 + self.midsemester_test_score_13 + self.exam_score_13

        
        if self.course_code_1 != 'nil':
            self.average_score = self.total_score_1/1
        if self.course_code_2 != 'nil':
            self.average_score = self.total_score_2 + self.total_score_1 / 2
        if self.course_code_3 != 'nil':
            self.average_score = self.total_score_3 + self.total_score_2 + self.total_score_3 / 3
        if self.course_code_4 != 'nil':
            self.average_score = self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 4
        if self.course_code_5 != 'nil':
            self.average_score = self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 5
        if self.course_code_6 != 'nil':
            self.average_score = self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 6
        if self.course_code_7 != 'nil':
            self.average_score = self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 7
        if self.course_code_8 != 'nil':
            self.average_score = self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 8
        if self.course_code_9 != 'nil':
            self.average_score = self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 9
        if self.course_code_10 != 'nil':
            self.average_score = self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 10
        if self.course_code_11 != 'nil':
            self.average_score = self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 11
        if self.course_code_12 != 'nil':
            self.average_score = self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 12
        if self.course_code_13 != 'nil':
            self.average_score = self.total_score_13 + self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 13
        


        load_1 = 0
        if self.total_score_1 >= 70 and self.total_score_1 <= 100:
            self.grade_1 = 'A'
            load_1 += 5 * self.course_1_credit_load
        elif self.total_score_1 >= 60 and self.total_score_1 <= 69:
            self.grade_1 = 'B'
            load_1 += 4 * self.course_1_credit_load
        elif self.total_score_1 >= 50 and self.total_score_1 <= 59:
            self.grade_1 = 'C'
            load_1 += 3 * self.course_1_credit_load
        elif self.total_score_1 >= 45 and self.total_score_1 <= 49:
            self.grade_1 = 'D'
            load_1 += 2 * self.course_1_credit_load
        elif self.total_score_1 >= 44 and self.total_score_1 <= 40:
            self.grade_1 = 'E'
            load_1 += 1 * self.course_1_credit_load
        else:
            self.grade_1 = 'F'
            load_1 += 0 * self.course_1_credit_load


        load_2 = 0
        if self.total_score_2 >= 70 and self.total_score_2 <= 100:
            self.grade_2 = 'A'
            load_2 += 5 * self.course_2_credit_load
        elif self.total_score_2 >= 60 and self.total_score_2 <= 69:
            self.grade_2 = 'B'
            load_2 += 4 * self.course_2_credit_load
        elif self.total_score_2 >= 50 and self.total_score_2 <= 59:
            self.grade_2 = 'C'
            load_2 += 3 * self.course_2_credit_load
        elif self.total_score_2 >= 45 and self.total_score_2 <= 49:
            self.grade_2 = 'D'
            load_2 += 2 * self.course_2_credit_load
        elif self.total_score_2 >= 44 and self.total_score_2 <= 40:
            self.grade_2 = 'E'
            load_2 += 1 * self.course_2_credit_load
        else:
            self.grade_2 = 'F'
            load_2 += 0 * self.course_2_credit_load

        
        load_3 = 0
        if self.total_score_3 >= 70 and self.total_score_3 <= 100:
            self.grade_3 = 'A'
            load_3 += 5 * self.course_3_credit_load
        elif self.total_score_3 >= 60 and self.total_score_3 <= 69:
            self.grade_3 = 'B'
            load_3 += 4 * self.course_3_credit_load
        elif self.total_score_3 >= 50 and self.total_score_3 <= 59:
            self.grade_3 = 'C'
            load_3 += 3 * self.course_3_credit_load
        elif self.total_score_3 >= 45 and self.total_score_3 <= 49:
            self.grade_3 = 'D'
            load_3 += 2 * self.course_3_credit_load
        elif self.total_score_3 >= 44 and self.total_score_3 <= 40:
            self.grade_3 = 'E'
            load_3 += 1 * self.course_3_credit_load
        else:
            self.grade_3 = 'F'
            load_3 += 0 * self.course_3_credit_load


        load_4 = 0
        if self.total_score_4 >= 70 and self.total_score_4 <= 100:
            self.grade_4 = 'A'
            load_4 += 5 * self.course_4_credit_load
        elif self.total_score_4 >= 60 and self.total_score_4 <= 69:
            self.grade_4 = 'B'
            load_4 += 4 * self.course_4_credit_load
        elif self.total_score_4 >= 50 and self.total_score_4 <= 59:
            self.grade_4 = 'C'
            load_4 += 3 * self.course_4_credit_load
        elif self.total_score_4 >= 45 and self.total_score_4 <= 49:
            self.grade_4 = 'D'
            load_4 += 2 * self.course_4_credit_load
        elif self.total_score_4 >= 44 and self.total_score_4 <= 40:
            self.grade_4 = 'E'
            load_4 += 1 * self.course_4_credit_load
        else:
            self.grade_4 = 'F'
            load_4 += 0 * self.course_4_credit_load


        load_5 = 0
        if self.total_score_5 >= 70 and self.total_score_5 <= 100:
            self.grade_5 = 'A'
            load_5 += 5 * self.course_5_credit_load
        elif self.total_score_5 >= 60 and self.total_score_5 <= 69:
            self.grade_5 = 'B'
            load_5 += 4 * self.course_5_credit_load
        elif self.total_score_5 >= 50 and self.total_score_5 <= 59:
            self.grade_5 = 'C'
            load_5 += 3 * self.course_5_credit_load
        elif self.total_score_5 >= 45 and self.total_score_5 <= 49:
            self.grade_5 = 'D'
            load_5 += 2 * self.course_5_credit_load
        elif self.total_score_5 >= 44 and self.total_score_5 <= 40:
            self.grade_5 = 'E'
            load_5 += 1 * self.course_5_credit_load
        else:
            self.grade_5 = 'F'
            load_5 += 0 * self.course_5_credit_load
        

        load_6 = 0
        if self.total_score_6 >= 70 and self.total_score_6 <= 100:
            self.grade_6 = 'A'
            load_6 += 5 * self.course_6_credit_load
        elif self.total_score_6 >= 60 and self.total_score_6 <= 69:
            self.grade_6 = 'B'
            load_6 += 4 * self.course_6_credit_load
        elif self.total_score_6 >= 50 and self.total_score_6 <= 59:
            self.grade_6 = 'C'
            load_6 += 3 * self.course_6_credit_load
        elif self.total_score_6 >= 45 and self.total_score_6 <= 49:
            self.grade_6 = 'D'
            load_6 += 2 * self.course_6_credit_load
        elif self.total_score_6 >= 44 and self.total_score_6 <= 40:
            self.grade_6 = 'E'
            load_6 += 1 * self.course_6_credit_load
        else:
            self.grade_6 = 'F'
            load_6 += 0 * self.course_6_credit_load

        
        load_7 = 0
        if self.total_score_7 >= 70 and self.total_score_7 <= 100:
            self.grade_7 = 'A'
            load_7 += 5 * self.course_7_credit_load
        elif self.total_score_7 >= 60 and self.total_score_7 <= 69:
            self.grade_7 = 'B'
            load_7 += 4 * self.course_7_credit_load
        elif self.total_score_7 >= 50 and self.total_score_7 <= 59:
            self.grade_7 = 'C'
            load_7 += 3 * self.course_7_credit_load
        elif self.total_score_7 >= 45 and self.total_score_7 <= 49:
            self.grade_7 = 'D'
            load_7 += 2 * self.course_7_credit_load
        elif self.total_score_7 >= 44 and self.total_score_7 <= 40:
            self.grade_7 = 'E'
            load_7 += 1 * self.course_7_credit_load
        else:
            self.grade_7 = 'F'
            load_7 += 0 * self.course_7_credit_load

        
        load_8 = 0
        if self.total_score_8 >= 70 and self.total_score_8 <= 100:
            self.grade_8 = 'A'
            load_8 += 5 * self.course_8_credit_load
        elif self.total_score_8 >= 60 and self.total_score_8 <= 69:
            self.grade_8 = 'B'
            load_8 += 4 * self.course_8_credit_load
        elif self.total_score_8 >= 50 and self.total_score_8 <= 59:
            self.grade_8 = 'C'
            load_8 += 3 * self.course_8_credit_load
        elif self.total_score_8 >= 45 and self.total_score_8 <= 49:
            self.grade_8 = 'D'
            load_8 += 2 * self.course_8_credit_load
        elif self.total_score_8 >= 44 and self.total_score_8 <= 40:
            self.grade_8 = 'E'
            load_8 += 1 * self.course_8_credit_load
        else:
            self.grade_8 = 'F'
            load_8 += 0 * self.course_8_credit_load

        
        load_9 = 0
        if self.total_score_9 >= 70 and self.total_score_9 <= 100:
            self.grade_9 = 'A'
            load_9 += 5 * self.course_9_credit_load
        elif self.total_score_9 >= 60 and self.total_score_9 <= 69:
            self.grade_9 = 'B'
            load_9 += 4 * self.course_9_credit_load
        elif self.total_score_9 >= 50 and self.total_score_9 <= 59:
            self.grade_9 = 'C'
            load_9 += 3 * self.course_9_credit_load
        elif self.total_score_9 >= 45 and self.total_score_9 <= 49:
            self.grade_9 = 'D'
            load_9 += 2 * self.course_9_credit_load
        elif self.total_score_9 >= 44 and self.total_score_9 <= 40:
            self.grade_9 = 'E'
            load_9 += 1 * self.course_9_credit_load
        else:
            self.grade_9 = 'F'
            load_9 += 0 * self.course_9_credit_load


        load_10 = 0
        if self.total_score_10 >= 70 and self.total_score_10 <= 100:
            self.grade_10 = 'A'
            load_10 += 5 * self.course_10_credit_load
        elif self.total_score_10 >= 60 and self.total_score_10 <= 69:
            self.grade_10 = 'B'
            load_10 += 4 * self.course_10_credit_load
        elif self.total_score_10 >= 50 and self.total_score_10 <= 59:
            self.grade_10 = 'C'
            load_10 += 3 * self.course_10_credit_load
        elif self.total_score_10 >= 45 and self.total_score_10 <= 49:
            self.grade_10 = 'D'
            load_10 += 2 * self.course_10_credit_load
        elif self.total_score_10 >= 44 and self.total_score_10 <= 40:
            self.grade_10 = 'E'
            load_10 += 1 * self.course_10_credit_load
        else:
            self.grade_10 = 'F'
            load_10 += 0 * self.course_10_credit_load

        
        load_11 = 0
        if self.total_score_11 >= 70 and self.total_score_11 <= 100:
            self.grade_11 = 'A'
            load_11 += 5 * self.course_11_credit_load
        elif self.total_score_11 >= 60 and self.total_score_11 <= 69:
            self.grade_11 = 'B'
            load_11 += 4 * self.course_11_credit_load
        elif self.total_score_11 >= 50 and self.total_score_11 <= 59:
            self.grade_11 = 'C'
            load_11 += 3 * self.course_11_credit_load
        elif self.total_score_11 >= 45 and self.total_score_11 <= 49:
            self.grade_11 = 'D'
            load_11 += 2 * self.course_11_credit_load
        elif self.total_score_11 >= 44 and self.total_score_11 <= 40:
            self.grade_11 = 'E'
            load_11 += 1 * self.course_11_credit_load
        else:
            self.grade_11 = 'F'
            load_11 += 0 * self.course_11_credit_load

        
        load_12 = 0
        if self.total_score_12 >= 70 and self.total_score_12 <= 100:
            self.grade_12 = 'A'
            load_12 += 5 * self.course_12_credit_load
        elif self.total_score_12 >= 60 and self.total_score_12 <= 69:
            self.grade_12 = 'B'
            load_12 += 4 * self.course_12_credit_load
        elif self.total_score_12 >= 50 and self.total_score_12 <= 59:
            self.grade_12 = 'C'
            load_12 += 3 * self.course_12_credit_load
        elif self.total_score_12 >= 45 and self.total_score_12 <= 49:
            self.grade_12 = 'D'
            load_12 += 2 * self.course_12_credit_load
        elif self.total_score_12 >= 44 and self.total_score_12 <= 40:
            self.grade_12 = 'E'
            load_12 += 1 * self.course_12_credit_load
        else:
            self.grade_12 = 'F'
            load_12 += 0 * self.course_12_credit_load

        
        load_13 = 0
        if self.total_score_13 >= 70 and self.total_score_13 <= 100:
            self.grade_13 = 'A'
            load_13 += 5 * self.course_13_credit_load
        elif self.total_score_13 >= 60 and self.total_score_13 <= 69:
            self.grade_13 = 'B'
            load_13 += 4 * self.course_13_credit_load
        elif self.total_score_13 >= 50 and self.total_score_13 <= 59:
            self.grade_13 = 'C'
            load_13 += 3 * self.course_13_credit_load
        elif self.total_score_13 >= 45 and self.total_score_13 <= 49:
            self.grade_13 = 'D'
            load_13 += 2 * self.course_13_credit_load
        elif self.total_score_13 >= 44 and self.total_score_13 <= 40:
            self.grade_13 = 'E'
            load_13 += 1 * self.course_13_credit_load
        else:
            self.grade_13 = 'F'
            load_13 += 0 * self.course_13_credit_load


        gpa = load_13 + load_12 + load_11 + load_10 + load_9 + load_8 + load_7 + load_6 + load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load + self.course_6_credit_load + self.course_7_credit_load + self.course_8_credit_load + self.course_9_credit_load + self.course_10_credit_load + self.course_11_credit_load + + self.course_12_credit_load + + self.course_13_credit_load
        self.gpa = gpa/total_credit_load
        super().save(*args, **kwargs)





class ComputerScience400Level(models.Model):
    SEMESTER = (
        ('First semester', 'First semester'),
        ('Second semester', 'Second semester')
    )
    SESSION = (
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026')
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225, default='')
    last_name = models.CharField(max_length=225, default='')
    semester = models.CharField(choices=SEMESTER, default='', max_length=100)
    session = models.CharField(max_length=9, choices=SESSION, default='')
    level = models.CharField(max_length=3, default='400')
    course_code_1 = models.CharField(max_length=50, default='nil')
    course_title_1 = models.CharField(max_length=200, default='nil')
    course_1_credit_load = models.IntegerField(default=0)
    attendance_score_1 = models.IntegerField(default=0)
    inception_quiz_score_1 = models.IntegerField(default=0)
    midsemester_test_score_1 = models.IntegerField(default=0)
    exam_score_1 = models.IntegerField(default=0)
    total_score_1 = models.IntegerField(default=0)
    grade_1 = models.CharField(max_length=3, default='nil') 
    course_code_2 = models.CharField(max_length=50, default='nil')
    course_title_2 = models.CharField(max_length=200, default='nil')
    course_2_credit_load = models.IntegerField(default=0)
    attendance_score_2 = models.IntegerField(default=0)
    inception_quiz_score_2 = models.IntegerField(default=0)
    midsemester_test_score_2 = models.IntegerField(default=0)
    exam_score_2 = models.IntegerField(default=0)
    total_score_2 = models.IntegerField(default=0)
    grade_2 = models.CharField(max_length=3, default='nil')
    course_code_3 = models.CharField(max_length=50, default='nil')
    course_title_3 = models.CharField(max_length=200, default='nil')
    course_3_credit_load = models.IntegerField(default=0)
    attendance_score_3 = models.IntegerField(default=0)
    inception_quiz_score_3 = models.IntegerField(default=0)
    midsemester_test_score_3 = models.IntegerField(default=0)
    exam_score_3 = models.IntegerField(default=0)
    total_score_3 = models.IntegerField(default=0)
    grade_3 = models.CharField(max_length=3, default='nil') 
    course_code_4 = models.CharField(max_length=50, default='nil')
    course_title_4 = models.CharField(max_length=200, default='nil')
    course_4_credit_load = models.IntegerField(default=0)
    attendance_score_4 = models.IntegerField(default=0)
    inception_quiz_score_4 = models.IntegerField(default=0)
    midsemester_test_score_4 = models.IntegerField(default=0)
    exam_score_4 = models.IntegerField(default=0)
    total_score_4 = models.IntegerField(default=0)
    grade_4 = models.CharField(max_length=3, default='nil')
    course_code_5 = models.CharField(max_length=50, default='nil')
    course_title_5 = models.CharField(max_length=200, default='nil')
    course_5_credit_load = models.IntegerField(default=0)
    attendance_score_5 = models.IntegerField(default=0)
    inception_quiz_score_5 = models.IntegerField(default=0)
    midsemester_test_score_5 = models.IntegerField(default=0)
    exam_score_5 = models.IntegerField(default=0)
    total_score_5 = models.IntegerField(default=0)
    grade_5 = models.CharField(max_length=3, default='nil')
    course_code_6 = models.CharField(max_length=50, default='nil')
    course_title_6 = models.CharField(max_length=200, default='nil')
    course_6_credit_load = models.IntegerField(default=0)
    attendance_score_6 = models.IntegerField(default=0)
    inception_quiz_score_6 = models.IntegerField(default=0)
    midsemester_test_score_6 = models.IntegerField(default=0)
    exam_score_6 = models.IntegerField(default=0)
    total_score_6 = models.IntegerField(default=0)
    grade_6 = models.CharField(max_length=3, default='nil')
    course_code_7 = models.CharField(max_length=50, default='nil')
    course_title_7 = models.CharField(max_length=200, default='nil')
    course_7_credit_load = models.IntegerField(default=0)
    attendance_score_7 = models.IntegerField(default=0)
    inception_quiz_score_7 = models.IntegerField(default=0)
    midsemester_test_score_7 = models.IntegerField(default=0)
    exam_score_7 = models.IntegerField(default=0)
    total_score_7 = models.IntegerField(default=0)
    grade_7 = models.CharField(max_length=3, default='nil')
    course_code_8 = models.CharField(max_length=50, default='nil')
    course_title_8 = models.CharField(max_length=200, default='nil')
    course_8_credit_load = models.IntegerField(default=0)
    attendance_score_8 = models.IntegerField(default=0)
    inception_quiz_score_8 = models.IntegerField(default=0)
    midsemester_test_score_8 = models.IntegerField(default=0)
    exam_score_8 = models.IntegerField(default=0)
    total_score_8 = models.IntegerField(default=0)
    grade_8 = models.CharField(max_length=3, default='nil')
    course_code_9 = models.CharField(max_length=50, default='nil')
    course_title_9 = models.CharField(max_length=200, default='nil')
    course_9_credit_load = models.IntegerField(default=0)
    attendance_score_9 = models.IntegerField(default=0)
    inception_quiz_score_9 = models.IntegerField(default=0)
    midsemester_test_score_9 = models.IntegerField(default=0)
    exam_score_9 = models.IntegerField(default=0)
    total_score_9 = models.IntegerField(default=0)
    grade_9 = models.CharField(max_length=3, default='nil')
    course_code_10 = models.CharField(max_length=50, default='nil')
    course_title_10 = models.CharField(max_length=200, default='nil')
    course_10_credit_load = models.IntegerField(default=0)
    attendance_score_10 = models.IntegerField(default=0)
    inception_quiz_score_10 = models.IntegerField(default=0)
    midsemester_test_score_10 = models.IntegerField(default=0)
    exam_score_10 = models.IntegerField(default=0)
    total_score_10 = models.IntegerField(default=0)
    grade_10 = models.CharField(max_length=3, default='nil')
    course_code_11 = models.CharField(max_length=50, default='nil')
    course_title_11 = models.CharField(max_length=200, default='nil')
    course_11_credit_load = models.IntegerField(default=0)
    attendance_score_11 = models.IntegerField(default=0)
    inception_quiz_score_11 = models.IntegerField(default=0)
    midsemester_test_score_11 = models.IntegerField(default=0)
    exam_score_11 = models.IntegerField(default=0)
    total_score_11 = models.IntegerField(default=0)
    grade_11 = models.CharField(max_length=3, default='nil')
    course_code_12 = models.CharField(max_length=50, default='nil')
    course_title_12 = models.CharField(max_length=200, default='nil')
    course_12_credit_load = models.IntegerField(default=0)
    attendance_score_12 = models.IntegerField(default=0)
    inception_quiz_score_12 = models.IntegerField(default=0)
    midsemester_test_score_12 = models.IntegerField(default=0)
    exam_score_12 = models.IntegerField(default=0)
    total_score_12 = models.IntegerField(default=0)
    grade_12 = models.CharField(max_length=3, default='nil')
    course_code_13 = models.CharField(max_length=50, default='nil')
    course_title_13 = models.CharField(max_length=200, default='nil')
    course_13_credit_load = models.IntegerField(default=0)
    attendance_score_13 = models.IntegerField(default=0)
    inception_quiz_score_13 = models.IntegerField(default=0)
    midsemester_test_score_13 = models.IntegerField(default=0)
    exam_score_13 = models.IntegerField(default=0)
    total_score_13 = models.IntegerField(default=0)
    grade_13 = models.CharField(max_length=3, default='nil')
    gpa = models.DecimalField(default=0, max_digits=10, decimal_places=1)
    average_score = models.DecimalField(default=0, max_digits=10, decimal_places=1)


    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.total_score_1 = self.attendance_score_1 + self.inception_quiz_score_1 + self.midsemester_test_score_1 + self.exam_score_1
        self.total_score_2 = self.attendance_score_2 + self.inception_quiz_score_2 + self.midsemester_test_score_2 + self.exam_score_2
        self.total_score_3 = self.attendance_score_3 + self.inception_quiz_score_3 + self.midsemester_test_score_3 + self.exam_score_3
        self.total_score_4 = self.attendance_score_4 + self.inception_quiz_score_4 + self.midsemester_test_score_4 + self.exam_score_4
        self.total_score_5 = self.attendance_score_5 + self.inception_quiz_score_5 + self.midsemester_test_score_5 + self.exam_score_5
        self.total_score_6 = self.attendance_score_6 + self.inception_quiz_score_6 + self.midsemester_test_score_6 + self.exam_score_6
        self.total_score_7 = self.attendance_score_7 + self.inception_quiz_score_7 + self.midsemester_test_score_7 + self.exam_score_7
        self.total_score_8 = self.attendance_score_8 + self.inception_quiz_score_8 + self.midsemester_test_score_8 + self.exam_score_8
        self.total_score_9 = self.attendance_score_9 + self.inception_quiz_score_9 + self.midsemester_test_score_9 + self.exam_score_9
        self.total_score_10 = self.attendance_score_10 + self.inception_quiz_score_10 + self.midsemester_test_score_10 + self.exam_score_10
        self.total_score_11 = self.attendance_score_11 + self.inception_quiz_score_11 + self.midsemester_test_score_11 + self.exam_score_11
        self.total_score_12 = self.attendance_score_12 + self.inception_quiz_score_12 + self.midsemester_test_score_12 + self.exam_score_12
        self.total_score_13 = self.attendance_score_13 + self.inception_quiz_score_13 + self.midsemester_test_score_13 + self.exam_score_13

        
        if self.course_code_1 != 'nil':
            self.average_score = self.total_score_1/1
        if self.course_code_2 != 'nil':
            self.average_score = self.total_score_2 + self.total_score_1 / 2
        if self.course_code_3 != 'nil':
            self.average_score = self.total_score_3 + self.total_score_2 + self.total_score_3 / 3
        if self.course_code_4 != 'nil':
            self.average_score = self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 4
        if self.course_code_5 != 'nil':
            self.average_score = self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 5
        if self.course_code_6 != 'nil':
            self.average_score = self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 6
        if self.course_code_7 != 'nil':
            self.average_score = self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 7
        if self.course_code_8 != 'nil':
            self.average_score = self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 8
        if self.course_code_9 != 'nil':
            self.average_score = self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 9
        if self.course_code_10 != 'nil':
            self.average_score = self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 10
        if self.course_code_11 != 'nil':
            self.average_score = self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 11
        if self.course_code_12 != 'nil':
            self.average_score = self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 12
        if self.course_code_13 != 'nil':
            self.average_score = self.total_score_13 + self.total_score_12 + self.total_score_11 + self.total_score_10 + self.total_score_9 + self.total_score_8 + self.total_score_7 + self.total_score_6 + self.total_score_5 + self.total_score_4 + self.total_score_3 + self.total_score_2 + self.total_score_1 / 13
        


        load_1 = 0
        if self.total_score_1 >= 70 and self.total_score_1 <= 100:
            self.grade_1 = 'A'
            load_1 += 5 * self.course_1_credit_load
        elif self.total_score_1 >= 60 and self.total_score_1 <= 69:
            self.grade_1 = 'B'
            load_1 += 4 * self.course_1_credit_load
        elif self.total_score_1 >= 50 and self.total_score_1 <= 59:
            self.grade_1 = 'C'
            load_1 += 3 * self.course_1_credit_load
        elif self.total_score_1 >= 45 and self.total_score_1 <= 49:
            self.grade_1 = 'D'
            load_1 += 2 * self.course_1_credit_load
        elif self.total_score_1 >= 44 and self.total_score_1 <= 40:
            self.grade_1 = 'E'
            load_1 += 1 * self.course_1_credit_load
        else:
            self.grade_1 = 'F'
            load_1 += 0 * self.course_1_credit_load


        load_2 = 0
        if self.total_score_2 >= 70 and self.total_score_2 <= 100:
            self.grade_2 = 'A'
            load_2 += 5 * self.course_2_credit_load
        elif self.total_score_2 >= 60 and self.total_score_2 <= 69:
            self.grade_2 = 'B'
            load_2 += 4 * self.course_2_credit_load
        elif self.total_score_2 >= 50 and self.total_score_2 <= 59:
            self.grade_2 = 'C'
            load_2 += 3 * self.course_2_credit_load
        elif self.total_score_2 >= 45 and self.total_score_2 <= 49:
            self.grade_2 = 'D'
            load_2 += 2 * self.course_2_credit_load
        elif self.total_score_2 >= 44 and self.total_score_2 <= 40:
            self.grade_2 = 'E'
            load_2 += 1 * self.course_2_credit_load
        else:
            self.grade_2 = 'F'
            load_2 += 0 * self.course_2_credit_load

        
        load_3 = 0
        if self.total_score_3 >= 70 and self.total_score_3 <= 100:
            self.grade_3 = 'A'
            load_3 += 5 * self.course_3_credit_load
        elif self.total_score_3 >= 60 and self.total_score_3 <= 69:
            self.grade_3 = 'B'
            load_3 += 4 * self.course_3_credit_load
        elif self.total_score_3 >= 50 and self.total_score_3 <= 59:
            self.grade_3 = 'C'
            load_3 += 3 * self.course_3_credit_load
        elif self.total_score_3 >= 45 and self.total_score_3 <= 49:
            self.grade_3 = 'D'
            load_3 += 2 * self.course_3_credit_load
        elif self.total_score_3 >= 44 and self.total_score_3 <= 40:
            self.grade_3 = 'E'
            load_3 += 1 * self.course_3_credit_load
        else:
            self.grade_3 = 'F'
            load_3 += 0 * self.course_3_credit_load


        load_4 = 0
        if self.total_score_4 >= 70 and self.total_score_4 <= 100:
            self.grade_4 = 'A'
            load_4 += 5 * self.course_4_credit_load
        elif self.total_score_4 >= 60 and self.total_score_4 <= 69:
            self.grade_4 = 'B'
            load_4 += 4 * self.course_4_credit_load
        elif self.total_score_4 >= 50 and self.total_score_4 <= 59:
            self.grade_4 = 'C'
            load_4 += 3 * self.course_4_credit_load
        elif self.total_score_4 >= 45 and self.total_score_4 <= 49:
            self.grade_4 = 'D'
            load_4 += 2 * self.course_4_credit_load
        elif self.total_score_4 >= 44 and self.total_score_4 <= 40:
            self.grade_4 = 'E'
            load_4 += 1 * self.course_4_credit_load
        else:
            self.grade_4 = 'F'
            load_4 += 0 * self.course_4_credit_load


        load_5 = 0
        if self.total_score_5 >= 70 and self.total_score_5 <= 100:
            self.grade_5 = 'A'
            load_5 += 5 * self.course_5_credit_load
        elif self.total_score_5 >= 60 and self.total_score_5 <= 69:
            self.grade_5 = 'B'
            load_5 += 4 * self.course_5_credit_load
        elif self.total_score_5 >= 50 and self.total_score_5 <= 59:
            self.grade_5 = 'C'
            load_5 += 3 * self.course_5_credit_load
        elif self.total_score_5 >= 45 and self.total_score_5 <= 49:
            self.grade_5 = 'D'
            load_5 += 2 * self.course_5_credit_load
        elif self.total_score_5 >= 44 and self.total_score_5 <= 40:
            self.grade_5 = 'E'
            load_5 += 1 * self.course_5_credit_load
        else:
            self.grade_5 = 'F'
            load_5 += 0 * self.course_5_credit_load
        

        load_6 = 0
        if self.total_score_6 >= 70 and self.total_score_6 <= 100:
            self.grade_6 = 'A'
            load_6 += 5 * self.course_6_credit_load
        elif self.total_score_6 >= 60 and self.total_score_6 <= 69:
            self.grade_6 = 'B'
            load_6 += 4 * self.course_6_credit_load
        elif self.total_score_6 >= 50 and self.total_score_6 <= 59:
            self.grade_6 = 'C'
            load_6 += 3 * self.course_6_credit_load
        elif self.total_score_6 >= 45 and self.total_score_6 <= 49:
            self.grade_6 = 'D'
            load_6 += 2 * self.course_6_credit_load
        elif self.total_score_6 >= 44 and self.total_score_6 <= 40:
            self.grade_6 = 'E'
            load_6 += 1 * self.course_6_credit_load
        else:
            self.grade_6 = 'F'
            load_6 += 0 * self.course_6_credit_load

        
        load_7 = 0
        if self.total_score_7 >= 70 and self.total_score_7 <= 100:
            self.grade_7 = 'A'
            load_7 += 5 * self.course_7_credit_load
        elif self.total_score_7 >= 60 and self.total_score_7 <= 69:
            self.grade_7 = 'B'
            load_7 += 4 * self.course_7_credit_load
        elif self.total_score_7 >= 50 and self.total_score_7 <= 59:
            self.grade_7 = 'C'
            load_7 += 3 * self.course_7_credit_load
        elif self.total_score_7 >= 45 and self.total_score_7 <= 49:
            self.grade_7 = 'D'
            load_7 += 2 * self.course_7_credit_load
        elif self.total_score_7 >= 44 and self.total_score_7 <= 40:
            self.grade_7 = 'E'
            load_7 += 1 * self.course_7_credit_load
        else:
            self.grade_7 = 'F'
            load_7 += 0 * self.course_7_credit_load

        
        load_8 = 0
        if self.total_score_8 >= 70 and self.total_score_8 <= 100:
            self.grade_8 = 'A'
            load_8 += 5 * self.course_8_credit_load
        elif self.total_score_8 >= 60 and self.total_score_8 <= 69:
            self.grade_8 = 'B'
            load_8 += 4 * self.course_8_credit_load
        elif self.total_score_8 >= 50 and self.total_score_8 <= 59:
            self.grade_8 = 'C'
            load_8 += 3 * self.course_8_credit_load
        elif self.total_score_8 >= 45 and self.total_score_8 <= 49:
            self.grade_8 = 'D'
            load_8 += 2 * self.course_8_credit_load
        elif self.total_score_8 >= 44 and self.total_score_8 <= 40:
            self.grade_8 = 'E'
            load_8 += 1 * self.course_8_credit_load
        else:
            self.grade_8 = 'F'
            load_8 += 0 * self.course_8_credit_load

        
        load_9 = 0
        if self.total_score_9 >= 70 and self.total_score_9 <= 100:
            self.grade_9 = 'A'
            load_9 += 5 * self.course_9_credit_load
        elif self.total_score_9 >= 60 and self.total_score_9 <= 69:
            self.grade_9 = 'B'
            load_9 += 4 * self.course_9_credit_load
        elif self.total_score_9 >= 50 and self.total_score_9 <= 59:
            self.grade_9 = 'C'
            load_9 += 3 * self.course_9_credit_load
        elif self.total_score_9 >= 45 and self.total_score_9 <= 49:
            self.grade_9 = 'D'
            load_9 += 2 * self.course_9_credit_load
        elif self.total_score_9 >= 44 and self.total_score_9 <= 40:
            self.grade_9 = 'E'
            load_9 += 1 * self.course_9_credit_load
        else:
            self.grade_9 = 'F'
            load_9 += 0 * self.course_9_credit_load


        load_10 = 0
        if self.total_score_10 >= 70 and self.total_score_10 <= 100:
            self.grade_10 = 'A'
            load_10 += 5 * self.course_10_credit_load
        elif self.total_score_10 >= 60 and self.total_score_10 <= 69:
            self.grade_10 = 'B'
            load_10 += 4 * self.course_10_credit_load
        elif self.total_score_10 >= 50 and self.total_score_10 <= 59:
            self.grade_10 = 'C'
            load_10 += 3 * self.course_10_credit_load
        elif self.total_score_10 >= 45 and self.total_score_10 <= 49:
            self.grade_10 = 'D'
            load_10 += 2 * self.course_10_credit_load
        elif self.total_score_10 >= 44 and self.total_score_10 <= 40:
            self.grade_10 = 'E'
            load_10 += 1 * self.course_10_credit_load
        else:
            self.grade_10 = 'F'
            load_10 += 0 * self.course_10_credit_load

        
        load_11 = 0
        if self.total_score_11 >= 70 and self.total_score_11 <= 100:
            self.grade_11 = 'A'
            load_11 += 5 * self.course_11_credit_load
        elif self.total_score_11 >= 60 and self.total_score_11 <= 69:
            self.grade_11 = 'B'
            load_11 += 4 * self.course_11_credit_load
        elif self.total_score_11 >= 50 and self.total_score_11 <= 59:
            self.grade_11 = 'C'
            load_11 += 3 * self.course_11_credit_load
        elif self.total_score_11 >= 45 and self.total_score_11 <= 49:
            self.grade_11 = 'D'
            load_11 += 2 * self.course_11_credit_load
        elif self.total_score_11 >= 44 and self.total_score_11 <= 40:
            self.grade_11 = 'E'
            load_11 += 1 * self.course_11_credit_load
        else:
            self.grade_11 = 'F'
            load_11 += 0 * self.course_11_credit_load

        
        load_12 = 0
        if self.total_score_12 >= 70 and self.total_score_12 <= 100:
            self.grade_12 = 'A'
            load_12 += 5 * self.course_12_credit_load
        elif self.total_score_12 >= 60 and self.total_score_12 <= 69:
            self.grade_12 = 'B'
            load_12 += 4 * self.course_12_credit_load
        elif self.total_score_12 >= 50 and self.total_score_12 <= 59:
            self.grade_12 = 'C'
            load_12 += 3 * self.course_12_credit_load
        elif self.total_score_12 >= 45 and self.total_score_12 <= 49:
            self.grade_12 = 'D'
            load_12 += 2 * self.course_12_credit_load
        elif self.total_score_12 >= 44 and self.total_score_12 <= 40:
            self.grade_12 = 'E'
            load_12 += 1 * self.course_12_credit_load
        else:
            self.grade_12 = 'F'
            load_12 += 0 * self.course_12_credit_load

        
        load_13 = 0
        if self.total_score_13 >= 70 and self.total_score_13 <= 100:
            self.grade_13 = 'A'
            load_13 += 5 * self.course_13_credit_load
        elif self.total_score_13 >= 60 and self.total_score_13 <= 69:
            self.grade_13 = 'B'
            load_13 += 4 * self.course_13_credit_load
        elif self.total_score_13 >= 50 and self.total_score_13 <= 59:
            self.grade_13 = 'C'
            load_13 += 3 * self.course_13_credit_load
        elif self.total_score_13 >= 45 and self.total_score_13 <= 49:
            self.grade_13 = 'D'
            load_13 += 2 * self.course_13_credit_load
        elif self.total_score_13 >= 44 and self.total_score_13 <= 40:
            self.grade_13 = 'E'
            load_13 += 1 * self.course_13_credit_load
        else:
            self.grade_13 = 'F'
            load_13 += 0 * self.course_13_credit_load


        gpa = load_13 + load_12 + load_11 + load_10 + load_9 + load_8 + load_7 + load_6 + load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load + self.course_6_credit_load + self.course_7_credit_load + self.course_8_credit_load + self.course_9_credit_load + self.course_10_credit_load + self.course_11_credit_load + + self.course_12_credit_load + + self.course_13_credit_load
        self.gpa = gpa/total_credit_load
        super().save(*args, **kwargs)



class InfoCenter(models.Model):
    DEPARTMENT = (
        ('Computer science', 'Computer science'),
        ('Mathematics', 'Mathematics'),
        ('Statistics', 'Statistics')
    )
    LEVEL = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )
    department = models.CharField(max_length=225, choices=DEPARTMENT)
    level = models.CharField(max_length=20, default='', choices=LEVEL)
    heading = models.CharField(max_length=225)
    message = models.TextField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class GeneralInfo(models.Model):
    heading = models.CharField(max_length=225)
    message = models.TextField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)