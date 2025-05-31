from django.db.models import Case, IntegerField, Value, When
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Candidate
from .serializsers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=["get"])
    def search(self, request):
        """
        Custom Search endpoint
        """
        q = request.query_params.get("q", "")
        print("query_params :", q)
        print("\n")

        q = q.strip()
        if not q:
            return Response(
                {"detail": "Query Parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        words = list(w.lower() for w in q.split() if w.strip())
        if not words:
            return Response(
                {"detail": "Query Parameter 'q' must contain atleast one word."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        case_expressions = [
            Case(
                When(name__icontains=word, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
            for word in words
        ]

        relevance_count = None
        for case_expr in case_expressions:
            if relevance_count is None:
                relevance_count = case_expr
            else:
                relevance_count = relevance_count + case_expr

        # Annotate each Candidate with that combined “relevance” integer
        annotated_qs = Candidate.objects.annotate(relevance=relevance_count)

        annotated_qs = annotated_qs.filter(relevance__gt=0).order_by("-relevance")

        # print relevance
        print("Candidate by Relevance :")
        for c in annotated_qs:
            print(c.id, c.name, c.relevance)

        name_list = list(annotated_qs.values_list("name", flat=True))
        print("\n name list :", name_list)
        return Response(name_list, status=status.HTTP_200_OK)
