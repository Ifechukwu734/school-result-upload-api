from django.shortcuts import render
from .models import ComputerScience100Level, ComputerScience200Level, InfoCenter, ComputerScience300Level, ComputerScience400Level
from .serializers import ComputerScience100LevlSerializer, InfoCenterSerializer, CustomUserSerializer, ComputerScience200LevlSerializer, ComputerScience300LevlSerializer, ComputerScience400LevlSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
# Create your views here.


class UserLoginView(APIView):
    
    def post(self, request):
        User = get_user_model()
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            serializer = CustomUserSerializer(user)
            data = {
                'token': token.key,
                'user': serializer.data
            }
            return Response(data, status=status.HTTP_302_FOUND)
        else:
            data = {
                'message': 'invalid credentials'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)



class CheckResultView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        level = request.data.get('level')
        semester = request.data.get('semester')
        if level == '100':
            result = ComputerScience100Level.objects.filter(student=user, semester=semester).first()
            if result:
                serializer = ComputerScience100LevlSerializer(result)
                user_serializer = CustomUserSerializer(user)
                data = {
                    'user': user_serializer.data,
                    'data': serializer.data,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'message': f'result for {semester} {level} level is not available'
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        elif level == '200':
            result = ComputerScience200Level.objects.filter(student=user, semester=semester).first()
            if result:
                serializer = ComputerScience200LevlSerializer(result)
                user_serializer = CustomUserSerializer(user)
                data = {
                    'user': user_serializer.data,
                    'data': serializer.data,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'message': f'result for {semester} {level} level is not available'
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        elif level == '300':
            result = ComputerScience300Level.objects.filter(student=user, semester=semester).first()
            if result:
                serializer = ComputerScience300LevlSerializer(result)
                user_serializer = CustomUserSerializer(user)
                data = {
                    'user': user_serializer.data,
                    'data': serializer.data,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'message': f'result for {semester} {level} level is not available'
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        elif level == '400':
            result = ComputerScience400Level.objects.filter(student=user, semester=semester).first()
            if result:
                serializer = ComputerScience400LevlSerializer(result)
                user_serializer = CustomUserSerializer(user)
                data = {
                    'user': user_serializer.data,
                    'data': serializer.data,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'message': f'result for {semester} {level} level is not available'
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data = {
                'message': 'please input a valid level'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        


class AverageChartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        average_chart = []
        total_cgpa_1 = 0
        cgpa_1 = 0
        year_one_average = ComputerScience100Level.objects.filter(student=user)
        if year_one_average:
            for items in year_one_average:
                average_chart.append(items.average_score)
                cgpa_1 += items.gpa
            if year_one_average.count() == 2:
                total_cgpa_1 += cgpa_1/2
            elif year_one_average.count() == 1:
                total_cgpa_1 += cgpa_1/1

        year_two_average = ComputerScience200Level.objects.filter(student=user)
        cgpa_2 = 0
        total_cgpa_2 = 0
        if year_two_average:
            for items in year_two_average:
                average_chart.append(items.average_score)
                cgpa_2 += items.gpa
            if year_two_average.count() == 2:
                total_cgpa_2 += cgpa_2/2
            elif year_two_average.count() == 1:
                total_cgpa_2 += cgpa_2/1

        year_three_average = ComputerScience300Level.objects.filter(student=user)
        cgpa_3 = 0
        total_cgpa_3 = 0
        if year_three_average:
            for items in year_three_average:
                average_chart.append(items.average_score)
                cgpa_3 += items.gpa
            if year_three_average.count() == 2:
                total_cgpa_3 += cgpa_3/2
            elif year_three_average.count() == 1:
                total_cgpa_3 += cgpa_3/1


        year_four_average = ComputerScience400Level.objects.filter(student=user)
        cgpa_4 = 0
        total_cgpa_4 = 0
        if year_four_average:
            for items in year_four_average:
                average_chart.append(items.average_score)
                cgpa_4 += items.gpa
            if year_four_average.count() == 2:
                total_cgpa_4 += cgpa_4/2
            elif year_four_average.count() == 1:
                total_cgpa_4 += cgpa_4/1


        data = {
            'data': average_chart,
            '100_level_cgpa': total_cgpa_1,
            '200_level_cgpa': total_cgpa_2,
            '300_level_cgpa': total_cgpa_3,
            '400_level_cgpa': total_cgpa_4,
        }
        return Response(data)


class ProfileDetailsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user =request.user
        serializer = CustomUserSerializer(user)
        data = {
            'user': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    

    def patch(self, request):
        user = request.user
        data = request.data.copy()
        data.pop('profile_image', None)
        image = request.FILES.getlist('profile_image')
        if image:
            image = image[0]
        serializer = CustomUserSerializer(user, data=data)

        if serializer.is_valid():
            if image:
                user.profile_image = image
                user.save()
            serializer.save()
            user_serializer = CustomUserSerializer(user)
            data = {
                'data': user_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InfoPageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        info = InfoCenter.objects.filter(level=user.level, department=user.department).order_by('-uploaded_at')
        serializer = InfoCenterSerializer(info, many=True)
        data = {
            'data': serializer.data
        }
        return Response(data)