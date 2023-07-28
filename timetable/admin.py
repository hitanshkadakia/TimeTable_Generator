from django.contrib import admin

# Register your models here.
from timetable.models import *

admin.site.register(Subject)
admin.site.register(Subject_Assigned)


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    """Admin View for TimeTable"""

    list_display = (
        "day",
        "semester",
        "period1",
        "period2",
        "period3",
        "period4",
        "period5",
        "period6",
        "period7",
        "period8",
    )
