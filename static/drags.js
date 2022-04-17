

function display_player(x,y,num){
    console.log(x)
    let newd = $("<div class='player_position'>")
    newd.css('left',y)
    newd.css("top",x)
    if (num=='0') {
        newd.css("background-color","white")
    } else {
        newd.css("background-color","red")
        newd.html(num)
    }
    $('#board').append(newd)
}

function update_player(data){
    console.log(data)
    $('#board').empty()
    $('#board').append(board_pic)
    $.each(data, function(i, z){
        display_player(z.x,z.y,0)
        if (z.num != '0') {
            display_player(z.x,z.y,z.num)
        } 
    })
}

$(document).ready(function(){
    update_player(data.positions);
    $('#q_num').empty();
    $('#q_num').html(data.id);
    $('#action_name').empty();
    $('#action_name').html(data.action);
    $('#step_num').empty();
    $('#step_num').html(data.step);
})