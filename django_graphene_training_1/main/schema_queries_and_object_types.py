import graphene
from graphene_django import DjangoObjectType
from .models import Category, Country, City, Author, Book, CoverColor


class CoverColorType(DjangoObjectType):
    class Meta:
        model = CoverColor
        fields = ("id", "color")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

    extra_field = graphene.String()

    def resolve_extra_field(root, info, **kwargs):
        return "It is extra function or something here!"

class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        exclude = ("name",)

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    countries = graphene.List(CountryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.String())
    cover_colors = graphene.List(CoverColorType)

    def resolve_categories(root, info, **kwargs):
        print(info.context.user)
        return Category.objects.all()

    def resolve_countries(root, info, **kwargs):
        return Country.objects.all()

    def resolve_category_by_id(root, info, **kwargs):
        return Category.objects.get(pk=kwargs['id'])

class Mutation(graphene.ObjectType):
    pass