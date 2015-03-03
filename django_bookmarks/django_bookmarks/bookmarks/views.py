from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.template import RequestContext
from django_bookmarks.bookmarks.forms import *
# Create your views here.

@csrf_exempt
def main_page(request):
#	template = get_template('main_page.html')
#	variables = Context({
#		'user' : request.user
#	})
#	output = template.render(variables)
#	return HttpResponse(output)
	return render_to_response('main_page.html', RequestContext(request))

@csrf_exempt
def user_page(request, username):
	try:
		user = User.objects.get(username = username)
	except:
		raise Http404('Requessted user not found.')
	
	bookmarks = user.bookmark_set.all()
	template = get_template('user_page.html')
	variables = RequestContext(request,
	{
		'username' : username,
		'bookmarks' : bookmarks
	})
	return render_to_response('user_page.html', variables)

@csrf_exempt
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
		return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
	variable = RequestContext(request, 
				{ 'form' : form })
	return render_to_response('registration/register.html', variable)	
