from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Author, Book, Contact, Cart
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'link':'index',
	    'category_list':category_list
    })

def index_detail(request, id):
    author_list = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'link':'index_detail',
	    'author_list':author_list
        
    })

def index_detail_book(request, id):
    book_list = Author.objects.filter(pk=id)
    return render(request, 'main/index_detail_book.html', context={
        'link':'index_detail',
	    'book_list':book_list
        
    })

def contact(request):
    if request.method == 'POST':
        contact_email = request.POST.get('contact_email')
        review = request.POST.get('review')
        Contact.objects.create(contact_email=contact_email, review=review)
        return redirect('index')
    return render(request, 'main/contact.html', context={
        'link':'contact'
    })



def card(request):
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        mymodel = Book.objects.get(id=prod_id)
        Cart.objects.create(prod=mymodel)
        return redirect('index')
    cart_list = Cart.objects.all()
    for i in cart_list:
        summ += i.prod.price
    return render(request, 'main/card.html', context={
        'cart_list':cart_list,
        'summ':summ,
        'link':'card'
    })


def delete_prod(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Cart.objects.filter(id=prod_id).delete()
        return redirect('card')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form, 'link':'register'})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form, 'link':'login'})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")