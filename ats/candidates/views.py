from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Candidate
from .serializsers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
