from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method == 'POST':
		# Creates an instance of the django creation form.
		form = UserCreationForm(request.POST)
		# Checking to see if information in POST is valid.
		if form.is_valid():
			# Saving the user information.
			# Automatically hashes the password as well. 
			form.save()
			# cleaned_data dictionary contains validated data. 
			username = form.cleaned_data.get('username')
			# Redirects the url pattern to the welcome page. 
			return redirect('welcome')	
	# The else is returned when the user has entered invalid data for the UserCreationForm.
	else:
		# Anything that is not a POST request returns a blank form. 
		form = UserCreationForm()
	# The second parameter directs django to the register template. 
	# The last parameter of render is a dictionary of forms. 
	return render(request, 'user/register.html', {'form': form})

def login(request):
 	return render(request, 'user/login.html')

def welcome(request):
	return render(request, 'user/welcome.html')