
function In_image(){
	var verifImg = document.getElementById("Inside");
        var random = Math.random()
	$.ajax({
	    type:'GET',
	    url:'/Pi_image?' + random,
	    success: function() {
		verifImg.setAttribute('src', "Pi_image?" + random);
		console.log("Image Refresh succussed!");
	    },
	    error: function() {
		verifImg.setAttribute("src", "Pi_image?" + random);
	    }
	});
}


window.onload=function initial(){
	x=0;
        function initial_fresh(){
            if(x<2){
             console.log(x);
             In_image();         
             x = x+1;
             setTimeout(initial_fresh,1200);
                }
            };
        initial_fresh();
}



var x=0;


$(document).ready(function() {
        //判断选中还是未选中
        var tog1 = document.getElementById("toggle1");
        var tog2 = document.getElementById("toggle2");
        
        var process_status = Server.docontent; //
    for(var i=0;i<process_status.length;i++){
        arrvalue=process_status[i];//数组的索引是从0开始的
        if (arrvalue ==60){
            tog2.checked = true;};


        console.log(arrvalue);}
        console.log(process_status);
        $(".docontent").html(process_status)
        
        
        $("#toggle1").click(function(){
                if($("#toggle1").is(":checked")===true){
                    x=0;
                    function auto_refresh(){
                        if(x<500){
                                console.log(x);
                                In_image();
                                x = x+1;
                                setTimeout(auto_refresh,1500);
                              }
                        else{
                            tog1.checked = false;
                            }
                        };
                    auto_refresh();
                    
                }else{
                    x=500;
                    }
        });
        
     $("#toggle2").click(function(){
        pin_num = "60";
        var turn_on = "/BlackWhiteOn/" + pin_num;
        var turn_off = "/BlackWhiteOff/" + pin_num;
        if($("#toggle2").is(":checked")===true){
                $.ajax({
                    type:'POST',
                    url: encodeURI(turn_on),
                    success: function() {
                        console.log("Turn on the pin successfully!");
                    },
                    error: function() {
                        alert("Failed to turn the pin");
                        console.log("Failed to turn oon the pin!");
                    }
                });
            }else{
                $.ajax({
                    type:'POST',
                    url: encodeURI(turn_off),
                    success: function() {
                        console.log("Close the pin successfully!");
                    },
                    error: function() {
                        alert("Failed to turn the pin!");
                        console.log("Failed to turn off the pin!");
                    }
                });
            }
        });
        

});
