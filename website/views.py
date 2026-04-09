from django.shortcuts import render, redirect
from .models import Contact, Feedback, Quote

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and email and phone and message:
            Quote.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            return redirect("home")

    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            return redirect("contact")

    feedbacks = list(Feedback.objects.all()[:8])
    return render(request, "contact.html", {"feedbacks": feedbacks})


def projects(request):
    if request.method == "POST":
        name = request.POST.get("feedback_name")
        location = request.POST.get("feedback_location")
        message = request.POST.get("feedback_message")
        rating = request.POST.get("feedback_rating", "5")

        if name and location and message:
            try:
                rating_value = int(rating)
            except (TypeError, ValueError):
                rating_value = 5

            rating_value = max(1, min(5, rating_value))
            Feedback.objects.create(
                name=name,
                location=location,
                rating=rating_value,
                message=message
            )
            return redirect("projects")

    return render(request, "projects.html")
def about(request):
    return render(request, 'about.html')

#Our Solar Products


def tata(request):
    return render(request, 'tata.html')

def waaree(request):
    return render(request, 'waaree.html')

def adani(request):
    return render(request, 'adani.html')

def primier(request):
    return render(request, 'primier.html')

def utl(request):
    return render(request, 'utl.html')

#Our Services
def residential(request):
    return render(request, 'residential.html')

def commercial(request):
    return render(request, 'commercial_solar.html')

def industrial(request):
    return render(request, 'industrial_solar.html')

def solar_maintenance(request):
    return render(request, 'solar_maintenance.html')
