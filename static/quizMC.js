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
        alert("Correct :)");
        userAnswer["answer"] = "true"
    }else{
        alert("Not Correct :(");
        userAnswer["answer"] = "false"
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
    initialize()

});