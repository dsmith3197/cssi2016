/*adapted from http://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling */
$(document).ready(function(){   
	var scrollStart = 0;
	var changeLocation = $('#description');
	var offset = changeLocation.offset();
	if (changeLocation.length){
	$(document).scroll(function() { 
	  scrollStart = $(this).scrollTop();
	  if(scrollStart + 60 > offset.top) {
	      $("#header").css('background-color', '#133838');
	      $("li a").css('color', 'white');
	   } else {
	      $('#header').css('background-color', 'transparent');
	      $("li a").css('color', 'black');
	   }
	});
	}
});


function setup() {
	$('#title').animate(
    {fontSize: 50},
    1500
	);
}



$(document).ready(setup);