from pymongo import MongoClient, errors

def create_or_append_collection(coll_name, data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.rasa
    
    # Check if the collection exists
    if coll_name in db.list_collection_names():
        print(f"Collection '{coll_name}' already exists. Appending data.")
    else:
        # Create the collection with the specified schema
        try:
            db.create_collection(coll_name, validator={
                '$jsonSchema': {
                    'bsonType': 'object',
                    'additionalProperties': True,
                    'required': ['event', 'timestamp', 'text', 'message_id', 'parse_data', 'data'],
                    'properties': {
                        'event': {
                            'bsonType': 'string',
                            'description': 'Event should be a string'
                        },
                        'timestamp': {
                            'bsonType': 'double',
                            'description': 'Timestamp should be a double'
                        },
                        'text': {
                            'bsonType': 'string',
                            'description': 'Text should be a string'
                        },
                        'message_id': {
                            'bsonType': 'string',
                            'description': 'Message id should be a string'
                        },
                        'parse_data': {
                            'bsonType': 'object',
                            'description': 'Parse data should be an object'
                        },
                        'data': {
                            'bsonType': ['string', 'null'],
                            'description': 'Data should be null'
                        }
                    }
                }
            })
            print(f"Created collection: '{coll_name}'")
        except errors.CollectionInvalid:
            print(f"Failed to create collection '{coll_name}' (it may already exist).")

    # Append new data to the collection
    if isinstance(data, list):
        result = db[coll_name].insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} documents into '{coll_name}'.")
    else:
        result = db[coll_name].insert_one(data)
        print(f"Inserted 1 document into '{coll_name}'.")

class UserSchema:
    def __init__(self, user_json):
        self.user_json = user_json

    def store(self):
        create_or_append_collection('user_event_logs', self.user_json)

