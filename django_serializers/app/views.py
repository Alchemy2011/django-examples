import json
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.
from .models import Book


def get_books(requests):
    book = Book.objects.all()
    json_str = serialize('json', book)
    return JsonResponse({'books': json.loads(json_str)})



