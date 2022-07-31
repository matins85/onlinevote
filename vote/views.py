# Django Imports #
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Django rest-framework Imports
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
# Account Imports
from accounts.permission import IdentityIsVerified
from accounts.models import Year, Department, RegisteredVoters
# Vote Import
from .serializers import VoteListSerializer, VoteCreateSerializer, VotersCreateSerializer
from .models import VoteModel, VotersModel

vote_model = VoteModel
voters_model = VotersModel
year_model = Year
department_model = Department
registered_model = RegisteredVoters


class ListVoteView(ListAPIView):
    """ Endpoint for List Vote """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = vote_model.objects.all()
    serializer_class = VoteListSerializer


class VoteCreateView(CreateAPIView):
    """ Endpoint for Create Vote """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = vote_model.objects.all()
    serializer_class = VoteCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.create(request, *args, **kwargs)
        return Response(serializer.data)


class VoteUpdateView(RetrieveUpdateAPIView):
    """ Endpoint for Update Vote """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = vote_model.objects.all()
    serializer_class = VoteCreateSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class VotersCreateView(CreateAPIView):
    """ Endpoint for Create Voters """

    queryset = voters_model.objects.all()
    serializer_class = VotersCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.create(request, *args, **kwargs)
        return Response(serializer.data)
