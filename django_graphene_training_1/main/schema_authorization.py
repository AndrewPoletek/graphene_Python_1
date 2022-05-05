#Authorization can be make by few ways i will write about it here becouse it is more django feature than graphql feature it is not element of training.

#1.Limiting access fields by set field or exclude in DjangoObjectType
#2. Query set filtering by owner of row or something different
#3. Use LoginRequireMixin for GraphQLView like here:
#class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
#    pass

