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
                    'required': ['event', 'timestamp', 'text', 'data', 'message_id', 'parse_data'],
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
                        'data': {
                            'bsonType': 'object',
                            'description': 'Data should be an object'
                        },
                        'message_id': {
                            'bsonType': ['string', 'null'],
                            'description': 'Message id should be null'
                        },
                        'parse_data': {
                            'bsonType': ['string', 'null'],
                            'description': 'Parse data should be null'
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

class BotSchema:
    def __init__(self, bot_json):
        self.bot_json = bot_json

    def store(self):
        create_or_append_collection('bot_event_logs', self.bot_json)

