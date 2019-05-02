$(document).ready(function(){
  $("#filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#user-repositories-list div").filter(function() {
        var visible = $(this).text().toLowerCase().indexOf(value) > -1;
        $(this).toggle(visible);
    });


    var count=$("#user-repositories-list div.repo:visible").length;
    $("#search_count").html(count);
    $("#search_string").html($(this).val());
    if ($(this).val().length>0) {
        $(".user-repo-search-results-summary").show();
    } else {
        $(".user-repo-search-results-summary").hide();
    }

    if (count>0) {
        $(".blankslate").hide();
    } else {
        $(".blankslate").show();
    }
  });
});
