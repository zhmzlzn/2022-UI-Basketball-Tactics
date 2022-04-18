function displayNames(subTitleData){
        console.log(subTitleData)
        $(".subBasicTitleLeft").append("<div>"+subTitleData[0].name+"</div>")
        $(".subBasicTitleRight").append("<div>"+subTitleData[1].name+"</div>")
    }
    $(document).ready(function(){
        displayNames(subTitleData)
    })