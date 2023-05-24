from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-date']

class Author(models.Model):

    category = models.ManyToManyField(Category, related_name='cat_author')
    name = models.CharField('Author name', max_length=60)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    name = models.CharField('Book name', max_length=60)
    about = models.TextField('Book about')
    price = models.PositiveIntegerField('Book price')
    date = models.DateTimeField(auto_now=True)
    img = models.ImageField('Book image', upload_to='books')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Cart(models.Model):
    prod = models.ForeignKey(Book, on_delete=models.CASCADE)


class Contact(models.Model):

    contact_email = models.EmailField('Contact email')
    review = models.TextField('Contact review')

    def __str__(self):
        return f'{self.review[:30]}'