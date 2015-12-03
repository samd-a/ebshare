from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login
from django.utils.decorators import method_decorator
from django.contrib.auth import (login as auth_login)
from django.contrib.auth import (logout as auth_logout)
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import authenticate

from userAuth.models import User

# Create your views here.
def renderSignup(request):
  """
  here we will manage all signup stuff
  """
  if request.method=="GET":
    params = dict()
    params['user']=''
    return render(request, "userAuth/signup.html",params)
  if request.method=="POST":
    params = dict()
    params['user']='logged_in'
    name = request.POST['name']
    email = request.POST['email']
    confirm_email = request.POST['confirm_email']
    password = request.POST['password']
    cnfrm_password = request.POST['cnfrm_password']
    if (email==confirm_email and password==cnfrm_password):
      user = User(name=name,username=email, email=email)
      user.set_password(password)
      user.save()
      return HttpResponse("registered successfully now admin will approve soon")

def renderSignin(request):
  """
  all login stuff, just need to confirm how to set password,
  than we will implement these, till than its on hold.
  """
  if request.method == 'GET':
      params = dict()
      params["view"] = "login"
      return render(request, "userAuth/signin.html", params)
  if request.method == 'POST':
      if not request.POST.get('remember', None):
          request.session.set_expiry(0)
      else:
          request.session.set_expiry(10)
      return login(request, *args, **kwargs)


class LoginRequiredMixin(object):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
      return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class Logout(LoginRequiredMixin, View):
    def get(self,request):
        auth_logout(request)
        return HttpResponseRedirect('/')


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

