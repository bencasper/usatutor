import datetime

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from user_admin.models import UserTutorSchedule

from user_admin.serializer import TutorScheduleSerializer


@csrf_exempt
def schedule_list(request, tutor_id):
    """
    List all code schedules, or create a new snippet.
    """
    if request.method == 'GET':
        schedules = UserTutorSchedule.objects.filter(Q(tutor_id=tutor_id, due_date__gte=datetime.date.today())).order_by('-create_time')
        serializer = TutorScheduleSerializer(schedules, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def schedule_detail(request, pk):
    """
    Retrieve, update or delete a code schedule.
    """
    try:
        schedule = UserTutorSchedule.objects.get(pk=pk)
    except UserTutorSchedule.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TutorScheduleSerializer(schedule)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TutorScheduleSerializer(schedule, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=204)
