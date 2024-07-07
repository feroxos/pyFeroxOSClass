import os
from datetime import datetime
import time
import class_string
logCostant={}
canale_di_provenienza=""
def getDateMillis():
    return int(time.time() * 1000)
def printRowLog(tipo_evento,return_code_evento,desc_return_code_evento,startDate,infoRow):    
    endtDate= getDateMillis()
    tempoEse=endtDate-startDate    
    dataAct=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z"
    objJsonPrint={
        "timestamp":dataAct,
        "app_name":os.getenv("LOG_APP_NAME"),
        "servizio_applicativo":os.getenv("LOG_SERVIZIO_APPLICATIVO"),
        "id_univoco":logCostant["businessID"],
        "HEADER_TRANSACTION_ID":logCostant["transactionID"],
        "tipo_evento":tipo_evento,
        "return_code_evento":return_code_evento,
        "desc_return_code_evento":desc_return_code_evento,
        "canale_di_provenienza":canale_di_provenienza,
        "tempo_di_esecuzione":tempoEse,
        "Evento":{
            "start":startDate,
            "end":endtDate,
            "infoRow":infoRow
        }}
    
    print(dataAct+" INFO ["+os.getenv("LOG_APP_NAME")+","+class_string.genEXA(6)+","+class_string.genEXA(6)+"] [E2E] "+str(objJsonPrint))
