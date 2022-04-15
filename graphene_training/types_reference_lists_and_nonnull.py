import graphene

#TODO: Totaly unusable scalars at this moment i don't know how to use it, ill back here in the future
class Character(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)
    appears_in = graphene.List(graphene.String)
    my_non_null_list = graphene.List(graphene.NonNull(graphene.String))


schema = graphene.Schema(query=Character)
#TODO: No execute here becouse scalars from this lesson are totaly unusable maybe ill back here in the future
#Im set it as todo