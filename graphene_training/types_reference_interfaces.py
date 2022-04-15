import graphene

class Character(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    friends = graphene.List(lambda: Character)

class Starship(graphene.Interface):
    id = graphene.ID(required=True)
    name= graphene.String(required=True)

class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character,Starship)

    starships = graphene.List(Starship)
    home_planet = graphene.String()

class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character,)

    primary_function = graphene.String()

class Query(graphene.ObjectType):
    hero = graphene.Field(Character,
                          required=True,
                          episode=graphene.Int(required=True)
                          )
    def resolve_hero(root, info, episode):
        if episode==5:
            return get_human(name='Luke Skywalker')
        return get_droid(name='R2-D2')

schema = graphene.Schema(query=Query, types=[Human, Droid])

print(schema.execute("""
query HeroForEpisode($episode: Int!) {
    hero(episode: $episode) {
        __typename
        name
        ... on Droid {
            primaryFunction
        }
        ... on Human {
            homePlanet
        }
    }
}
""",variables={'episode': 4}))