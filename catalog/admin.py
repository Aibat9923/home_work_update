from django.contrib import admin
from .models import *




# admin.site.register(Author)
# Define the admin class

class AuthorInstanceInline(admin.TabularInline):
	model = AuthorInstance

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
	inlines = [AuthorInstanceInline]

#admin.site.register(Book)
#admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	def get_exstra(self, request, obj=None, **kwargs):
		extra = 0
		return extra

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator


class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
			'fields': ('book','imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back')
		}),
	)




admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorInstance) 