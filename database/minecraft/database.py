import json
import bcrypt
import pysftp
import sqlite3


with open('database/minecraft/discordminecraftlinking.json') as discordminecraftlinkingjson:
	discordminecraftlinking = json.load(discordminecraftlinkingjson)


def redownloadDB():

	with open('settings.json') as configfile_:

		config = json.load(configfile_)
		sftpURL = config["sftpURL"]
		sftpUsername = config["sftpUsername"]
		sftpPassword = config["sftpPassword"]
		sftpPort = config["sftpPort"]
	cnopts = pysftp.CnOpts()
	cnopts.hostkeys = None
	with pysftp.Connection(
		sftpURL, 
		port=sftpPort, 
		username=sftpUsername, 
		password=sftpPassword, 
		cnopts=cnopts
	) as sftp:
		with sftp.cd('plugins'):
			with sftp.cd('AuthMe'):
				sftp.get('authme.db', 'database/minecraft/authme.db')
	sftp.close()


def initializeLogin(enteredUsername, enteredPassword, discorduserid):
    database = sqlite3.connect('database/minecraft/authme.db')
    cursor = database.cursor()
    
    
    credentialsRow = list(cursor.execute('SELECT realname, password FROM authme WHERE realname = ?', (enteredUsername, )).fetchone())

    hashedPassword = credentialsRow[1]
    hashedPassword = str(hashedPassword).encode()

    cursor.close()


    enteredPassword = str(enteredPassword).encode()

    checkpasses = bcrypt.checkpw(password=enteredPassword, hashed_password=hashedPassword)

    if checkpasses:
        return True
    
    elif not checkpasses:
        return False


def saveChanges(changes):

	with open('database/minecraft/discordminecraftlinking.json', 'w') as discordminecraftlinkingjsonfiletosave:
		
		json.dump(changes, discordminecraftlinkingjsonfiletosave)



def addVerification(discordID: int, mcusername: str):

	try:
		if discordminecraftlinking[str(discordID)] is mcusername:
			pass

	except KeyError:
		discordminecraftlinking[str(discordID)] = mcusername
		saveChanges(discordminecraftlinking)
	

def checkMinecraftVerification(discordVerificationID):

	try:
		if discordminecraftlinking[str(discordVerificationID)]:
			return True
		else:
			return False
	
	except KeyError:
		return False


