
function displayNames(titleData){
        console.log(titleData)
        $(".basicTitle").append("<div>"+titleData[1].name+"</div>")
<<<<<<< HEAD
        $(".detailMan").append("<div>"+titleData[2].descriptionOne+"</div>")
        $(".detailZoom").append("<div>"+titleData[2].descriptionTwo+"</div>")
=======
>>>>>>> cfa5b882f587aa4ddcbe5cd5227232a9bc2009ed
    }
    $(document).ready(function(){
        displayNames(titleData)
    })