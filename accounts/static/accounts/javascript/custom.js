function logoToggle() {
    if($("#logoText").css("display") === "none"){
        console.log("Hello logo");
        $("#logoText").css("display", "block");
        $("#logo").css("width", "25%");
    } else{
        console.log("Bye bye logo");
        $("#logoText").css("display", "none");
        $("#logo").css("width", "75%");
    }
}

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});
