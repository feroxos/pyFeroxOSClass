import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os
import class_log
headerLog={}

def get_with_basic_auth_and_header(url, auth_username, auth_password, headers ,timeout):
    startDate=class_log.getDateMillis()
    try:
        resInt=requests.get(url, auth=HTTPBasicAuth(auth_username, auth_password), headers=headers,timeout=timeout)
        response = { 
            "res":resInt.text,
            "code":resInt.status_code
        }
        class_log.printRowLog("EXTERNAL_CALL",response["code"],"UNDEF",startDate,url)
        return response
    except:
        class_log.printRowLog("EXTERNAL_CALL","KO","UNDEF",startDate,url)
        return {"res":"Errore during http_request","code":-1}    
def post_with_basic_auth_and_header(url, auth_username, auth_password, data, headers,timeout):
    startDate=class_log.getDateMillis()
    try:
        resInt = requests.post(url, data=data, auth=HTTPBasicAuth(auth_username, auth_password), headers=headers,timeout=timeout)  
        response = { 
            "res":resInt.text,
            "code":resInt.status_code
        }
        class_log.printRowLog("EXTERNAL_CALL",response["code"],"UNDEF",startDate,url)
        return response
    except:        
        class_log.printRowLog("EXTERNAL_CALL","KO","UNDEF",startDate,url)
        return {"res":"Errore during http_request","code":-1}    
def get_with_header(url,  headers,timeout):
    startDate=class_log.getDateMillis()
    try:        
        resInt = requests.get(url, headers=headers,timeout=timeout)
        response = { 
            "res":resInt.text,
            "code":resInt.status_code
        }
        class_log.printRowLog("EXTERNAL_CALL",response["code"],"UNDEF",startDate,url)
        return response
    except:        
        class_log.printRowLog("EXTERNAL_CALL","KO","UNDEF",startDate,url)
        return {"res":"Errore during http_request","code":-1}  
def post_with_header(url,  data, headers,timeout):
    startDate=class_log.getDateMillis()
    try:
        resInt = requests.post(url, data=data, headers=headers,timeout=timeout)
        ##print(resInt.status_code)
        #print(str(resInt))
        response = { 
            "res":resInt.text,
            "code":resInt.status_code
        }
        
        class_log.printRowLog("EXTERNAL_CALL",response["code"],"UNDEF",startDate,url)
        return response
    except ValueError:
        print(ValueError)
        class_log.printRowLog("EXTERNAL_CALL","KO","UNDEF",startDate,url)
        return {"res":"Errore during http_request","code":-1}  
def generate_header(bid,tid,mid,sid,sourceS,channel):
    return {
        "Accept":"application/json",
        "cache-control":"no-cache",
        "interactionDate-date":datetime.now().strftime('%Y-%m-%d'),
        "interactionDate-time": datetime.now().strftime('%H:%M:%S.%f')[:-3],
        "businessID":bid,
        "messageID":mid,
        "sessionID":sid,
        "transactionID":tid,   
        "sourceSystem":sourceS,     
        "channel":channel}
def generate_header_to_send(byGenerated):
    arrToSend=[]
    arrToSend.append({"header":"Accept","value":byGenerated["Accept"]})
    arrToSend.append({"header":"cache-control","value":byGenerated["cache-control"]})
    arrToSend.append({"header":"interactionDate-date","value":byGenerated["interactionDate-date"]})
    arrToSend.append({"header":"interactionDate-time","value":byGenerated["interactionDate-time"]})
    arrToSend.append({"header":"businessID","value":byGenerated["businessID"]})
    arrToSend.append({"header":"messageID","value":byGenerated["messageID"]})
    arrToSend.append({"header":"sessionID","value":byGenerated["sessionID"]})
    arrToSend.append({"header":"transactionID","value":byGenerated["transactionID"]})
    arrToSend.append({"header":"sourceSystem","value":byGenerated["sourceSystem"]})
    arrToSend.append({"header":"channel","value":byGenerated["channel"]})
    return arrToSend
def queryElk(byElkCfg,byQuery,indice,byHeaders):
    return post_with_basic_auth_and_header(byElkCfg["uri"]+indice+"/_search", os.getenv(byElkCfg["user"]),  os.getenv(byElkCfg["pass"]), byQuery, byHeaders,120)

