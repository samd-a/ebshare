from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def renderHome(request):
	pass
	return render(request, "homePage/home.html")