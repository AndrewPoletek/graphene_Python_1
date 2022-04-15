from graphene import ObjectType, String, Schema

class Users(ObjectType):
    username = String(default_value="Szybkiuser")
    password = String(default_value="Jest i haslo")
    first_name = String(default_value="Jan")
    last_name = String(default_value="Nowak")

# Turn off camel case default
schema = Schema(query=Users, auto_camelcase=False)
query = "{ username, password, first_name, last_name }"
result = schema.execute(query)
print(result)

#With turn on camel case!
schema = Schema(query=Users)
query = "{ username, password, firstName, lastName }"
result = schema.execute(query)
print(result)
