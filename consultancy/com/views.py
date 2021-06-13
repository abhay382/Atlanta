from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from.models import Contact



def index (request):
    return render(request,'index.html')





def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'Contact.html', {'thank': thank})







def Digital (request):
    return render(request,'Digitalmarketing.html')



def about (request):
    return render(request,'Aboutus.html')


def bigdata (request):
    return render(request,'Bigdata.html')


def advertisement (request):
    return render(request,'Advertisement.html')

def Business (request):
    return render(request,'Businessconsultant.html')

def carrier (request):
    return render(request,'Carrier.html')

def cloud (request):
    return render(request,'Cloudservices.html')

def consulting (request):
    return render(request,'Consulting.html')

def dataanalyse (request):
    return render(request,'Dataanalyse.html')


def datascience (request):
    return render(request,'Datascience.html')


def development (request):
    return render(request,'Development.html')


def ecommmerce (request):
    return render(request,'Ecommercesolution.html')


def Financesolution (request):
    return render(request,'Financesolution.html')


def Powerplatform (request):
    return render(request,'Powerplatform.html')

def SAP (request):
    return render(request,'SAP.html')
