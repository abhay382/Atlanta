from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="Home"),

    path("contact/", views.contact, name="contact"),
    path("Digital/", views.Digital, name="Digitalmarketing"),
    path("about/", views.about, name="Digitalmarketing"),
    path("bigdata/", views.bigdata, name="Digitalmarketing"),
    path("advertisement/", views.advertisement, name="Digitalmarketing"),
    path("Business/", views.Business, name="Digitalmarketing"),
    path("carrier/", views.carrier, name="Digitalmarketing"),
    path("cloud/", views.cloud, name="Digitalmarketing"),
    path("consulting/", views.consulting, name="Digitalmarketing"),
    path("dataanalyse/", views.dataanalyse, name="Digitalmarketing"),
    path("datascience/", views.datascience, name="Digitalmarketing"),
    path("development/", views.development, name="Digitalmarketing"),
    path("ecommmerce/", views.ecommmerce, name="Digitalmarketing"),
    path("Financesolution/", views.Financesolution, name="Digitalmarketing"),
    path("Powerplatform/", views.Powerplatform, name="Digitalmarketing"),
    path("SAP/", views.SAP, name="Digitalmarketing"),



]