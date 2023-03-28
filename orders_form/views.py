from django.shortcuts import render,redirect
from .models import order

def add_enquiry(request):
   # if request.user.is_authenticated == True:
   #     return redirect('/')
    if request.method=='POST':
        first_name = request.POST.get("First name")
        last_name = request.POST.get("Last name")
        e_mail = request.POST.get("E-Mail")
        phone = request.POST.get("Phone")
        country = request.POST.get("Country")
        city = request.POST.get("City")
        description = request.POST.get("Description")
        full = [first_name, last_name, e_mail, phone, country, city, description]

        order.objects.create(first_name=first_name, last_name=last_name, e_mail=e_mail, phone=phone,
                                 country=country, city=city, description=description)
        return redirect("/")
    return render(request, "orders_form/orders.html",{})


