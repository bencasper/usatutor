import datetime

from django.contrib.auth import get_user
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import UserTutorSchedule
from .serializer import TutorScheduleSerializer


def schedule_list(request, tutor_id):
    """
    List all code schedules, or create a new snippet.
    """
    if request.method == 'GET':
        schedules = UserTutorSchedule.objects.filter(
            Q(tutor_id=tutor_id, due_date__gte=datetime.date.today())).order_by('-create_time')
        serializer = TutorScheduleSerializer(schedules, many=True)
        return JsonResponse(serializer.data, safe=False)


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


@api_view(['POST'])
def add_schedule(request):
    """
    Add new schedule
    """
    schedule_param = request.data
    user = get_user(request)
    schedule = UserTutorSchedule(tutor_id=user.id,
                                 event_id=schedule_param['event_id'],
                                 course_id=schedule_param['course_id'],
                                 course_name=schedule_param['course_name'],
                                 start_at=schedule_param['start_at'],
                                 end_at=schedule_param['end_at'],
                                 edit_by=user.username)
    schedule.save()
    return HttpResponse(schedule.id, status=200)


@api_view(['POST'])
def update_schedule(request):
    """
    update schedule
    :param request:
    :return:
    """
    schedule_param = request.data
    user = get_user(request)
    schedule = UserTutorSchedule.objects.get(pk=schedule_param['schedule_id'])
    schedule.start_at = schedule_param['start_at']
    schedule.end_at = schedule_param['end_at']
    schedule.save()
    return HttpResponse(schedule.id, status=200)


@api_view(['POST'])
def del_schedule(request):
    """

    :param request:
    :param schedule_id:
    :return:
    """
    UserTutorSchedule.objects.filter(id=request.data['id']).delete()
    return HttpResponse('success', status=200)
