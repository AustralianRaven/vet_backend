from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer
from json import loads
# Login
# Takes a username and password as part of the request body
# Returns the id and role of the user with the given username and password
# TODO: Add Autorization and session management
# TODO: Add password hashing
# TODO: Test this
@csrf_exempt
def login(request):
	if request.method == 'POST':
		data = loads(request.body)
		user = User.objects.filter(username=data['username'], password=data['password'])
		if user:
			return JsonResponse({'id': user[0].id, 'role': user[0].role})
		else:
			return JsonResponse({'error': 'No user found with that username and password.'})
	else:
		return JsonResponse({'error': 'This endpoint only accepts POST requests.'})
# Register
# Add functionality for users
# Takes a username and password as part of the request body
# Returns the id and role of the newly created user
# TODO: Test this
@csrf_exempt
def register(request):
	if request.method == 'POST':
		data = loads(request.body)
		user = User.objects.filter(username=data['username'])
		if user:
			return JsonResponse({'error': 'A user with that username already exists.'})
		else:
			user = User.objects.create(username=data['username'], password=data['password'])
			return JsonResponse({'id': user.id, 'role': user.role})
	else:
		return JsonResponse({'error': 'This endpoint only accepts POST requests.'})
# Edit
# Update functionality for users
# Takes an id as part of the endpoint and all user fields as part of the request body
# Returns the id and role of the updated user
# TODO: Test this
@csrf_exempt
def edit(request, id):
	if request.method == 'POST':
		data = loads(request.body)
		user = User.objects.filter(id=id)
		if user:
			user.update(username=data['username'], password=data['password'])
			return JsonResponse({'id': user[0].id, 'role': user[0].role})
		else:
			return JsonResponse({'error': 'No user found with that id.'})
	else:
		return JsonResponse({'error': 'This endpoint only accepts POST requests.'})
# Delete
# Delete functionality for users
# Takes an id as part of the endpoint
# Returns a success message if the user was deleted successfully
# TODO: Test this
@csrf_exempt
def delete(request, id):
	if request.method == 'POST':
		user = User.objects.filter(id=id)
		if user:
			user.delete()
			return JsonResponse({'success': 'User deleted successfully.'})
		else:
			return JsonResponse({'error': 'No user found with that id.'})
	else:
		return JsonResponse({'error': 'This endpoint only accepts POST requests.'})
