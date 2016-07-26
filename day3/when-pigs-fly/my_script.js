function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function flyWhenClicked() {
    $("#pig").animate({
    	right: '200px'
    	});
}



function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flyPig").click(flyWhenClicked);
}

$(document).ready(setup);
