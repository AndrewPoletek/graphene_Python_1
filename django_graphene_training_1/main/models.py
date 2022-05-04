from django.db import models

# Create your models here.

class CoverColor(models.Model):
    COVER_COLORS = (
        ('BLACK', 'BLACK'),
        ('RED', 'RED'),
        ('YELLOW', 'YELLOW'),
    )
    color = models.CharField(choices=COVER_COLORS, max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=200)
    cover_color = models.ForeignKey(CoverColor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
    shortcode=models.CharField(max_length=4)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=250)
    ISBN_CODE = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.title} - {self.ISBN_CODE} - {self.author}"
