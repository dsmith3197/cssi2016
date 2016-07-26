/*adapted from http://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling */

$(document).ready(function(){   
	var scrollStart = 0;
	var changeLocation = $('#description');
	var offset = changeLocation.offset();
	if (changeLocation.length){
	$(document).scroll(function() { 
		scrollStart = $(this).scrollTop();
		if(scrollStart + 60 > offset.top) {
	    	$("#headerHome").fadeIn('slow');
	    	$("li a").css('color', 'white');
		} else {
	    	$('#headerHome').fadeOut('slow');
	    	$("li a").css('color', 'black');
		}
	});
	}
});


$(document).ready(setup);