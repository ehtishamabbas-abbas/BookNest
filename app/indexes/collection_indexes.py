async def create_indexes(db):
    # create the index on email field in users collection
    collection = db["users"]
    # Motor's create_index is async and expects index keys as a list of tuples
    await collection.create_index([("email", 1)], unique=True)
    
    print("Indexes created successfully")
