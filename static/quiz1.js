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
      var new1 = $("<p data-name='"+list[i]+"' style='text-align: center;padding:5px;font-size:15px;' class='border border-secondary'></p>")
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
    userAnswer["quiz_id"] = question.quiz_id
    if (JSON.stringify(correct_answers) === JSON.stringify(answers)) {
      userAnswer["score"] = 1
      // score += 1
      var success = $('<div class="alert alert-success" style="width:200px;display: flex;align-items: center;" role="alert"><i class="bi bi-check" style="font-size: 1.3rem"></i>Correct!</div>')
      $("#res").append(success)
    } else {
      userAnswer["score"] = 0
      var fail = $('<div class="alert alert-danger" style="width:200px;display: flex;align-items: center;" role="alert"><i class="bi bi-x" style="font-size: 1.3rem"></i>Incorrect</div>')
      $("#res").append(fail)
    }
    // let newScore = {"score":score}
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
    setTimeout(function(){
        window.location.href = "/quiz/"+ question.next_question
    },1000);
}

$(document).ready(function () {
    initialize(initial_pos);
    $("#restart").click(function(){
        window.location.href = window.location.href;
    })
    $("#review").click(function(){
        let userAnswer = {}
        userAnswer["quiz_id"] = question.quiz_id
        userAnswer["score"] = -1
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
        window.location.href = "/review/1"
    })
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