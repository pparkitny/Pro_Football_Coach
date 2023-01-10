from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Coach
from .serializers import CoachSerializer


@csrf_exempt
def coach_list(request):
    """
    List all code snippets, or create a new coach.
    """
    if request.method == 'GET':
        coaches = Coach.objects.all()
        serializer = CoachSerializer(coaches, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CoachSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def coach_detail(request, pk):
    """
    Retrieve, update or delete a code coach.
    """
    try:
        coaches = Coach.objects.get(pk=pk)
    except Coach.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CoachSerializer(coaches)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CoachSerializer(coaches, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        coaches.delete()
        return HttpResponse(status=204)
