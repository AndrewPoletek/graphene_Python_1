from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from graphene import relay
from .models import Category

class CategoryNode(DjangoObjectType):
    class Meta:
        model=Category
        filter_fields = {
            'id':['exact'],
             'name':['exact', 'icontains', 'istartswith']
        }
        interfaces=(relay.Node,)

class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_Categories = DjangoFilterConnectionField(CategoryNode)

class Mutation(graphene.ObjectType):
    pass