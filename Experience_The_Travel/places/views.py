from django.shortcuts import render,get_object_or_404,redirect
from .models import Place
from .forms import PlaceFilterForm


# Create your views here.
def home(request):
    places = Place.objects.order_by('id')[:3]
    return render(request,'home.html', {'places': places})

def search(request):
    form = PlaceFilterForm(request.GET)

    places = Place.objects.order_by('id')[:4]

    # destination_type = request.GET.get('destination_type')
    # typologies = request.GET.getlist('typologies')
    # duration = request.GET.get('duration')
    # difficulty = request.GET.get('difficulty')

    # # Filtering the queryset based on request data
    # if destination_type:
    #     places = places.filter(destination_type=destination_type)

    # if typologies:
    #     places = places.filter(typologies__in=typologies).distinct()

    # if duration and duration != '':
    #     places = places.filter(duration=duration)

    # if difficulty and difficulty != '':
    #     places = places.filter(difficulty=difficulty)
    context = {
        'form': form,
        'places': places,
    }
    return render(request, 'search.html', context)



def filter(request):
    form = PlaceFilterForm(request.GET)

    places = Place.objects.all()

    destination_type = request.GET.get('destination_type')
    typologies = request.GET.getlist('typologies')
    duration = request.GET.get('duration')
    difficulty = request.GET.get('difficulty')

    # Filtering the queryset based on request data
    if destination_type:
        places = places.filter(destination_type=destination_type)

    if typologies:
        places = places.filter(typologies__in=typologies).distinct()

    if duration and duration != '':
        places = places.filter(duration=duration)

    if difficulty and difficulty != '':
        places = places.filter(difficulty=difficulty)
    context = {
        'form': form,
        'places': places,
    }
    return render(request, 'search.html', context)

    # if form.is_valid():
    #     if form.cleaned_data['destination_type']:
    #         places = places.filter(destination_type=form.cleaned_data['destination_type'])
    #     if form.cleaned_data['duration']:
    #         print(form.cleaned_data['duration'],"duration")
    #         places = places.filter(duration=form.cleaned_data['duration'])
    #     if form.cleaned_data['difficulty']:
    #         places = places.filter(difficulty=form.cleaned_data['difficulty'])
    #     if form.cleaned_data['typologies']:
    #         places = places.filter(typologies__in=form.cleaned_data['typologies']).distinct()
    # return render(request,'search.html', {'form': form, 'places': places})

def details(request, pk):
    place = get_object_or_404(Place, pk=pk)

    all_places = Place.objects.exclude(pk=pk).order_by('-id')
    places = all_places[:3]

    return render(request,'details.html',{'place': place,'places': places})