import requests, json


commandURL = json.load(open("/settings.json"))["serverIP"]+"/v1/command"
playerlistURL = json.load(open("/settings.json"))["serverIP"]+"/v1/players"
pluginkey = json.load(open("/settings.json"))["pluginkey"]

headers = {
	"Accept": "application/json",
	"Content-Type": "application/x-www-form-urlencoded", 
	"key": pluginkey
}


def playerList():
	"""Gets a playerlist list from the Minecraft server"""
	return requests.get(playerlistURL).json()

def runCommand(command):
	response = requests.post(url=commandURL, headers=headers, data=command).json()
	try:
		if type(response) == str:
			return True
	except IndexError:
		return False
	except IndexError:
		return False

