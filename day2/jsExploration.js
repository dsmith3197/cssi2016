//1

function findLongestLength(words){
	var longest = words[0].length;

	for(var i = 0; i < words.length; i++){
		if(words[i].length > longest){
			longest = words[i].length;
		}
	}
	return longest;
}

function niceRegularBox(words){
	var width = findLongestLength(words) + 4;
	var horizontalBars = ""
	for(var i = 0; i < width; i++){
		horizontalBars += "-";
	}

	console.log(horizontalBars);

	for(var i = 0; i < words.length; i++){
		var line = "| " + words[i];

		var spaces = width - 4 - words[i].length
		var blankSpace = "";
		for(var n = 0; n < spaces; n++){
			blankSpace += " ";
		}
		line += blankSpace;
		line += " |";

		console.log(line);
	}
	
	console.log(horizontalBars);
}

niceRegularBox(["Grim", "visaged", "War", "hath", "smooth'd", "his", "wrinkled", "front"]);


//2
function stringToMorse(message){
	key = {"a":"dot dash", "b":"dash dot dot dot", "c":"dash dot dash dot", "d":"dash dot dot", "e":"dot", "f":"dot dot dash dot", "g":"dash dash dot", "h":"dot dot dot dot", "i":"dot dot", "j":"dot dash dash dash", "k":"dash dot dash", "l":"dot dash dot dot", "m":"dash dash", "n":"dash dot", "o":"dash dash dash", "p":"dot dash dash dot", "q":"dash dash dot dash", "r":"dot dash dot", "s":"dot dot dot", "t":"dash", "u":"dot dot dash", "v":"dot dot dot dash", "w":"dot dash dash", "x":"dash dot dot dash", "y":"dash dot dash dash", "z":"dash dash dot dot"};
	for(var i = 0; i < message.length; i++){
		console.log(key[message[i].toLowerCase()]);
	}
}

stringToMorse("Jacob");

//3
function square(index){
	var result = 1;
	for(var i = 1; i < index; i++)
	{
		result *= 2;
	}
	return result;
}

console.log(square(5));

function total(index)
{
	var total = 0;
	for(var i = 1; i <= index; i++){
		total += square(i);
	}
	return total;
}
console.log(total(4));


//4

function pressFloorNumber(elevatorLine, floor){
	elevatorLine.push(floor);
	return "Position " + elevatorLine.length;
}
function goToNextFloor(elevatorLine){
	if(elevatorLine.length==0){
		return "There are no more floors to go to!";
	}
	var nextLevel = elevatorLine[0];
	elevatorLine.splice(0,1);
	return "Floor " + nextLevel;
}
function currentLine(elevatorLine){
	if(elevatorLine.length==0){
		return "The line is currently empty";
	}
	var message = "The line is currently: "
	for(var i = 0; i < elevatorLine.length; i++){
		if(i < elevatorLine.length - 1){
			message += "Floor " + elevatorLine[i] + ", ";
		} 
		else {
			message += "Floor " + elevatorLine[i];
		}
	}
	return message;
}

var elevatorLine = [];

console.log(currentLine(elevatorLine));
console.log(pressFloorNumber(elevatorLine, 6));
console.log(pressFloorNumber(elevatorLine, 3));
console.log(goToNextFloor(elevatorLine));
console.log(pressFloorNumber(elevatorLine, 12));
console.log(pressFloorNumber(elevatorLine, 5));
console.log(currentLine(elevatorLine));
console.log(goToNextFloor(elevatorLine));
console.log(currentLine(elevatorLine));
console.log(goToNextFloor(elevatorLine));
console.log(goToNextFloor(elevatorLine));
console.log(goToNextFloor(elevatorLine));




function test(functionName, argument){
	return functionName(argument);
}

test(stringToMorse, "Doug");
