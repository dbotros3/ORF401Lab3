from django.shortcuts import render

from django.shortcuts import redirect

from .models import Person

# relative import of forms
from .forms import RideForm

from .forms import RideForm, NewRideForm

# Create your views here.


def index(request):
    context = {}

    people = Person.objects.none()

    if "search_orig" in request.GET:
        search_orig = request.GET["search_orig"]
        people = Person.objects.filter(origination_city__icontains=search_orig) | Person.objects.filter(destination_city__icontains=search_orig)

    if "search_dest" in request.GET:
        search_dest = request.GET["search_dest"]
        people = people.filter(destination_state__icontains=search_dest)

    context["people"] = people
    context["form"] = RideForm()
    context["new_ride_form"] = NewRideForm()

    return render(request, "index_view.html", context)

def splash_page(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST':
        form = NewRideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rides:splash_page')  # Redirect to the listing page after successful creation
    else:
        form = NewRideForm()  # Initialize an empty form for GET requests
    return render(request, 'rides/create_ride.html', {'form': form})  # Render the form page for GET requests

