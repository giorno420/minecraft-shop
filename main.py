import os, json, sqlite3
from database.minecraft import pluginInteractions
from database.minecraft import database as minecraftDB
from flask import Flask, redirect, url_for, render_template, request, abort, jsonify
from flask_discord import DiscordOAuth2Session, requires_authorization


with open("settings.json", 'r') as configjson:
    config = json.load(configjson)

app = Flask("minorities")

app.secret_key = os.urandom(24)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = config['insecuretransport']
app.config["DISCORD_CLIENT_ID"] = config['id']
app.config["DISCORD_CLIENT_SECRET"] = config['secret']
app.config["DISCORD_REDIRECT_URI"] = config['redirect_uri']
app.config['DISCORD_BOT_TOKEN'] = config['token']
discord = DiscordOAuth2Session(app)
playerlist = []

@app.route('/login')
def login():
    return discord.create_session()


@app.route('/callback')
def callback():
    discord.callback()
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    discord.revoke()
    return redirect(url_for('index'))


@app.route('/')
def index():
	return '<a href="/shoplogin">Shop Login page</a><br><br><br>bottom "text"'



@app.route('/shoplogin')
def shopLoginForm():
	if discord.authorized:
		user = discord.fetch_user()
		return render_template('shoplogin.html')
	elif not discord.authorized:
		return redirect(url_for('login'))


@app.route('/shoplogin', methods=['POST'])
@requires_authorization
def shopLoginFormVerification():
	if discord.authorized:
		user = discord.fetch_user()

		username = str(request.form['usernameform'])
		password = str(request.form['passwordform'])

		try:

			if minecraftDB.checkMinecraftVerification(user.id) is True:
				return redirect(url_for('shop'))

			if minecraftDB.checkMinecraftVerification(user.id) is False:
				if minecraftDB.initializeLogin(username, password, str(user.id)) is True:
					minecraftDB.addVerification(str(user.id), username)
					return redirect(url_for('shop'))
					
				elif minecraftDB.initializeLogin(username, password, str(user.id)) is False:
					minecraftDB.redownloadDB()
					return render_template("Wrong Username/Password<br>Make sure you have logged in at least once to our Minecraft server. Also keep in mind that the password is the one you use for the /login command in the server, not your actual Minecraft password")
				
				minecraftDB.initializeLogin(username, password, str(user.id))

		except sqlite3.OperationalError:
					return render_template("Wrong Username/Password<br>Make sure you have logged in at least once to our Minecraft server. Also keep in mind that the password is the one you use for the /login command in the server, not your actual Minecraft password")
		except TypeError:
					return render_template("Wrong Username/Password<br>Make sure you have logged in at least once to our Minecraft server. Also keep in mind that the password is the one you use for the /login command in the server, not your actual Minecraft password")
	elif not discord.authorized:
		return redirect(url_for('login'))


@app.route('/shop')
def shop():

	if discord.authorized:
		user = discord.fetch_user()

		mcusernamefile = json.load(open('database/minecraft/discordminecraftlinking.json'))

		if minecraftDB.checkMinecraftVerification(user.id) is True:
			try:
				return render_template("shop.html", mcusername=mcusernamefile[str(user.id)], discordid=str(user.id))
			except KeyError:
				return redirect(url_for("shopLoginForm"))

		elif minecraftDB.checkMinecraftVerification(user.id) is False:
			return redirect(url_for("shopLoginForm"))
	
	elif not discord.authorized:
		return redirect(url_for("login"))




@app.route('/runcommand', methods=["GET", "POST"])
def runcommand():
	jsonrespons = request.get_json()
	isDone = pluginInteractions.runCommand(command=jsonrespons["command"])
	if isDone:
		done = "yes"
	elif not isDone:
		done = "no"
	return jsonify(done=done)




@app.route('/getplayerlist')
def getplayerlist():
	global playerlist
	players = pluginInteractions.playerList()
	playerlist = []
	for playeriterate in range(len(players)):
		playerlist.append(players[playeriterate]["displayName"])
	return jsonify(players=playerlist)


app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
