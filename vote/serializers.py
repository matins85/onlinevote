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

# Rest Imports
from rest_framework import serializers
# Accounts Serializer
from accounts.models import Year, Department, RegisteredVoters
from accounts.serializers import (DepartmentSerializer, YearSerializer, VotersDetailSerializer, PositionSerializer)
# Vote Imports
from .models import VoteModel, VotersModel
# Python Import
import datetime

vote_model = VoteModel
voters_model = VotersModel
year_model = Year
department_model = Department
registered_model = RegisteredVoters


class VoteListSerializer(serializers.ModelSerializer):
    """ Serializer for List Vote Endpoint """

    year = YearSerializer()
    department = DepartmentSerializer()
    details = PositionSerializer(required=False, source='aspirant', many=True)

    class Meta:
        model = vote_model
        fields = ['id', 'start', 'year', 'department', 'details']


class VotersListSerializer(serializers.ModelSerializer):
    """ Serializer for List Voters Endpoint """

    year = YearSerializer()
    department = DepartmentSerializer()
    choice = VotersDetailSerializer()

    class Meta:
        model = voters_model
        fields = "__all__"


class VoteCreateSerializer(serializers.ModelSerializer):
    """ Serializer for Create Voters Endpoint """

    year = serializers.PrimaryKeyRelatedField(required=True, queryset=year_model.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=True, queryset=department_model.objects.all())

    class Meta:
        model = vote_model
        fields = "__all__"

    def create(self, validated_data):
        add_vote = vote_model.objects.create(**validated_data)
        add_vote.save()
        return add_vote

    def update(self, instance, validated_data):
        instance.year = validated_data.get('year', instance.year)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance


class VotersCreateSerializer(serializers.ModelSerializer):
    """ Serializer for Create Voters Endpoint """

    year = serializers.PrimaryKeyRelatedField(required=True, queryset=year_model.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=True, queryset=department_model.objects.all())
    choice = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=registered_model.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(required=True, queryset=registered_model.objects.all())

    class Meta:
        model = voters_model
        fields = "__all__"

    def create(self, validated_data):
        year = year_model.objects.get(id=validated_data['year'])
        created_by = registered_model.objects.get(id=validated_data['created_by'])
        department = department_model.objects.get(id=validated_data['department'])

        if int(year.year) != int(datetime.date.today().year):
            raise serializers.ValidationError({"detail": "Cannot vote for the selected year"})
        elif voters_model.objects.filter(created_by=created_by, year=year).exists():
            raise serializers.ValidationError({"detail": "Already voted!"})
        else:
            save_list = [voters_model(year=year, department=department,
                                      choice=registered_model.objects.get(id=row),
                                      created_by=created_by) for row in validated_data['choice']]
            voters_model.objects.bulk_create(save_list)
        return dict()
