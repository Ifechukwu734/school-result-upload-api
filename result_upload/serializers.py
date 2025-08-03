from rest_framework import serializers
from .models import CustomUser, ComputerScience100Level, InfoCenter, ComputerScience200Level, ComputerScience300Level, ComputerScience400Level
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    
    class Meta:
        model = CustomUser
        fields = [ 'email', 'first_name', 'last_name', 'matric_number', 'phone_number', 'department', 'level', 'profile_image']
        read_only_fields = ['email']
    
    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.profile_image.url) if obj.profile_image and request else None 
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if isinstance(value, list) and len(value) == 1:
                validated_data[key] = value[0]
        return super().update(instance, validated_data)     
    


class ComputerScience100LevlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputerScience100Level
        fields = ['semester', 'session', 'course_code_1', 'course_title_1', 'course_1_credit_load', 'attendance_score_1', 'inception_quiz_score_1', 'midsemester_test_score_1', 'exam_score_1', 'total_score_1', 'grade_1', 
                  'course_code_2',  'course_title_2', 'course_2_credit_load', 'attendance_score_2', 'inception_quiz_score_2', 'midsemester_test_score_2', 'exam_score_2', 'total_score_2', 'grade_2',  
                  'course_code_3',  'course_title_3', 'course_3_credit_load', 'attendance_score_3', 'inception_quiz_score_3', 'midsemester_test_score_3', 'exam_score_3', 'total_score_3', 'grade_3',
                    'course_code_4', 'course_title_4', 'course_4_credit_load', 'attendance_score_4', 'inception_quiz_score_4', 'midsemester_test_score_4', 'exam_score_4', 'total_score_4', 'grade_4',
                     'course_code_5', 'course_title_5', 'course_title_5', 'course_5_credit_load', 'attendance_score_5', 'inception_quiz_score_5', 'midsemester_test_score_5', 'exam_score_5', 'total_score_5', 'grade_5',
                     'average_score', 'gpa']



class ComputerScience200LevlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputerScience200Level
        fields = ['semester', 'session', 'course_code_1', 'course_title_1', 'course_1_credit_load', 'attendance_score_1', 'inception_quiz_score_1', 'midsemester_test_score_1', 'exam_score_1', 'total_score_1', 'grade_1', 
                  'course_code_2',  'course_title_2', 'course_2_credit_load', 'attendance_score_2', 'inception_quiz_score_2', 'midsemester_test_score_2', 'exam_score_2', 'total_score_2', 'grade_2',  
                  'course_code_3',  'course_title_3', 'course_3_credit_load', 'attendance_score_3', 'inception_quiz_score_3', 'midsemester_test_score_3', 'exam_score_3', 'total_score_3', 'grade_3',
                    'course_code_4', 'course_title_4', 'course_4_credit_load', 'attendance_score_4', 'inception_quiz_score_4', 'midsemester_test_score_4', 'exam_score_4', 'total_score_4', 'grade_4',
                     'course_code_5', 'course_title_5', 'course_title_5', 'course_5_credit_load', 'attendance_score_5', 'inception_quiz_score_5', 'midsemester_test_score_5', 'exam_score_5', 'total_score_5', 'grade_5',
                     'average_score', 'gpa']


class ComputerScience300LevlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputerScience300Level
        fields = ['semester',  'session', 'course_code_1', 'course_title_1', 'course_1_credit_load', 'attendance_score_1', 'inception_quiz_score_1', 'midsemester_test_score_1', 'exam_score_1', 'total_score_1', 'grade_1', 
                  'course_code_2',  'course_title_2', 'course_2_credit_load', 'attendance_score_2', 'inception_quiz_score_2', 'midsemester_test_score_2', 'exam_score_2', 'total_score_2', 'grade_2',  
                  'course_code_3',  'course_title_3', 'course_3_credit_load', 'attendance_score_3', 'inception_quiz_score_3', 'midsemester_test_score_3', 'exam_score_3', 'total_score_3', 'grade_3',
                    'course_code_4', 'course_title_4', 'course_4_credit_load', 'attendance_score_4', 'inception_quiz_score_4', 'midsemester_test_score_4', 'exam_score_4', 'total_score_4', 'grade_4',
                     'course_code_5', 'course_title_5', 'course_title_5', 'course_5_credit_load', 'attendance_score_5', 'inception_quiz_score_5', 'midsemester_test_score_5', 'exam_score_5', 'total_score_5', 'grade_5',
                     'average_score', 'gpa']



class ComputerScience400LevlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputerScience400Level
        fields = ['semester', 'session', 'course_code_1', 'course_title_1', 'course_1_credit_load', 'attendance_score_1', 'inception_quiz_score_1', 'midsemester_test_score_1', 'exam_score_1', 'total_score_1', 'grade_1', 
                  'course_code_2',  'course_title_2', 'course_2_credit_load', 'attendance_score_2', 'inception_quiz_score_2', 'midsemester_test_score_2', 'exam_score_2', 'total_score_2', 'grade_2',  
                  'course_code_3',  'course_title_3', 'course_3_credit_load', 'attendance_score_3', 'inception_quiz_score_3', 'midsemester_test_score_3', 'exam_score_3', 'total_score_3', 'grade_3',
                    'course_code_4', 'course_title_4', 'course_4_credit_load', 'attendance_score_4', 'inception_quiz_score_4', 'midsemester_test_score_4', 'exam_score_4', 'total_score_4', 'grade_4',
                     'course_code_5', 'course_title_5', 'course_title_5', 'course_5_credit_load', 'attendance_score_5', 'inception_quiz_score_5', 'midsemester_test_score_5', 'exam_score_5', 'total_score_5', 'grade_5',
                     'average_score', 'gpa']




class InfoCenterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InfoCenter
        fields = ['heading', 'message']