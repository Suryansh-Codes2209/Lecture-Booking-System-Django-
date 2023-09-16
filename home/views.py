from django.shortcuts import render , HttpResponse , redirect
from home.models import Contact , Lectures , Booking 
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request , 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact( name=name, email=email , subject=subject , desc=desc)
        contact.save()
        messages.success(request, "Your Message has been sent!!!!")
    return render(request , 'contact.html')

def booking(request):
    Lectures_list = Lectures.objects.all()
    if request.method == "POST":

        date = request.POST.get('date')
        time = request.POST.get('time')
        lecture = request.POST.get('lecture')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        branch = request.POST.get('branch')

        book = Booking( date=date , time=time , lecture=lecture , name=name, email=email , phone=phone , college=college , branch=branch)
        book.save()
        messages.success(request, "🙌😊Your Booking is succesfully registered . you will shortly receive a Mail !!")
    
    return render(request , 'booking.html' , {"Lectures":Lectures_list} )

def booked(request):
    return render(request , 'booked.html')

def avilable(request):
    Lectures_list = Lectures.objects.all()


    return render(request , 'avilable.html' , {"Lectures":Lectures_list})

def booked1(request):
    Student = Booking.objects.all()

    return render(request , 'booked1.html' , {"Book":Student})
