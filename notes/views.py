from django.http import JsonResponse
from .models import Note
from .serializers import NoteSerializer
from json import loads, dumps

def show(request, id):
	note = Note.objects.get(id=id)
	return JsonResponse(note, safe=False)

def create(request):
	note = loads(request.body)
	serializer = NoteSerializer(data=note)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, safe=False)
	return JsonResponse(serializer.errors, safe=False)

def update(request, id):
	note = Note.objects.get(id=id)
	updated_note = loads(request.body)
	serializer = NoteSerializer(note, data=updated_note)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, safe=False)
	return JsonResponse(serializer.errors, safe=False)

def delete(request, id):
	note = Note.objects.get(id=id)
	note.delete()
	return JsonResponse("Deleted note with id: " + str(id), safe=False)
