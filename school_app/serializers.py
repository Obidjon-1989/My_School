from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherSerialazer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields="__all__"

class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields="__all__"

