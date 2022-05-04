from .models import Category
import graphene
from graphene_django import DjangoObjectType

from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields = "__all__"

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()