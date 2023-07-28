from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from timetable.models import *
from django.http import JsonResponse

# Create your views here.
def add_subject(request):
    context = {}
    context["subjects"] = Subject.objects.all()
    if request.method == "POST":
        code = request.POST.get("code")
        name = request.POST.get("name")
        semester = request.POST.get("semester")
        try:
            subject = Subject(code=code, name=name, semester=semester)
            subject.save()
            context["msg"] = "Subject added Successfully"
        except:
            context["msg"] = "Subject with this code already exists"
    return render(request, "add_subject.html", context)


def assign_subject(request):
    context = {}
    context["subjects"] = Subject.objects.all()
    context["faculties"] = Faculty.objects.all()
    context["assigned"] = Subject_Assigned.objects.all()
    if request.method == "POST":
        room = request.POST.get("room")
        remarks = request.POST.get("remarks")
        subject = Subject.objects.get(code=request.POST.get("subject"))
        faculty = Faculty.objects.get(username=request.POST.get("faculty"))
        try:
            Subject_Assigned.objects.get(subject=subject, faculty=faculty)
            context["msg"] = "This Subject already assigned to this Faculty"
        except:
            subject_assigned = Subject_Assigned(
                subject=subject, faculty=faculty, remarks=remarks, room=room
            )
            subject_assigned.save()
            context["msg"] = "Subject assigned Successfully"
    return render(request, "assign_subject.html", context)


def show_timetable(request):
    sem = request.GET.get("sem")
    tt = TimeTable.objects.filter(semester=sem)
    return render(request, "show_timetable.html", {"tt": tt, "sem": sem})


def generate_timetable(request, sem):
    context = {}
    context["tt"] = TimeTable.objects.filter(semester=sem)
    context["assg"] = Subject_Assigned.objects.filter(subject__semester=sem)
    context["sem"] = sem
    return render(request, "generate_timetable.html", context)


@csrf_exempt
def check_freedom(request):
    period = request.POST.get("period")
    day = request.POST.get("pday")
    print(request.POST)
    sa = Subject_Assigned.objects.get(id=request.POST.get("sa"))
    print(sa)
    q = TimeTable.objects.filter(day=day)
    # print(q)
    if "period1" in period:
        qr = q.filter(period1__faculty=sa.faculty)
    if "period2" in period:
        qr = q.filter(period2__faculty=sa.faculty)
    if "period3" in period:
        qr = q.filter(period3__faculty=sa.faculty)
    if "period4" in period:
        qr = q.filter(period4__faculty=sa.faculty)
    if "period5" in period:
        qr = q.filter(period5__faculty=sa.faculty)
    if "period6" in period:
        qr = q.filter(period6__faculty=sa.faculty)
    if "period7" in period:
        qr = q.filter(period7__faculty=sa.faculty)
    if "period8" in period:
        qr = q.filter(period8__faculty=sa.faculty)
    if qr:
        return JsonResponse({"code": 0, "msg": "Not free"})
    else:
        qs = q.filter(semester=request.POST.get("sem"))[0]
        if "period1" in period:
            qs.period1 = sa
            qs.save()
            qd = qs.period1
        if "period2" in period:
            qs.period2 = sa
            qs.save()
            qd = qs.period2
        if "period3" in period:
            qs.period3 = sa
            qs.save()
            qd = qs.period3
        if "period4" in period:
            qs.period4 = sa
            qs.save()
            qd = qs.period4
        if "period5" in period:
            qs.period5 = sa
            qs.save()
            qd = qs.period5
        if "period6" in period:
            qs.period6 = sa
            qs.save()
            qd = qs.period6
        if "period7" in period:
            qs.period7 = sa
            qs.save()
            qd = qs.period7
        if "period8" in period:
            qs.period8 = sa
            qs.save()
            qd = qs.period8
        # print(qs)

        return JsonResponse(
            {
                "code": 1,
                "msg": "alloted",
                "room": qd.room,
                "subject": qd.subject.name,
                "faculty": qd.faculty.name,
            }
        )
