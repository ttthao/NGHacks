$(document).ready(function(){
  $("search").keypress(function(){
    setTimeout(function(){
      $.post("/autocomplete/", { 'text': $("search").text() }, function(data, status){
        console.log("Status: " + status)
      })
    }, 3000)
  })
})
