from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .models import Category,Products,Toppings,CartItem,Placed_Order,Reviews
from decimal import Decimal
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You need to login first!')
        return HttpResponseRedirect(reverse("login"))
    else:
        # print(request.user.id)
        counter = Placed_Order.objects.count()
        items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
        len1 = 0
        if items:
            len1 = len(items)
        context={
            'user': request.user,
            'Category': Category.objects.all(),
            'length': len1
        }
        return render(request,'orders/index.html',context)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User registered successfully!')
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "orders/signup.html", {'form': form})
    else:
        form = SignupForm()
    return render(request, 'orders/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            name = user.username
            messages.add_message(request,messages.SUCCESS,f'Welcome {request.user.first_name}')
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'orders/login.html',{'form':form})

    else:
        form = AuthenticationForm()
        return render(request,'orders/login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,"Logged out from Cheesilicious")
    return HttpResponseRedirect(reverse('login'))

def listmenu(request,name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        try:
            if name != 'Toppings':
                products = Products.objects.all().filter(product_type__name=name)
                print(products)
        except Products.DoesNotExist:
            raise Http404("Item does not exist")
        flag2=False
        if name=='Pasta' or name=='Salad':
            flag=True
        else:
            flag=False
        if name=='Toppings':
            products=Toppings.objects.all()
            flag2=True
            flag=True
        if name!='Toppings':
            toppings = Toppings.objects.all()
        else:
            toppings=''
        items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
        len1 = 0
        if items:
            len1 = len(items)
        context = {
            "products": products,
            'name':name,
            'flag':flag,
            'flag2':flag2,
            'toppings':toppings,
            'length': len1
        }
        
        return render(request, "orders/list.html", context)
def contact(request):
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/contact.html', {'length':len1})

def home(request):
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/home.html',{'length':len1})

def add_to_cart(request):
    if request.method=='POST':
        category=str(request.POST['type'])
        subcategory=str(request.POST['subcategory'])
        price=Decimal(request.POST['size'])
        toppings=[]
        topping1=''
        topping2=''
        topping3=''
        topping4=''
        topping5=''
        if str(category)=='Regular Pizza' or str(category)=='Sicilian Pizza':
            tops=(request.POST.getlist('custom'))
            for top in tops:
                if top != 'None':
                    toppings.append(top)
            num_of_toppings=len(toppings)
            if num_of_toppings==1:
                topping1=toppings[0]
            elif num_of_toppings==2:
                topping1=toppings[0]
                topping2=toppings[1]
            elif num_of_toppings==3:
                topping1=toppings[0]
                topping2=toppings[1]
                topping3=toppings[2]
            elif num_of_toppings==4:
                topping1=toppings[0]
                topping2=toppings[1]
                topping3=toppings[2]
                topping4=toppings[3]
            elif num_of_toppings==5:
                topping1=toppings[0]
                topping2=toppings[1]
                topping3=toppings[2]
                topping4=toppings[3]
                topping5=toppings[4]
        if str(category) == "Regular Pizza":
            item1=Products.objects.filter(product_type__name="Regular Pizza").filter(name__startswith=subcategory).values('small_price','large_price')
            if Decimal(price) == Decimal(item1[0]['small_price']):
                size="small"
            else:
                size ="large"
        elif str(category) == "Sicilian Pizza":
            item1=Products.objects.filter(product_type__name=category).filter(name__startswith=subcategory).values('small_price','large_price')
            if Decimal(price) == Decimal(item1[0]['small_price']):
                size="small"
            else:
                size ="large"
        elif str(category) == "Subs":
            item1=Products.objects.filter(product_type__name=category).filter(name__startswith=subcategory).values('small_price','large_price')
            if Decimal(price) == Decimal(item1[0]['small_price']):
                size="small"
            else:
                size ="large"
        elif str(category) == "Dinner Platters":
            item1=Products.objects.filter(product_type__name=category).filter(name__startswith=subcategory).values('small_price','large_price')
            if Decimal(price) == Decimal(item1[0]['small_price']):
                size="small"
            else:
                size ="large"
        elif str(category)=='Pasta' or str(category)=='Salad':
            size= 'N/A'
        else:
            size='N/A'
        cartitem=CartItem(user_id=request.user.id,category=category,subcategory=subcategory,price=price,size=size,topping1=topping1,topping2=topping2,topping3=topping3,topping4=topping4,topping5=topping5)
        cartitem.save()

        #messages.add_message(request,messages.SUCCESS,'Item added to cart successfully!')
        #
        try:
            if category != 'Toppings':
                products = Products.objects.all().filter(product_type__name=category)
        except Products.DoesNotExist:
            raise Http404("Item does not exist")
        flag2=False
        if category=='Pasta' or category=='Salad':
            flag=True
        else:
            flag=False
        if category=='Toppings':
            products=Toppings.objects.all()
            flag2=True
            flag=True
        if category!='Toppings':
            toppings = Toppings.objects.all()
        else:
            toppings=''
        it = CartItem.objects.filter(user_id= request.user.id, order_no= None)
        len1 = 0
        if it:
            len1 = len(it)
        context = {
            "products": products,
            'name': category,
            'flag':flag,
            'flag2':flag2,
            'toppings':toppings,
            'length':len1
        }
        messages.add_message(request,messages.SUCCESS,'Item added to cart successfully!')
        return render(request, "orders/list.html", context)
      
    

def checkout(request):
    if not request.user.is_authenticated:
        messages.add_message(request,messages.WARNING,'Please login to place your order')
        return HttpResponseRedirect(reverse('login'))
    
    cost=CartItem.objects.filter(user_id=request.user.id).values('price','order_no')
    total=0
    for c in cost: 
        if not c['order_no']:
            total += c['price']
    
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    context={
        'checkout_items':CartItem.objects.filter(user_id=request.user.id, order_no=None),
        'total_cost':total,
        'length': len1
    }
    check=CartItem.objects.all()
    return render(request,'orders/checkout.html',context=context)

def faq(request):
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/faq.html', {'length': len1})


def placeorder(request):
    if not request.user.is_authenticated:
        messages.add_message(request,messages.WARNING,'Please login to place your order.')
        return HttpResponseRedirect(reverse('login'))
    if request.method=='POST':
        #get the email of the receiver

        ordernumber=Placed_Order.objects.count()
        items=CartItem.objects.filter(user_id=request.user.id)
        ordernumber += 1
        for i in items:
            if not i.order_no:
                i.order_no=ordernumber
                i.save()
        placed_order=Placed_Order(order_no=ordernumber,user_id=request.user.id,status='Pending')
        placed_order.save()
        item1=CartItem.objects.filter(user_id=request.user.id, order_no=ordernumber)

        content = "Order id:"+str(ordernumber)+"\nStatus: Pending\nComplete order details:\n"
        sum = 0
        for i in item1:
            content += ("category: "+ str(i.category)+", subcategory: "+ str(i.subcategory)+"\nprice: $"+str(i.price)+"\n")
            sum += (i.price)
        content += ("Total: $" + str(sum))
        send_mail(
                #subject #msg #from mail #rec list
                "Details of order placed", 
                content, 
                settings.EMAIL_HOST_USER,
                ["komalsharma0509@gmail.com", request.user.email]
            )

    messages.add_message(request,messages.SUCCESS,'Your order has been successfully placed!')
    return HttpResponseRedirect(reverse('see_order_status'))

def see_order_status(request):
    if not request.user.is_authenticated:
        messages.add_message(request,messages.WARNING,'Please login first.')
        return HttpResponseRedirect(reverse('login'))
    get_all_orders = Placed_Order.objects.filter(user_id=request.user.id)
    contents=[]
    if get_all_orders:
        for order in get_all_orders:
            ord_no=order.order_no
            orders=CartItem.objects.filter(order_no=ord_no)
            for o in orders:
                cont={}
                cont['order_no'] = ord_no
                cont['status'] = order.status
                cont['date_time'] = order.date_time
                cont['category']=o.category
                cont['subcategory']=o.subcategory
                cont['size'] = o.size
                cont['price'] = o.price
                if o.topping1:
                    cont['topping1'] = o.topping1
                    if o.topping2:
                        cont['topping2'] =o.topping2
                        if o.topping3:
                            cont['topping3'] = o.topping3
                            if o.topping4:
                                cont['topping4'] = o.topping4
                                if o.topping5:
                                    cont['topping5'] = o.topping5
                contents.append(cont)
    else:
        contents=[]
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/see_order_status.html',{'contents':contents, 'length':len1})        

def curr_orders(request):
    if not request.user.is_superuser:
        messages.add_message(request,messages.ERROR,'You do not have access to that page!')
        return HttpResponseRedirect(reverse('index'))
    
    orders_placed= Placed_Order.objects.all()
    order_details=[]
    for order in orders_placed:
        ord_no=order.order_no
        orders=CartItem.objects.filter(order_no=ord_no).values('category','subcategory') 
        cont=[]   
        cont.append(ord_no)
        cont.append(order.user_id)
        cont.append(order.is_pending())
        for o in orders:
            temp=[]
            temp.append(o['category'])
            temp.append(o['subcategory'])
            cont.append(temp)
        order_details.append(cont)
        del cont
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/curr_orders.html',{'order_details':order_details, 'length':len1})

# [
#     [order_no, user_id, t/f,
#         [items]
#     ],
#     [

#     ]

# ]

def mark_order(request):
    if request.method == 'POST':
        order_no = request.POST['ordnum']
        obj = Placed_Order.objects.get(order_no=order_no)
        obj.status = 'Delivered'
        obj.save()
        item1=CartItem.objects.filter( order_no=order_no)
        content = "Order id:"+str(order_no)+"\nStatus: Delivered\nComplete order details:\n"
        sum = 0
        print(item1)
        for i in item1:
            content += ("category: "+ str(i.category)+", subcategory: "+ str(i.subcategory)+"\nprice: $"+str(i.price)+"\n")
            sum += (i.price)
        content += ("Total: $" + str(sum))
        send_mail(
                #subject #msg #from mail #rec list
                "Order Delivered", 
                content, 
                settings.EMAIL_HOST_USER,
                ["komalsharma0509@gmail.com", request.user.email,"sparsh_11813049@nitkkr.ac.in"]
            )
        messages.add_message(request,messages.SUCCESS,'Order completed')
        return HttpResponseRedirect(reverse('curr_orders'))
    
    return HttpResponseRedirect(reverse('home'))

def delete_item(request):
    if request.method=='POST':
        obj_id=int(request.POST['del'])
        obj = CartItem.objects.get(pk=obj_id)
        obj.delete()
        messages.add_message(request,messages.INFO,'Item deleted')
        return HttpResponseRedirect(reverse('checkout'))
    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    return render(request,'orders/home.html', {'length':len1})

def review(request):  
    User = get_user_model()
    user = User.objects.get(username="Archana")
    print(user.id)      
    if not request.user.is_authenticated:
        reviews = Reviews.objects.all()[0:2]
        reviews1 = Reviews.objects.all()[2:4]
        return render(request, 'orders/reviews.html', {'reviews':reviews,'reviews1':reviews1, 'condition':False,'cond1':False})
        # return HttpResponseRedirect(reverse("login"))

    items = CartItem.objects.filter(user_id= request.user.id, order_no= None)
    len1 = 0
    if items:
        len1 = len(items)
    userReviews = Reviews.objects.filter(user_id=request.user.id)
    if userReviews:
        reviews = Reviews.objects.all()[0:2]
        reviews1 = Reviews.objects.all()[2:4]
        context={
        'cond1':False,
        'userReviews':userReviews,
        'condition':True,
        'reviews':reviews,
        'reviews1':reviews1,
        'length':len1
        }    
        return render(request, 'orders/reviews.html', context)
    else:
        reviews = Reviews.objects.all()[0:2]
        reviews1 = Reviews.objects.all()[2:4]
        context={
        'cond1':True,
        'condition':False,
        'reviews':reviews,
        'reviews1':reviews1,
        'length':len1 
        }
        return render(request, 'orders/reviews.html', context)

def delReview(request):
    if request.method=='POST':
        obj = Reviews.objects.get(user_id=request.user.id)
        obj.delete()
        messages.add_message(request,messages.INFO,'Your review id deleted')
        return HttpResponseRedirect(reverse('reviews'))
def addReview(request):
    if(request.method=='POST'):
        stars=int(request.POST['rate'])
        desc = str(request.POST['desc'])
        user_id =request.user.id
        name=request.user.get_full_name()
        review = Reviews(user_id=user_id,name=name, description=desc, star=stars)
        review.save()
        messages.add_message(request,messages.SUCCESS,'Your review has been added!')
        return HttpResponseRedirect(reverse('reviews'))
