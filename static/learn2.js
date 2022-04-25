
function displayNames(titleData){
        console.log(titleData)
        $(".basicTitle").append("<div>"+titleData[2].name+"</div>")
        $(".detailMan").append("<div>"+titleData[2].descriptionOne+"</div>")
        $(".detailZoom").append("<div>"+titleData[2].descriptionTwo+"</div>")
    }
    $(document).ready(function(){
        displayNames(titleData)
    })
