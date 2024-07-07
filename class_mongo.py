import pymongo
from pymongo import MongoClient
import os
import class_log
headerLog={}

def CONN_URI(uri):
    try:
        return MongoClient(uri)
    except:
        return False


def CONN_509(uri,pemPath):
    try:
        return MongoClient(uri,tls=True,tlsCertificateKeyFile=pemPath)
    except:
        return False

def detectConn(byConn):
    startDate=class_log.getDateMillis()
    if byConn["auth"]=="certs":
        clnt=CONN_509(byConn["uri"],byConn["cert_name"])
        if clnt != False:
            class_log.printRowLog("MONGO_CONN","OK","OK",startDate,byConn["auth"])
        else:
            class_log.printRowLog("MONGO_CONN","FD001","CannotCreateClient",startDate,byConn["auth"])
        return clnt
    if byConn["auth"]=="basic":
        fUri=byConn["uri"].replace("USER",str(os.getenv(byConn["user"]))).replace("PASS",str(os.getenv(byConn["pass"])))
        clnt= CONN_URI(fUri)
        if clnt != False:
            class_log.printRowLog("MONGO_CONN","OK","OK",startDate,byConn["auth"])
        else:
            class_log.printRowLog("MONGO_CONN","FD001","CannotCreateClient",startDate,byConn["auth"])
        return clnt
    class_log.printRowLog("MONGO_CONN","FD043","ConnectionNotKnown",startDate,byConn["auth"])
    return False

def makeCount(byClient,query,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.count_documents(query)
        class_log.printRowLog("DB_COUNT","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_COUNT","KO","KO",startDate,str(ValueError))
        return False

def makeFind(byClient,query,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.find(query)
        class_log.printRowLog("DB_READ_MANY","OK","OK",startDate,"")
        arrob=[]
        for rs in vario:
            arrob.append(rs)
        return arrob
    except ValueError:
        class_log.printRowLog("DB_READ_MANY","KO","KO",startDate,str(ValueError))
        return False

def makeFindOne(byClient,query,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.find_one(query)
        class_log.printRowLog("DB_READ_ONE","OK","OK",startDate,"")
        return vario
    except ValueError:        
        class_log.printRowLog("DB_READ_ONE","KO","KO",startDate,str(ValueError))
        return False
def makeFindWithHintIndexAscending(byClient,query,dbs,collections,campoHint): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.find(query).hint([(campoHint, pymongo.ASCENDING)])
        class_log.printRowLog("DB_READ_MANY_HINT","OK","OK",startDate,"")
        arrob=[]
        for rs in vario:
            arrob.append(rs)
        return arrob
    except ValueError:
        class_log.printRowLog("DB_READ_MANY_HINT","KO","KO",startDate,str(ValueError))
        return False
def makeFindWithHintIndexDescending(byClient,query,dbs,collections,campoHint): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.find(query).hint([(campoHint, pymongo.DESCENDING)])
        class_log.printRowLog("DB_READ_MANY_HINT","OK","OK",startDate,"")
        arrob=[]
        for rs in vario:
            arrob.append(rs)
        return arrob
    except ValueError:
        class_log.printRowLog("DB_READ_MANY_HINT","KO","KO",startDate,str(ValueError))
        return False
def makeDeleteMany(byClient,query,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.delete_many(query)
        class_log.printRowLog("DB_DELETE_MANY","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_DELETE_MANY","KO","KO",startDate,str(ValueError))
        return False

def makeDeleteOne(byClient,query,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.delete_one(query)
        class_log.printRowLog("DB_DELETE_ONE","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_DELETE_ONE","KO","KO",startDate,str(ValueError))
        return False

def makeUpdateOne(byClient,query,dbs,collections,byUpdate):
    startDate=class_log.getDateMillis() 
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.update_one(query,byUpdate)
        class_log.printRowLog("DB_UPDATE_ONE","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_UPDATE_ONE","KO","KO",startDate,str(ValueError))
        return False

def makeUpdateMany(byClient,query,dbs,collections,byUpdate): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.update_many(query,byUpdate)
        class_log.printRowLog("DB_UPDATE_MANY","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_UPDATE_MANY","KO","KO",startDate,str(ValueError))
        return False

def makeInsertMany(byClient,documents,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.insert_many(documents)
        class_log.printRowLog("DB_INSERT_MANY","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_INSERT_MANY","KO","KO",startDate,str(ValueError))
        return False

def makeInsertOne(byClient,document,dbs,collections): 
    startDate=class_log.getDateMillis()
    try:
        db = byClient[dbs]
        collection = db[collections]
        vario=collection.insert_one(document)
        class_log.printRowLog("DB_INSERT_ONE","OK","OK",startDate,"")
        return vario
    except ValueError:
        class_log.printRowLog("DB_INSERT_ONE","KO","KO",startDate,str(ValueError))
        return False