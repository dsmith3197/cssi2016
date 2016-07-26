
//day 3 exercises
for (var i = 0; i < 5; i++){
	$('.frame').fadeTo(500, .5);
	$('.frame').fadeTo(500, 1);
}


$('h5').prev().append("<p>I love cake!</p>");
$('.frame #PEP b').addClass("newColor");

function fadeImage() {
  $('img').fadeToggle();
}

$(".the-button").click(function () {
    alert("House Music!! Boots, and Cats, and Boots, and Cats");

    // I don't think they can handle more House Music
    // Let's fade out the element they clicked on.

    $(this).fadeOut();
  }
);

function setupHandlers() {
  $('#android').on('click', fadeImage);
}

$(document).ready(setupHandlers);
