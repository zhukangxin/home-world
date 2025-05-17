from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
    """
    A view that returns a simple "Hello World!" response.
    """
    # You can use render to return an HTML template if needed
    # return render(request, 'home.html')

    # For now, we'll just return a plain text response
    return HttpResponse("Hello World!")
