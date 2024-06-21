from pymongo import MongoClient



client =  MongoClient(host='')
database = client.database_2
table = database.collection_2



def insertData(data):
    check = table.insert_one(data)
    if(check):
        return True
    else:
        return False

def viewData():
    array = list()
    it = table.find()
    for i in it:
        i['_id'] = str(i['_id'])
        array.append(i)
    return array

def checkData(data):
    it = table.find_one(filter={"name":data['name'], "password":data['password']})
    if(it):
        return True
    else:
        return False
    
        
    