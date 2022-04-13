from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="Stranger"))
    goodbye = String()

    def resolve_hello(root, info, **kwargs):
        return f"Hello {kwargs['name']}!"

    def resolve_goodbye(root, info):
        return "See Ya!"

schema = Schema(query=Query)

query_string = "{ hello }"

result = schema.execute(query_string)
print(result.data['hello'])

query_string = '{ hello(name: "Andrew") }'
result = schema.execute(query_string)
print(result)