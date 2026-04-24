from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


def application_list(request):
    applications = JobApplication.objects.all().order_by("-date", "-created_at")
    return render(request, "applications/application_list.html", {
        "applications": applications,
    })


def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm()

    return render(request, "applications/add_application.html", {
        "form": form,
        "title": "Add New Application",
        "button_text": "Save Application",
    })


def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm(instance=application)

    return render(request, "applications/add_application.html", {
        "form": form,
        "title": "Edit Application",
        "button_text": "Update Application",
    })

def update_status(request, pk, status):
    application = get_object_or_404(JobApplication, pk=pk)
    application.status = status
    application.save()
    return redirect("application_list")