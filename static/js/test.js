
In_image = function(){
	var verifImg = document.getElementById("Inside");
	$.ajax({
	    type:'GET',
	    url:'/Pi_image',
	    success: function() {
		verifImg.setAttribute('src', "Pi_image");
		console.log("Image Refresh succussed!");
	    },
	    error: function() {
		verifImg.setAttribute("src", "Pi_image");
	    }
	});
}


