function initialize(){
    var answers = question.answers
    var quiz_id = question.quiz_id
    for (let i = 0; i <Object.keys(answers).length; i++){
        var letter = Object.keys(answers)[i]
        $("#options").append(
            '<div id="labels">'+'<label>'
            + '<input type="radio" name="question'+quiz_id+'" value="'+letter+'">'
            + letter + '. '
            + answers[letter]
          + '</label>'+'</div>'
        )
    }
}
  function checkAnswer() {
    var quiz_id = question.quiz_id
    var answer = (document.querySelector('input[name=question'+quiz_id+']:checked')||{}).value;
    let userAnswer = {}
    if(answer===question.correctAnswer){
        userAnswer["answer"] = "true"
        var success = $('<div class="alert alert-success" role="alert"><i class="bi bi-check" style="font-size: 1.3rem"></i>Correct!</div>')
        $("#res").append(success)
    }else{
        userAnswer["answer"] = "false"
        var fail = $('<div class="alert alert-danger" role="alert"><i class="bi bi-x" style="font-size: 1.3rem"></i>Incorrect</div>')
        $("#res").append(fail)
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
    setTimeout(function(){
        window.location.href = "/quiz/"+ question.next_question
    },1000);
  }

$(document).ready(function () {
    initialize()
    $("#review").click(function(){
        window.location.href = "/review/" + question.quiz_id
    })
});