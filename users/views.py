import os

from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth import login as login_user
from django.contrib.auth.models import User


# if os.path.exists('rando/env.py'):
#     from djangoProject.env import AUTO_USER, AUTO_PASSWORD
# else:
#     AUTO_USER = os.environ.get('AUTO_USER')
#     AUTO_PASSWORD = os.environ.get('AUTO_PASSWORD')


# def auto_login(request):
#     try:
#         user = User.objects.get(username=AUTO_USER)
#         user.set_password(AUTO_PASSWORD)
#         user = authenticate(username=user.username, password=AUTO_PASSWORD)
#
#         login_user(request, user)
#         return HttpResponseRedirect(reverse('company_search'), {'message': 'Welcome to Randomizer'})
#
#     except User.DoesNotExist:
#         return render(request, '403.html')  # handle it here return valid error here



# def register(request):
#     if request.method != 'POST':
#         form = UserCreationForm()
#     else:
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             authenticated_user = authenticate(username=new_user.username,
#                                               password=request.POST['password1'])
#             login(request, authenticated_user)
#             return HttpResponseRedirect(reverse('company_search'))
#
#     context = {'form': form}
#     return render(request, 'users/register.html', context)


# def welcome(request):
#     # WORKED ON BY MICHAEL NEED TO WORK OUT A BETTER WAY OF DOING THIS
#     # try:
#     #     jurisdictions = Jurisdiction.objects.all().order_by('-name')
#     # except Jurisdiction.DoesNotExist:
#     #     return render(request, 'users/403.html')
#
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('create_teams'))
#     else:
#         if code:
#             url = access_url
#             headers = {
#                 'Content-Type': 'application/x-www-form-urlencoded',
#                 'Cookie': 'visid_incap_1574952=/aP5e+LbRde8eud+nkEEUt3dIl8AAAAAQUIPAAAAAAAcGfwWeYl2Y3o9vc0ai2zN'
#             }
#
#             # payload = "code=" + code + "&client_secret=T8uyFpqjf3EnKQD2BC67f57S2R578fws&grant_type=authorization_code&client_id=urn:kycidentify-dev.uk.pwc.com&redirect_uri=urn:kycidentify-dev.uk.pwc.com"
#
#             payload = "code=" + code + "&client_secret=" + client_secret + "&grant_type=authorization_code&client_id=" + client_id + "&redirect_uri=" + redirect_uri
#
#             pre_code = payload
#             response = requests.request("POST", url, headers=headers, data=payload)
#
#             # see what the response is and send to page
#             json_data = response.json()
#             message = json_data['id_token']
#             # grab the stuff back and decode the jwt
#             # encoded_jwt = message.get('access_token')
#             secret = 'T8uyFpqjf3EnKQD2BC67f57S2R578fws'
#             decoded = jwt.decode(message, verify=False)  # secret, algorithms='HS256'
#             # extract the email address and first name
#             try:
#                 user = User.objects.get(username=decoded['nameid'])
#                 login_user(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
#
#             except User.DoesNotExist:
#                 return render(request, 'users/403.html')  # handle it here return valid error here
#
#         return render(request, 'base.html', {'message': 'Welcome to Randomizer'})
