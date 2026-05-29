from django.shortcuts import render
from ticketSales.models import concertModel
from django.contrib.auth.decorators import login_required
from ticketSales.models import locationModel
from ticketSales.models import timeModel
from ticketSales.forms import SearchForm, concertFrom
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import ticketSales
import ticketSales.views


# Create your views here.
def home(request):
    searchFrom = SearchForm(request.GET)
    times = timeModel.objects.all()
    today = datetime.today()
    if searchFrom.is_valid():
        searchText = searchFrom.cleaned_data["SearchText"]
        concerts = concertModel.objects.filter(name__contains=searchText)

    else:
        concerts = concertModel.objects.all()
    context = {
        "concertlist": concerts,
        "concertcount": concerts.count(),
        "searchFrom":  searchFrom,
        "TodayData": today,
        "timelist": times,
    }

    return render(request, 'webapp/index.html', context)


def locationa_list_view(request):

    locations = locationModel.objects.all()

    context = {
        "locationlist": locations,
    }
    return render(request, "ticketSales/locationlist.html", context)


def concertDetails(request, concert_id):
    concert = concertModel.objects.get(pk=concert_id)
    time = timeModel.objects.get(pk=concert_id)
    context = {
        "concertdetails": concert,
        "time": time
    }

    return render(request, "ticketSales/concert_details.html", context)


@login_required
def time_details(request, time_id):
    concert = concertModel.objects.get(pk=time_id)
    times = timeModel.objects.filter(concert=concert)

    context = {
        "timelist": times,
        "concertdetails": concert,
    }
    return render(request, "ticketSales/concert_details.html", context)


@login_required
def time_view(request):
    times = timeModel.objects.all()

    context = {
        "timelist": times,
    }
    return render(request, "ticketSales/timelist.html", context)


def concertedite(request, concert_id):
    concert = concertModel.objects.get(pk=concert_id)

    if request.method == "POST":
        concert_form = concertFrom(request.POST, request.FILES, instance=concert)
        if concert_form.is_valid:
            concert_form.save()
            return HttpResponseRedirect(reverse(ticketSales.views.home))

    else:
        concert_form = concertFrom(instance=concert)

    context = {
        "concertForm": concert_form,
        "posterImage": concert.poster,
        "concert": concert,
    }
    return render(request, "ticketSales/concertEdit.html", context)
