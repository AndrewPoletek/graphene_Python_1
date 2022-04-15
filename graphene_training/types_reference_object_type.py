from graphene import ObjectType, String, Schema, Field

class Person(ObjectType):
    class Meta:
        name='myPerson'
        description = "It is description my person!"
    first_name = String(name=String(default_value="Andrzej"))
    last_name = String(name=String(default_value="Połetek"))
    full_name = String()

    def resolve_last_name(parent, info, **kwargs):
        print(kwargs)
        return kwargs['name']

    def resolve_full_name(parent, info, **kwargs):
        print(kwargs)
        return f"Full name is: {parent.first_name} {parent.last_name}"


class Query(ObjectType):
    me = Field(Person)

    # def resolve_me(self):
    #     return self

# schema = Schema(query=Query)
schema = Schema(query=Person)

# print(schema.execute("{ me {fullName, lastName} }"))
print(schema.execute("{lastName, fullName}"))