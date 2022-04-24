function displayNames(subTitleData){
        console.log(subTitleData)
<<<<<<< HEAD
        $(".subBasicTitleLeft").append("<div>"+subTitleData[1].name+"</div>")
        $(".subBasicTitleRight").append("<div>"+subTitleData[2].name+"</div>")
=======
        $(".subBasicTitleLeft").append("<div>"+subTitleData[0].name+"</div>")
        $(".subBasicTitleRight").append("<div>"+subTitleData[1].name+"</div>")
>>>>>>> cfa5b882f587aa4ddcbe5cd5227232a9bc2009ed
    }
    $(document).ready(function(){
        displayNames(subTitleData)
    })