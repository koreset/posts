from cassandra.cqlengine import columns
from cassandra.cqlengine.connection import setup
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model


setup(hosts=["localhost"], default_keyspace="eeklesia")

class ConcretePost(Model):
    __table_name__ = "posts"
    __keyspace__   = "eeklesia"
    id = columns.UUID(primary_key=True)
    author = columns.Text(index=True)
    text = columns.Text()
    creationdate = columns.DateTime()
    lastmodified = columns.DateTime()


sync_table(ConcretePost)