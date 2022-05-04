#https://docs.graphene-python.org/projects/django/en/latest/fields/
from graphene import ObjectType, Schema
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class Query(ObjectType):
    all_categories = DjangoListField(CategoryType)

class Mutation(ObjectType):
    pass