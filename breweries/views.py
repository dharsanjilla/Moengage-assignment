from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Brewery, Review
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse  
import requests
import uuid

def search_breweries(request):
    query = request.GET.get('query')
    search_type = request.GET.get('type')
    breweries = []
    if query:
        if search_type == 'city':
            response = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={query}')
        elif search_type == 'name':
            response = requests.get(f'https://api.openbrewerydb.org/breweries?by_name={query}')    
        elif search_type == 'type':
            response = requests.get(f'https://api.openbrewerydb.org/breweries?by_type={query}')
        breweries = response.json()
    error_message = None
    return render(request, 'breweries/search.html', {'breweries': breweries})


@login_required
def brewery_detail(request, brewery_id):
        
        try:
            # Convert captured brewery_id to a UUID object
            brewery_id = uuid.UUID(str(brewery_id))
            
        except ValueError:
            # Handle invalid UUID
            error_message = 'Invalid brewery ID.'
            return redirect('search', error_message=error_message)

        try:
            brewery = Brewery.objects.get(id=brewery_id)
        except Brewery.DoesNotExist:
            error_message = 'Brewery not found.'
            return redirect(reverse('search_breweries') + f'?error_message={error_message}')

        reviews = Review.objects.filter(brewery=brewery)
        review_form = ReviewForm()

        context = {'brewery': brewery, 'reviews': reviews, 'review_form': review_form}
        return render(request, 'brewery_details.html', context)


@login_required
def add_review(request, brewery_id):
        brewery = get_object_or_404(Brewery, id=brewery_id)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.brewery = brewery
                review.user = request.user
                review.save()
                return redirect('brewery_detail', brewery_id=brewery.id)
        else:
            form = ReviewForm()
        return render(request, 'breweries/add_review.html', {'form': form})


def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('search_breweries')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def login(request,user):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('search_breweries')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})

