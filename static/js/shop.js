let playername = document.getElementById("mcusername").innerHTML; // Gets Minecraft username from Jinja2 template
let discordID = document.getElementById("discordid").innerHTML.toString(); // Gets Discord ID from Jinja2 template
async function runcommand(command) { 
	/* 
	A command should be a string, but without the slash in Minecraft commands 
	For example, if you want to run "/give Giorno420 minecraft:apple 64", you'd use "give Giorno420 minecraft:apple 64" instead

	You can use onclick event listeners and call this function when they're clicked
	*/
		
	let canBeRan = null; 
	/* 
	if this is false, then the commands will not be run, but if its true, only then will they be run
	these are made false when the user doesnt have enough coins or if they're offline

	you can add your own logic to check for requirements before purchasing
	*/
	console.log(response[discordID])
	let onlineplayerslist = $.getJSON("/getplayerlist", (data) => {
		const playerlist = data.players;
		
		// Player online
		if (playerlist.includes(playername)){ canBeRan = true; }

		// Player offline
		if (!(playerlist.includes(playername))){
			alert("You're not online in the Minecraft server!");
			canBeRan = false;
			return; 
		}
			
	});
		
		
	let particlestr = `{
		"mcusername": "${playername}",
		"discordID": "${discordID}",
		"command": "${command}"
	}`
		
	if (!canBeRan){ return; }

	if (canBeRan){
		fetch(
			"/runcommand", 
			{
				method: "POST",
				headers: {
					"Accept": "application/json", 
					"Content-Type": "application/json"
				}, 
				body: particlestr})
		.then(response => response.json())
		if (response["done"] == "yes"){ alert("Command ran!") }
		else if (response["done"] == "no"){ alert("An error occured"); } // get fucking trol'd
	}
}
