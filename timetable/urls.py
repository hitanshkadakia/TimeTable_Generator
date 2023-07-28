from django.contrib import admin
from django.urls import path

from timetable.views import *

urlpatterns = [
    path("add_subject/", add_subject, name="add_subject"),
    path("assign_subject/", assign_subject, name="assign_subject"),
    path("show_timetable/", show_timetable, name="show_timetable"),
    path("generate_timetable/<int:sem>", generate_timetable, name="generate_timetable"),
    path("check_freedom/", check_freedom, name="check_freedom"),
]
