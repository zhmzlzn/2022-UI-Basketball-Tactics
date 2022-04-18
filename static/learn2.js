
function displayNames(titleData){
        console.log(titleData)
        $(".basicTitle").append("<div>"+titleData[1].name+"</div>")
    }
    $(document).ready(function(){
        displayNames(titleData)
    })