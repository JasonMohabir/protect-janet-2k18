$(function() {
  var cursor;
  $('#cmd').click(function() {
    $('input').focus();
    cursor = window.setInterval(function() {
      if ($('#cursor').css('visibility') === 'visible') {
        $('#cursor').css({
          visibility: 'hidden'
        });
      } else {
        $('#cursor').css({
          visibility: 'visible'
        });
      }
    }, 500);

  });

  $('input').keyup(function() {
    $('#cmd span').text($(this).val());
  });

  $('input').blur(function() {
    clearInterval(cursor);
    $('#cursor').css({
      visibility: 'visible'
    });
  });
});


function getBotResponse() {
    var rawText = $("#textInput").val();
  
    var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    $.get("/get", { msg: rawText }).done(function(data) {
      if (data.indexOf("<br") > -1){
      responsiveVoice.speak(data.substring(0, data.indexOf("<br")));
    }
      else if (data.indexOf("<img") > -1){
      responsiveVoice.speak(data.substring(0, data.indexOf("<img")));
    }
    else{
      responsiveVoice.speak(data);
    }
      var botHtml = '<p class="botText"><span>' + data + '</span></p>';
      $("#chatbox").append(botHtml);

      document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    });
  }
  $("#textInput").keypress(function(e) {
      if(e.which == 13) {
          getBotResponse();
      }
  });
  $("#buttonInput").click(function() {
    getBotResponse();
  })