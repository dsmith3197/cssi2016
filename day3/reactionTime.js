$('#image').hide();
$('#results').hide();
$('#retry').hide();


var startTime;
var endTime;

//makes image appear and starts timer
function showImage(){
	$('#image').show();
	var date = new Date();
	startTime = date.getTime();
}

//set random timeout till image shows up
setTimeout(showImage, Math.random()*9000 + 1);


function imageClicked(){
	console.log("Image Clicked");
    var date = new Date();
    endTime = date.getTime();
    $('#image').hide();
    var reactionTime = (endTime - startTime) / 1000;
    $('#results').text('Your reaction time was ' + reactionTime + ' seconds!');
    $('#results').show();
    $('#retry').show();

    $('#retry').click(retryClicked);
 }

 function retryClicked(){

 	console.log("Button Clicked");
 	$('#results').hide();
 	$('#retry').hide();
 	$('#image').hide();
 	setTimeout(showImage, Math.random()*9000 + 1);
 }


function setup() {
	$('#title').animate(
    {fontSize: 50},
    500
	);
	$('#image').click(imageClicked);
	$('#retry').click(retryClicked);
}


$(document).ready(setup);
