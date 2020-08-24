from django.contrib import admin

# Register your models here.
from middleware.admin import TutorREADAdmin, TutorCRUDAdmin

from class_admin.models import ClassAdminModel


@admin.register(ClassAdminModel)
class ClassAdmin(TutorREADAdmin):
    list_display = ('id',
                    'class_time',
                    'duration',
                    'course_tutor_name',
                    'course_student_name',
                    'course_status',
                    'score'
                    )

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        from sale_admin.models import SaleOrderCourse
        qs = SaleOrderCourse._default_manager.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def id(self, obj):
        return obj.id

    def class_time(self, obj):
        from django.utils.dateformat import format

        from django.conf import settings
        return format(obj.course_begin_time, settings.DATETIME_FORMAT) + '~' + format(obj.course_end_time, settings.DATETIME_FORMAT)
    class_time.short_description = '课程时间'

    def course_tutor_name(self, obj):
        return obj.course_tutor_name
    course_tutor_name.short_description = 'tutor'

    def course_student_name(self, obj):
        return obj.course_student_name
    course_student_name.short_description = '学员'

    def course_status(self, obj):
        return obj.course_status
    course_status.short_descrption = '课程状态'

    def duration(self, obj):
        return obj.course_duration
    duration.short_description = '时长'

    def score(self, obj):
        return 5
    score.short_description = '评分'


