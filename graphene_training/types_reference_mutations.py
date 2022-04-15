import graphene

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

class CreatePerson(graphene.Mutation):
    class Arguments:
        name= graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok =True
        return CreatePerson(person=person, ok=ok)

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema = graphene.Schema(query=Query, mutation=MyMutations)

result = schema.execute("""
mutation myFirstMutation{
    createPerson(name: "Peter"){
        person {
            name
        }
        ok
    }
}
""")

print(result)