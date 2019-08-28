import graphene
from database import emails

class IEmail(graphene.Interface):
    id = graphene.ID()
    eid = graphene.Int()
    subject = graphene.String()
    content = graphene.String()


class Email(graphene.ObjectType):
    class Meta:
        interfaces = (IEmail,)

class CreateEmail(graphene.Mutation):
    class Arguments:
        subject = graphene.String()
        content = graphene.String()

    ok = graphene.Boolean()
    email = graphene.Field(lambda: Email)

    def mutate(self, info, subject, content):
        email = {
          'eid': emails.count() + 1,
          'subject': subject,
          'content': content
        }
        result = emails.insert_one(email)
        email['id'] = result.inserted_id
        ok = True
        return CreateEmail(email=email, ok=ok)

class Query(graphene.ObjectType):
    emails = graphene.List(Email)
    email = graphene.Field(Email, eid=graphene.Int())

    def resolve_emails(self, info):
      return [e for e in emails.find()]

    def resolve_email(self, info, eid):
      return emails.find_one({ 'eid': eid })

class Mutation(graphene.ObjectType):
    create_email = CreateEmail.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Email])
