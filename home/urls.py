from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home,name="home"), 
    path('', views.home3,name="home"),
    path('contact', views.contact,name="home"),
    path('aboutUs', views.aboutus,name="home"),
    path('services', views.services,name="home"),
    path('contact/form', views.contactform,name="home"),
    path('career/apply/<int:id>', views.CarrerApply,name="careerapply"),
    path('career/apply/upload/<int:id>', views.UploadResume,name="home"),
]