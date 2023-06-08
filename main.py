import requests
def sendWSP(message, apikey,gid=0):
    url = "https://whin2.p.rapidapi.com/send"
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": "whin2.p.rapidapi.com"}
    try:
        if gid==0:
            return requests.request("POST", url, json=message, headers=headers)
        else:
            url = "https://whin2.p.rapidapi.com/send2group"
            querystring = {"gid":gid}
            return requests.request("POST", url, json=message, headers=headers, params=querystring)
    except requests.ConnectionError:
        return("Error: Connection Error")

# Testing Section

msg2 = {"text":"Bonjour"}

myapikey = "e490b9fc53mshc63429375f5f05bp1170f2jsnb6082dc533c9"
mygroup = "120363140048868763"

#sendWSP(msg1,myapikey)
sendWSP(msg2, myapikey,mygroup)