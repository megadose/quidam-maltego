#The Content has been made available for informational and educational purposes only
from quidam import *
from MaltegoTransform import *
import json

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
username = mt.getValue()
mt = MaltegoTransform()

info = instagram(username)
if '"status"' not in info:
    if info !="lien":
        mt.addEntity("maltego.EmailAddress"," instagram "+info)
    else:
        mt.addEntity("maltego.Phrase","Not informations found in Instagram")
else:
    mt.addEntity("maltego.Phrase",username+" account not found in instagram")


info = twitter(username)
if len(info)==2:
    mt.addEntity("maltego.PhoneNumber","0X XX XX XX "+str(info["phone"]))
    mt.addEntity("maltego.EmailAddress","Twitter "+info["email"])
elif len(info)==1 :
    mt.addEntity("maltego.EmailAddress","Twitter "+info["email"])
else:
    mt.addEntity("maltego.Phrase","Not informations found in Twitter")

info = github(username)
if len(info)==0:
    mt.addEntity("maltego.Phrase","Not informations found in github")
else:
    for e in info:
        mt.addEntity("maltego.EmailAddress",""+e["email"]+" for "+e["name"] +"in github")

mt.returnOutput()
