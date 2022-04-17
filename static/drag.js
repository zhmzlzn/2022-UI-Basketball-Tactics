function display_player(x,y,num){
    let newd = $("<div class='player_position'>")
    newd.attr('left',x)
    newd.attr("top",y)
    if (num=='0') {
        newd.attr("background-color","white")
    } else {
        newd.attr("background-color","red")
        newd.html(num)
    }
    $('#board').append(newd)
}

function update_player(data){
    $('#board').empty()
    $('#board').append(board_pic)
    $.each(data, function(i, z){
        display_player(z.x,z.y,0)
        if (z.num != '0') {
            display_player(z.x,z.y,z.num)
        } 
    })
}

$(function(){
    update_player(data.positions)
    $('#q_num').empty()
    $('#q_num').html(data.id)
    $('#action_name').empty()
    $('#action_name').html(data.action)
    $('#step_num').empty()
    $('#step_num').html(data.step)
})