$(document).ready(function(){
  $("search").autocomplete({
    source: function(request, response) {
      $.post("/autocomplete/", { 'text': $("search").text() }, function(data, status){
        console.log("Autocomplete status: " + status)
      })
    },
    create: function() {
      //TODO
    }
  })
})
