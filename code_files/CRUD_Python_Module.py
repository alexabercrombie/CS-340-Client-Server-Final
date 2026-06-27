# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    '''def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)]'''
        
    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS =  password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result = self.database.animals.insert_one(data)  # data should be dictionary  
            return result.acknowledged
        else: 
            return false

    
    # Create method to implement the R in CRUD.
    def read(self, data):
        results = []
        if data != None:
            try: 
                results = list(self.database.animals.find(data))
                return results
            except:
                return results
        else:
            return results
        
        
    # Update function to update all documents matching the query data    
    def update(self, data, updateData):
        result = {}
        if data != None:
            try:
                result = self.database.animals.update_many(data, updateData)
                return result.modified_count
            except:
                return result

            
    # Delete function to delete all documents that match the query data        
    def delete(self, data):
        if data != None:
            try: 
                results = self.database.animals.delete_many(data)
                return results.deleted_count
            except:
                return 0
        