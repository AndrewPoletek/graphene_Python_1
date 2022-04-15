from graphene import ObjectType, String, Schema, ID, DateTime, Float, Boolean
from graphene.types import Scalar

class Message(ObjectType):
    id = ID(default_value=5, required=True)
    subject = String(default_value="Temat testowej wiadomości")
    content = String(default_value="Treść testowej wiadomości")
    date_time_send = DateTime(default_value="2022-13-14 13:34")
    date_time_delivery = DateTime(default_value="2022-13-17 13:34")
    cost = Float(default_value=22.39)
    delivery_report = Boolean(default_value=True)

schema = Schema(query=Message)

query = "{ subject, content, dateTimeSend, dateTimeDelivery, cost, deliveryReport }"
result = schema.execute(query)
print(result)