import uuid
import json
import jsonschema
import random
caratteri = "0123456789ABCDEF"
def genUUID4():
    return uuid.uuid4()
def genEXA(byRange):
    esadecimale = "" 
    for _ in range(byRange):
        esadecimale += random.choice(caratteri) 
    return esadecimale
def genRANbyAlph(byAlph,byRange):
    esadecimale = "" 
    for _ in range(byRange):
        esadecimale += random.choice(byAlph) 
    return esadecimale
def validate_json(json_data, json_schema):
    try:
        schema = json.loads(json_schema)
        data = json.loads(json_data)
        jsonschema.validate(instance=data, schema=schema)        
        return True
    except jsonschema.exceptions.ValidationError as e:
        return False
    except json.decoder.JSONDecodeError as e:
        return False
def array_from_jsonArray_getbyRootField(jsonObj,rootField):
    retArr=[]
    for nst in jsonObj:
        retArr.append(nst[rootField])
    return retArr
def array_from_jsonArray_getbyRootAndSecondField(jsonObj,rootField,secondField):
    retArr=[]
    for nst in jsonObj:
        retArr.append(nst[rootField][secondField])
    return retArr