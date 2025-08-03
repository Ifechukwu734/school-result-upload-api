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

        total = self.total_score_1 + self.total_score_2 + self.total_score_3 + self.total_score_4 + self.total_score_5
        self.average_score = total/5

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

        gpa = load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load
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

        total = self.total_score_1 + self.total_score_2 + self.total_score_3 + self.total_score_4 + self.total_score_5
        self.average_score = total/5

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

        gpa = load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load
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

        total = self.total_score_1 + self.total_score_2 + self.total_score_3 + self.total_score_4 + self.total_score_5
        self.average_score = total/5

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

        gpa = load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load
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

        total = self.total_score_1 + self.total_score_2 + self.total_score_3 + self.total_score_4 + self.total_score_5
        self.average_score = total/5

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

        gpa = load_5 + load_4 + load_3 + load_2 + load_1
        total_credit_load = self.course_1_credit_load + self.course_2_credit_load + self.course_3_credit_load + self.course_4_credit_load + self.course_5_credit_load
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