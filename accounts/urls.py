from django.contrib import admin
from django.urls import path

from accounts.views import *

urlpatterns = [
    # path("home/", home, name="home"),
    path("faculty_login/", faculty_login, name="faculty_login"),
    path("faculty_page/", faculty_page, name="faculty_page"),
    path("add_faculty/", add_faculty, name="add_faculty"),
    path("faculty_logout/", faculty_logout, name="faculty_logout"),
    path("admin_login/", admin_login, name="admin_login"),
    path("admin_logout/", logout_view, name="admin_logout"),
    path("free_list/", free_list, name="free_list"),
]
