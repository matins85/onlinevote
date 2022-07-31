#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
↓↓...........................................................................↓↓
↓↓..........................↓↓↓↓↓↓↓↓↓↓↓↓↓....................................↓↓
↓↓.......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................................↓↓
↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...↓↓↓.............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓.....↓↓↓↓↓↓↓↓↓............................↓↓
↓↓......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..↓↓↓↓↓↓↓............................↓↓
↓↓...................................↓↓↓.....................................↓↓
↓↓.................↓↓................↓↓↓↓ ↓↓↓↓↓↓↓........↓...................↓↓
↓↓...............↓↓↓↓↓↓..............↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓..↓↓↓↓↓.........................↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓...↓↓↓↓↓↓↓....................↓↓↓↓↓↓.↓↓.↓↓.................↓↓
↓↓...............↓↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓..........................↓↓
↓↓.........................↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓↓...............................↓↓
↓↓..............................↓↓↓↓↓↓↓↓↓↓...................................↓↓
↓↓..........................↓↓↓↓↓....↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓............↓↓.↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓.↓↓..↓↓↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................↓↓
↓↓..............↓↓↓↓↓↓............................↓↓.↓↓↓↓↓↓↓.................↓↓
↓↓..................                                   ......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑ .......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑   ↑↑↑↑     ↑↑↑   ↑↑↑↑.....................↓↓
↓↓.................. ↑↑↨  ↑↑↑  ↑↑↨   ↨↑↑      ↑↑↨   ↨↑↑......................↓↓
↓↓.................. ↨↑↨  ↑↨↑  ↨↑↨   ↨↑↨      ↨↑↨   ↨↑↨......................↓↓
↓↓.................. ↑↨↑  ↨↑↨  ↨↨↑↨↑↨↨↑↑↨     ↨↨↑↨↑↨↨↑↑↨.....................↓↓
↓↓.................. ↨↑↨  ↨↨↨  ↨↨↨      ↨↨↨   ↨↨↨     ↨↨↨....................↓↓
↓↓.................. :↨:  ↨↨:  ↨↨:      :↨↨   ↨↨:     :::....................↓↓
↓↓................... ::↨↨:↨   :↨:      :↨:   :↨:     :::....................↓↓
↓↓.................... ::::    :::      :::   :::     :::....................↓↓
↓↓...................... :      :        :      :::::::  ....................↓↓
↓↓...........................................................................↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓      serializers.py  Created by  Olorunshola Matins 2022                  ↓↓
↓↓            Personal Email : <olorunsholamatins@gmail.com>                 ↓↓
↓↓                 Telephone Number: +2348117039368                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓


"""
# Django framework Imports
from rest_framework.authtoken.models import Token
from rest_framework import serializers
# Rest Auth Imports
from rest_auth.serializers import LoginSerializer
# Django Imports
from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
# Account Import
from accounts.models import Year, RegisteredVoters, Department, School

UserModel = get_user_model()
token_model = Token
year_model = Year
voters_model = RegisteredVoters
department_model = Department
school_model = School


class OnlinevoteUserDetailSerializer(serializers.ModelSerializer):
    """ Serializer for Get User detail Endpoint """

    class Meta:
        model = UserModel
        exclude = ('password', 'groups', 'user_permissions', 'is_superuser',)


class OnlinevoteLoginSerializer(LoginSerializer):
    """ Serializer for Login user Endpoint """

    username = None


class OnlinevotersLoginSerializer(serializers.Serializer):
    """ Serializer for Login Voters Endpoint """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class YearSerializer(serializers.ModelSerializer):
    """ Serializer for Year Endpoint """

    class Meta:
        model = year_model
        fields = "__all__"


class SchoolSerializer2(serializers.ModelSerializer):
    """ Serializer for Department Serializer """

    class Meta:
        model = school_model
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """ Serializer for Department Endpoint """

    school = SchoolSerializer2()

    class Meta:
        model = department_model
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    """ Serializer for School Endpoint """

    departments = DepartmentSerializer(required=False, source="departments", many=True)

    class Meta:
        model = school_model
        fields = ['id', 'school', 'departments']


class VotersDetailSerializer(serializers.ModelSerializer):
    """ Serializer for School Endpoint """

    department = DepartmentSerializer()
    year = YearSerializer()

    class Meta:
        model = voters_model
        fields = "__all__"


class VotersCreateSerializer(serializers.ModelSerializer):
    """ serializer for Create Voters Endpoint """

    year = serializers.PrimaryKeyRelatedField(required=True, queryset=year_model.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=True, queryset=department_model.objects.all())
    profile = Base64ImageField(required=True)

    class Meta:
        model = voters_model
        fields = "__all__"

    def create(self, validated_data):
        add_voters = voters_model.objects.create(**self.validated_data)
        add_voters.save()
        return add_voters


class VotersUpdateSerializer(serializers.ModelSerializer):
    """ serializer for Update Voters Endpoint """

    year = serializers.PrimaryKeyRelatedField(required=False, queryset=year_model.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=False, queryset=department_model.objects.all())
    profile = Base64ImageField(required=False)

    class Meta:
        model = voters_model
        fields = "__all__"
        extra_kwargs = {'name': {'required': False}, 'profile': {'required': False}, 'year': {'required': False},
                        'department': {'required': False}, 'matric': {'required': False},
                        'email': {'required': False}}

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.year = validated_data.get('year', instance.year)
        instance.department = validated_data.get('department', instance.department)
        instance.matric = validated_data.get('matric', instance.matric)
        instance.verified_voter = validated_data.get('verified_voter', instance.verified_voter)
        instance.aspirant = validated_data.get('aspirant', instance.aspirant)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance
