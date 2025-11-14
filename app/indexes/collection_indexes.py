async def create_indexes(db):
    # create the index on email field in users collection
    collection = db["users"]
    await collection.create_index([("email", 1)], unique=True)

    #create the indexes for book collection on title, author name, category, and price
    collection = db["books"]
    await collection.create_index([("title", 1)])
    await collection.create_index([("author.name", 1)])
    await collection.create_index([("category", 1), ("price", 1)])
    await collection.create_index([("price", 1)])
    
    print("Indexes created successfully")
