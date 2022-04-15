import graphene

class Chapter(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Chapter.NEWHOPE:
            return 'New hope chapter'
        return 'Other chapter'

# assert Chapter(4) == Chapter.NEWHOPE

Chapter = graphene.Enum('Chapter', [('NEWHOPE', 4), ('EMPIRE', 5), ('JEDI', 6)])