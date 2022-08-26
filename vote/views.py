# Django Imports #
# Django rest-framework Imports
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import recognize_face, save_image
# Account Imports
from accounts.permission import IdentityIsVerified
from accounts.models import Year, Department, RegisteredVoters
# Vote Import
from .serializers import VoteListSerializer, VoteCreateSerializer, VotersCreateSerializer, VotersDetailSerializer
from .models import VoteModel, VotersModel
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

vote_model = VoteModel
voters_model = VotersModel
year_model = Year
department_model = Department
registered_model = RegisteredVoters


class VoterLoginView(APIView):
    """ Endpoint for login """

    queryset = vote_model.objects.all()
    serializer_class = VotersDetailSerializer

    def post(self, request):
        try:
            query_set = registered_model.objects.get(matric=request.data['matric'])
            res = self.serializer_class(query_set)
            return Response(res.data)
        except registered_model.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class ListAspirantView(APIView):
    """ Endpoint for get list of aspirant for a department """

    queryset = vote_model.objects.all()

    def get(self, request):
        year = request.query_params.get('year', None)
        get_id = request.query_params.get('id', None)
        voters = voters_model.objects.filter(year__id=year).filter(department__id=get_id)
        print(voters)
        return Response({})


class CheckFaceView(APIView):
    """ Endpoint for recognize face """

    def post(self, request):
        image1 = request.data['image1']
        image2 = request.data['image2']
        save_img1 = save_image(image1)
        save_img2 = save_image(image2)
        recognize_face(os.path.join(base_dir, 'templates', save_img1),
                       os.path.join(base_dir, 'templates', save_img2))
        return Response({"detail": "success"})


class ListVoteView(ListAPIView):
    """ Endpoint for List Vote """

    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated, IdentityIsVerified,)
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


class VotersCreateView(APIView):
    """ Endpoint for Create Voter """

    queryset = voters_model.objects.all()
    serializer_class = VotersCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.serializer_class.create(request, serializer.data)
        return Response({"detail": "success"})
