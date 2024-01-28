import mongomock

# stub files copied from: https://github.com/sbdchd/mongo-types/tree/main/mongoengine-stubs
from mongoengine import Document, connect

connect(
    "mongoenginetest",
    host="mongodb://localhost",
    mongo_client_class=mongomock.MongoClient,
)


class User(Document):
    name: str
    age: int


print(type(User.objects()))
count = User.objects().count()

# BEFORE stub:
# reveal_type(count)  <-- Type of "count" is "Unknown" ❌
# AFTER stub:
# reveal_type(count)  <-- Type of "count" is "int" ✨

print(count)
