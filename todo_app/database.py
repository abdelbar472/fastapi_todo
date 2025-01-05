from cassandra.cluster import Cluster

def get_db_session():
    cluster = Cluster(['127.0.0.1'])  # Replace with ScyllaDB IP
    session = cluster.connect()
    session.set_keyspace('todo_app')
    return session
