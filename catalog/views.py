from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
	"""
	Функция отображения для домашней страницы сайта.
	"""
	# Генерация "количеств" некоторых главных объектов
	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	# Доступные книги (статус = 'a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.

	# Отрисовка HTML-шаблона index.html с данными внутри 
	# переменной контекста context
	
# Number of visits to this view, as counted in the session variable.
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	print('num_visits')

	return render(
	   	request,
	   	'catalog/index.html',
	   	context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
	       	'num_visits':num_visits,} # num_visits appended

    	)

class BookListView(generic.ListView):
	model = Book
	paginate_by = 2
	#context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
	#queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
	#template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения

class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request,pk):
	    try:
	        book_id=Book.objects.get(pk=pk)
	    except Book.DoesNotExist:
	        raise Http404("Book does not exist")
	    #book_id=get_object_or_404(Book, pk=pk)
	    return render(
	        request,
	        'catalog/book_detail.html',
	        context={'book':book_id,}
	    )



# Create your views here.
