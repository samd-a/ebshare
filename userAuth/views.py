from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from userAuth.models import User

# Create your views here.
def renderSignup(request):
  """
  here we will manage all signup stuff
  """
  if request.method=="GET":
    return render(request, "userAuth/signup.html")
  if request.method=="POST":
    params = dict()
    params['user']='logged_in'
    name = request.POST['name']
    email = request.POST['email']
    confirm_email = request.POST['confirm_email']
    if email==confirm_email:
      user = User(name=name,username=email, email=email)
      user.save()
      return render(request, "homePage/home.html", params)

def renderSignin(request):
	return render_to_response("userAuth/signin.html")


# From METSCAV

# # Create your views here.
# def login_user(request):
#     """
#     :param: HttpRequest
#     :rtype: HttpResponse
    
#     log a user into the website. This function takes the login information
#     such as the username and password from the user and pass the information
#     to **LogInForm**. The **LogInForm** has class method called **login_process()**
#     and this class method handles processing the login information.
#     """
#     title = "Log in"
#     args = {}
#     user = None

#     if request.method == "POST":
#         # The method should be post since it does not expose the user imformation on url.
#         # it should be get method since login does not change state of any user data.
#         form = LogInForm(request.POST)
#         # check the form validation.
#         if form.is_valid():

#             user = form.login_process(request)
#             if user is not None:
#                 args = {'user':user}
#                 args.update(csrf(request))
#                 return render_to_response('home/home.html', args)
#             else:
#                 args = {'title':'Username does not exist.'}
#                 args.update(csrf(request))
#                 return render_to_response('user_auth/login.html', args)
#     else:
#         form = LogInForm()


#     args = {'form':form, 'title':title}
#     args.update(csrf(request))
#     return render_to_response('user_auth/login.html', args)

