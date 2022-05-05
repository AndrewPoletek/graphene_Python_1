import graphene
# import main.schema_relay_tutorial
# import main.schema_schema_tutorial
# import main.schema_queries_and_object_types
# import main.schema_fields
# import main.schema_mutations
import main.schema_filtering


class Query(main.schema_filtering.Query, graphene.ObjectType):
    pass

# class Mutation(main.schema_filtering.Mutation, graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query)
