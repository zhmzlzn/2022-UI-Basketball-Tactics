function add_ball(){
    let ball = $("<img id='ball' src='../static/pic/basketball.png'>")
    $('#board').append(ball)
}

// function get_player(oldp){
    
// }

function display_player(x,y,num,i){
    console.log(x)
    let newd = $("<img class='player_position'>")
    let s = "../static/pic/dot"+num+".png"
    if (num == '0'){
        newd.droppable({
            drop: function(event, ui){
                data.positions[parseInt(ui.draggable.data("i"))].num = 0
                data.positions[i].num = ui.draggable.data("index")
                update_player()
                $(this).css("opacity",1)
            },
            over:function(event, ui){
                $(this).css("opacity",0.3)
            },
            out:function(event, ui){
                $(this).css("opacity",1)
            },
            activate:function(event, ui){
                // $(this).css("opacity",0.8)
                $(this).addClass("shad")
            },
            deactivate:function(event, ui){
                // $(this).css("opacity",1)
                $(this).removeClass("shad")
            }
        })
    } else {
        newd.draggable({
            revert:true,
            helper: function(){
                let newp = $("<img>")
                newp.attr("src",$(this).attr("src"))
                newp.css("width","30px")
                newp.css("height","30px")
                newp.css("z-index",4)
                return newp
            }
        })
        newd.attr("data-index",num)
        newd.attr("data-i",i)
        newd.css("z-index",3)
        if (data.basketball == num){
            $("#ball").css('left',y)
            $("#ball").css("top",x)
        }
    }

    newd.attr('src',s)
    newd.css('left',y)
    newd.css("top",x)
    $('#board').append(newd)
}

function update_player(){
    $('#board').empty()
    $('#board').append(board_pic)
    add_ball()
    $.each(data.positions, function(i, z){
        display_player(z.x,z.y,z.num,i)
        // if (z.num != '0') {
        //     display_player(z.x,z.y,z.num,i)
        // } 
    })
}

$(document).ready(function(){
    update_player();
    $('#q_num').empty();
    $('#q_num').html(data.num);
    $('#action_name').empty();
    $('#action_name').html(data.action);
    $('#step_num').empty();
    $('#step_num').html(data.step);

    $("#restart").click(function(){
        window.location.href = window.location.href;
    })

    $("#review").click(function(){
        let userAnswer = {}
        userAnswer["quiz_id"] = data.id
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
        window.location.href = "/review/"+data.id;
    })

    $("#next").click(function(){
        let r = false
        $.each(data.positions, function(i, z){
            if (z.num != z.correct) {
                r = true
            }
        })
        let userAnswer = {}
        userAnswer["quiz_id"] = data.id
        if (r) {
            userAnswer["score"] = 0
            var fail = $('<div class="alert alert-danger" style="display: flex;align-items: center;" role="alert"><i class="bi bi-x" style="font-size: 1.3rem"></i>Incorrect</div>')
            $("#res").append(fail)
        } else {
            userAnswer["score"] = 1
            // score += 1
            var success = $('<div class="alert alert-success" style="display: flex;align-items: center;" role="alert"><i class="bi bi-check" style="font-size: 1.3rem"></i>Correct!</div>')
            $("#res").append(success)
        }
        // let newScore = {"score": score}
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
            window.location.href = "/quiz/"+data.next;
        },1000); 
    })
})