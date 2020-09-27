from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Product
from django.views import View
import simplesearch
import re
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import ProductCategory
from django import forms


# home page view
class HomeView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/maincatalog.html', {'products': products})

    def post(self, request):
        product = Product.objects.all()
        product.create(name = request.POST['name'], seller = request.POST['seller'], description = request.POST['description'], image = request.POST['image'])
        return HttpResponseRedirect( reverse('home') )

@method_decorator(login_required, name = 'get')
class AddView(View, LoginRequiredMixin):
    
    def get(self, request):
        products = Product.objects.all()
        form = ProductCategory()
        return render(request, 'products/adding.html', {'products': products, 'form': form})

    def post(self, request):
        product = Product.objects.all()
        seller = request.user
        form = ProductCategory()
        product.create(
            name = request.POST['name'],
            seller_id = seller.id,
            description = request.POST['description'],
            image = request.POST['image'],
            amount = request.POST['amount'],
            price = request.POST['price'],
            category = request.POST['category'],
                )
        return HttpResponseRedirect( reverse('home') )

def productinfo(request, id):
    if request.method == 'GET':
        user_id = request.user.id
        product = Product.objects.get(id=id)
        return render(request, 'products/productinfo.html', {'product': product, 'user_id': user_id})
    elif request.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect( reverse('home') )

# search view
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['name',])
        products = Product.objects.filter(entry_query).order_by('id')
        return render(request, 'products/search.html', { 'query_string': query_string, 'products': products })
    else:
        return render(request, 'products/search.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })
