from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from accounts.models import Faculty
from timetable.models import TimeTable


def home(request):
    return render(request, "home.html")


def add_faculty(request):
    context = {}
    context["faculties"] = Faculty.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        subjects = request.POST.get("subjects")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        designation = request.POST.get("designation")
        print(request.POST)
        # try:
        faculty = Faculty(
            username=username,
            name=name,
            subjects=subjects,
            email=email,
            phone=phone,
            gender=gender,
            designation=designation,
        )
        faculty.save()
        context["msg"] = "Faculty added Successfully"
        # except:
        #     context["msg"] = "Faculty with this ID already exists"
    return render(request, "add_faculty.html", context)


def faculty_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            faculty = Faculty.objects.filter(username=username)
            request.session["faculty_id"] = faculty[0].id
            request.session["faculty_name"] = faculty[0].name
            return redirect("faculty_page")
        except:
            return render(request, "home.html", {"msg": "This ID does not exist"})


def faculty_page(request):
    context = {}
    dummy = {}
    if request.session.get("faculty_id"):
        faculty = Faculty.objects.filter(id=request.session.get("faculty_id"))
        context["tt_monday"] = (
            TimeTable.objects.filter(day="Monday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Monday", period8__faculty=faculty[0])
        )[0]
        context["tt_tuesday"] = (
            TimeTable.objects.filter(day="Tuesday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Tuesday", period8__faculty=faculty[0])
        )[0]
        context["tt_wednesday"] = (
            TimeTable.objects.filter(day="Wednesday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Wednesday", period8__faculty=faculty[0])
        )[0]
        context["tt_thursday"] = (
            TimeTable.objects.filter(day="Thursday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Thursday", period8__faculty=faculty[0])
        )[0]
        context["tt_friday"] = (
            TimeTable.objects.filter(day="Friday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Friday", period8__faculty=faculty[0])
        )[0]
        context["tt_saturday"] = (
            TimeTable.objects.filter(day="Saturday", period1__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period2__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period3__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period4__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period5__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period6__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period7__faculty=faculty[0])
            | TimeTable.objects.filter(day="Saturday", period8__faculty=faculty[0])
        )[0]
        # print(context["tt"])
        context.update(faculty.values()[0])
        return render(request, "faculty_page.html", context)
    else:
        return redirect("home")


def faculty_logout(request):
    if request.session.get("faculty_id"):
        try:
            del request.session["faculty_id"]
            del request.session["faculty_name"]
        except:
            pass
        return render(request, "home.html", {"msg": "Successfully Logged Out"})
    return render(request, "home.html")


@login_required(login_url="/admin/login/")
def admin_login(request):
    return render(request, "home.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


def free_list(request):
    context = {}
    day = request.GET.get("day")
    if day:
        context["day"] = day
        context["list"] = TimeTable.objects.filter(day=day)
    return render(request, "free_list.html", context)
