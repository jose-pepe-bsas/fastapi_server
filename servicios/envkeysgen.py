from dotenv import load_dotenv
from os import environ,path 
import os
import random as m 
import hashlib as a


def generate_env_key_value():
    h = a.new('sha256')
    h.update(bytes(m.randrange(10)))
    return h.hexdigest()
    


def read_env_key(key_name:str) -> str:
    load_dotenv()
    return environ[key_name]

def set_key(key_name:str,key:str):
    if path.isfile(".enr") is False:
        open(".env",'a').close()
    with open(".env",mode='a') as dot:
        to_write = key_name+"="+key
        dot.write(to_write)
