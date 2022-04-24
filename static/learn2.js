
function displayNames(titleData){
        console.log(titleData)
        $(".basicTitle").append("<div>"+titleData[1].name+"</div>")
        $(".detailMan").append("<div>"+titleData[1].descriptionOne+"</div>")
        $(".detailZoom").append("<div>"+titleData[1].descriptionTwo+"</div>")
    }
    $(document).ready(function(){
        displayNames(titleData)
    })