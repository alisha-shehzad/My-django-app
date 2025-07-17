from django.contrib import admin
from django.urls import path, include  # include added
from django.http import HttpResponse  # To return an HTML response

# 👇 Define a view function
def hello_netsol(request):
    return HttpResponse("<h1 style='text-align: center; color: #2c3e50;'>Hello Netsol</h1>")

# 👇 URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include your API urls here
    path('', hello_netsol),  # root URL will show Hello Netsol
]
