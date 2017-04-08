$(document).ready(function(){
  $.post("/search/", { 'text': $("search").text() }, function(data, status){
    console.log("Search status: " + status)
  })
})
