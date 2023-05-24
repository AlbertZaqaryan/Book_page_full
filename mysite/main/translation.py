from .models import Category, Author, Book
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'about')