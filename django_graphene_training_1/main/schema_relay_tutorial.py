from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Category, Country, City, Author, Book

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'name': ['exact', 'icontains'],
            'id': ['exact',]
        }
        interfaces = (relay.Node,)

class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = ['title', 'id']
        interfaces = (relay.Node,)

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name', 'country', 'city']
        interfaces = (relay.Node,)



class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    book = relay.Node.Field(BookNode)
    author = relay.Node.Field(AuthorNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_books = DjangoFilterConnectionField(BookNode)