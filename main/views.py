from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if(filter_type == "all"):
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406343224',
        'nama': 'Galih Nur Rizqy',
        'kelas': 'PBP E',
        'nama_aplikasi': 'adidos',
        'products': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
    }

    return render(request, "main.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, "edit_product.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'size': product.size,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'size': product.size,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@require_POST
def login_ajax(request):
    username = strip_tags(request.POST.get("username", ""))
    password = request.POST.get("password", "")
    
    # Validasi input kosong
    if not username or not password:
        return JsonResponse({
            'success': False, 
            'message': 'Please fill in both username and password.'
        }, status=400)
    
    # Proses autentikasi
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        
        # Buat response dengan data user
        response = JsonResponse({
            'success': True,
            'message': f'Welcome back, {user.username}!',
            'redirect_url': reverse('main:show_main'),
            'username': user.username
        })
        
        # Set cookie last_login
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        return JsonResponse({
            'success': False,
            'message': 'Username or password is incorrect.'
        }, status=401)
    
@require_POST
def register_ajax(request):
    username = strip_tags(request.POST.get("username", ""))
    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")
    
    # Basic validation
    if not all([username, password1, password2]):
        return JsonResponse({
            'success': False,
            'message': 'Please complete all required fields.'
        }, status=400)
    
    # Use UserCreationForm for proper validation
    form_data = {
        'username': username,
        'password1': password1, 
        'password2': password2
    }
    
    form = UserCreationForm(form_data)
    
    if form.is_valid():
        # Save new user
        new_user = form.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Registration successful! Welcome to Adidos, {new_user.username}!',
            'redirect_url': reverse('main:login'),
            'new_user': new_user.username
        }, status=201)
    else:
        # Handle form errors - ambil error pertama saja
        error_messages = []
        for field_name, errors in form.errors.items():
            for error in errors:
                error_messages.append(str(error))
        
        return JsonResponse({
            'success': False,
            'message': error_messages[0] if error_messages else 'Registration failed. Please try again.'
        }, status=400)

@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    stock = strip_tags(request.POST.get("stock"))
    size = strip_tags(request.POST.get("size"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        stock=stock,
        size=size,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request):
    product_id = strip_tags(request.POST.get("id"))
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if user is the owner
    if product.user != request.user:
        return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=401)
    
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    stock = strip_tags(request.POST.get("stock"))
    size = strip_tags(request.POST.get("size"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == "on"

    product.name = name
    product.price = price
    product.description = description
    product.category = category
    product.stock = stock
    product.size = size
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_ajax(request):
    product_id = strip_tags(request.POST.get("id"))
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if user is the owner
    if product.user != request.user:
        return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=401)
    
    product.delete()
    return HttpResponse(b"DELETED", status=200)