var initial_pos = [
  "Power Forward",
  "Small Forward",
  "Point Guard",
  "Center",
  "Shooting Guard"
]

var correct_answers = [
    "Point Guard",
    "Shooting Guard",
    "Small Forward",
    "Power Forward",
    "Center"
]

function initialize(list){
    $("#options").empty()
    for (let i = 0; i <list.length; i++) {
      var new1 = $("<p data-name='"+list[i]+"'></p>")
      $(new1).text(list[i])
      $("#options").append(new1)
    }
}

function checkAnswer() {
    const targets = document.querySelectorAll('.target');
    let answers = new Array();
    targets.forEach(function (text) {
      answers.push(text.textContent);
      console.log(text.textContent)
    });
    let userAnswer = {}
    if (JSON.stringify(correct_answers) === JSON.stringify(answers)) {
      alert("Correct :)");
      userAnswer["answer"] = "true"
    } else {
      alert("Not Correct :(");
      userAnswer["answer"] = "false"
      // console.log(JSON.stringify(correct_answers))
      // console.log(JSON.stringify(answers))
    }
    $.ajax({
        type: "POST",
        url: "/count",
        // dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(userAnswer),
        success: function(result){
            console.log(userAnswer)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function () {
initialize(initial_pos);
});

$(function() {
    var $options = $( "#options" );
    $( "p", $options ).draggable({
      revert: "invalid",
      cursor: "move"
    });
    for (let i = 1; i <= correct_answers.length; i++) {
        $("#t"+i).droppable({
            accept: "#options > p",
            drop: function (event, ui) {
                $("#t"+i).empty()
                var new1 = $("<p data-name='" + ui.draggable.attr('data-name') + "'></p>")
                $(new1).text(ui.draggable.attr('data-name'))
                $("#t"+i).append(new1)
                $(ui.draggable).remove();
            }
        })
    }
})