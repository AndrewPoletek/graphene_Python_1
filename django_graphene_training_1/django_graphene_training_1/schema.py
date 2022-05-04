import graphene
# import main.schema_relay_tutorial
# import main.schema_schema_tutorial
# import main.schema_queries_and_object_types
# import main.schema_fields
import main.schema_mutations

class Query(main.schema_mutations.Query, graphene.ObjectType):
    pass

class Mutation(main.schema_mutations.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
