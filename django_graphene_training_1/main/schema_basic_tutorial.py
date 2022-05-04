import graphene
from graphene_django import DjangoObjectType
from .models import Category, Country, City, Author, Book

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "ISBN_CODE", "author", "description", "price", "category")

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_books = graphene.List(BookType)
    book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))
    category_by_id = graphene.Field(CategoryType, id=graphene.ID(required=True))

    def resolve_all_books(root, info):
        return Book.objects.select_related('author', 'category').all()

    def resolve_book_by_id(root, info, id):
        return Book.objects.select_related('author', 'category').get(id=id)

    def resolve_category_by_id(root, info, id):
        return Category.objects.get(id=id)

schema = graphene.Schema(query=Query)
