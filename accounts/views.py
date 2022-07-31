from builtins import super
# Python Import
import datetime
# Django Allauth Imports #
from allauth.account.signals import email_confirmed
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# Django Imports #
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Rest-Auth Imports #
from rest_auth.registration.views import SocialLoginView
from rest_auth.views import LoginView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Accounts Import
from accounts.permission import IdentityIsVerified
from accounts.serializers import OnlinevoteUserDetailSerializer, YearSerializer, VotersCreateSerializer, \
    VotersDetailSerializer, VotersUpdateSerializer, DepartmentSerializer
from accounts.models import Year, RegisteredVoters, Department, School
from accounts.utils import year_choices

UserModel = get_user_model()
year_model = Year
voters_model = RegisteredVoters
department_model = Department
school_model = School


@api_view()
def django_rest_auth_null():
    return Response(status=status.HTTP_400_BAD_REQUEST)


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    user.email_verified = True
    user.save()


class UserLoginView(LoginView):
    """ Login Endpoint """

    def get_response(self):
        response = super().get_response()
        data = {"message": "Welcome {}".format(self.user), "code": response.status_code, "user_id": self.user.id,
                "staff": self.user.is_staff}
        response.data.update(data)
        return response


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class OnlinevoteUserProfileView(APIView):
    """ Get User Profile Endpoint """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = OnlinevoteUserDetailSerializer

    def get(self, request):
        queryset = UserModel.objects.get(pk=self.request.user.id)
        data = self.serializer_class(queryset)
        return Response(data.data)


class ListVotersView(ListAPIView):
    """ Endpoint for List all Voters """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = voters_model.objects.filter()
    serializer_class = VotersDetailSerializer

    def get(self, request, *args, **kwargs):
        self.get_object()
        queryset = voters_model.objects.filter(aspirant=False, year=self.kwargs['pk'])
        data = self.serializer_class(queryset, many=True)
        return Response(data.data)


class ListAspirantView(ListAPIView):
    """ Endpoint for List all Aspirant Candidate """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = voters_model.objects.filter()
    serializer_class = VotersDetailSerializer

    def get(self, request, *args, **kwargs):
        self.get_object()
        queryset = voters_model.objects.filter(aspirant=True, year=self.kwargs['pk'])
        data = self.serializer_class(queryset, many=True)
        return Response(data.data)


class VotersCreateView(CreateAPIView):
    """ Endpoint for Create Voter """

    queryset = voters_model.objects.all()
    serializer_class = VotersCreateSerializer
    serializer_class2 = VotersDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_voters = self.create(request, *args, **kwargs)
        data = self.serializer_class2(voters_model.objects.get(id=new_voters.data['id']))
        return Response(data.data)


class VotersUpdateView(RetrieveUpdateAPIView):
    """ Endpoint for Update Voter """

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, IdentityIsVerified,)
    queryset = voters_model.objects.all()
    serializer_class = VotersUpdateSerializer
    serializer_class2 = VotersDetailSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.update(request, *args, **kwargs)
        data = self.serializer_class2(voters_model.objects.get(id=instance.id))
        return Response(data.data)


class ListYearDeptView(ListAPIView):
    """ List All Years and Department Endpoint """

    queryset = year_model.objects.all()
    serializer_class = YearSerializer
    serializer_class2 = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        obj = year_model.objects.filter(year=datetime.date.today().year - 1)
        if obj.exists():
            if not year_model.objects.filter(year=datetime.date.today().year).exists():
                year_model.objects.create(year=datetime.date.today().year).save()
            queryset = self.serializer_class(year_model.objects.all(), many=True)
            queryset2 = self.serializer_class2(department_model.objects.all(), many=True)
            return Response({'years': queryset.data, 'department': queryset2.data})
        else:
            add_year = [year_model(year=year['year']) for year in year_choices()]
            year_model.objects.bulk_create(add_year)
            queryset = self.serializer_class(year_model.objects.all(), many=True)
            queryset2 = self.serializer_class2(department_model.objects.all(), many=True)
            return Response({'years': queryset.data, 'department': queryset2.data})


# class MelinaStatView(APIView):
#     """ Melina Statistics Endpoint """
#
#     authentication_classes = [TokenAuthentication]
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         queryset = [{
#             "user": {
#                 "total_users": UserModel.objects.all().count(),
#                 "active_users": UserModel.objects.filter(is_active=True).count(),
#                 "deactivated_users": UserModel.objects.filter(is_active=False).count()
#             },
#             "roles": {
#                 # "total_roles": group_model.objects.all().count(),
#                 "deleted_roles": audit_model.objects.filter(audit_type="role", subject="delete role").count()
#             },
#         }]
#         return Response(queryset)


def index(request):
    return HttpResponse("Welcome to ONLINE VOTING Server API Page")
