# Message Deleter Bot

Autodeletes messages after a specified amount of time. 

The way that it works is that it first checks a message for a shebang (#!) then it will read the next characters using regex. It will determine if the format matches what the regex is expecting, then it will pick apart the expression, seperating out the unit of time, and how many units should pass before the message is deleted. e.g. #!5s deletes that message in 5 seconds. #!24h is the same as #!1d, and they will both function the same.

if you want to use this, the token should be put in a .env file with the format token={token}


