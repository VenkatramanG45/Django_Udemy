from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg, Min, Max

def index(requests):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"), Min("rating"), Max("rating"))
    return render(requests, "base/index.html", {
        "total_number_of_books": num_books,
        "books":books,
        "average_rating": avg_rating
    })

#def book_detail(requests, id):
def book_detail(requests, slug):
    '''try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()'''
    #book = get_object_or_404(Book, pk=id)
    book = get_object_or_404(Book, slug = slug)
    return render(requests, "base/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
# Create your views here.
