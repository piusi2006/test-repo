from ncclient import manager

router = {"host": "192.168.0.42", "port": "830", 
          "username": "admin", "password": "test123"}

with manager.connect(host=router['host'], port=router["port"], hostkey_verify=False, username=router["username"], password=router["password"]) as m:
    m.close_session()

