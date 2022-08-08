// main function for hiding and showing the elements of sidebar
function maint(event){
    //function for hiding all elements of sidebar
    function hide(){
        let elements = document.getElementsByClassName('menu12');
        for (let i =0 ;i < elements.length ; i++){
            elements[i].style.display = "none";
            // console.log(elements[i]);
        }
    }
    hide();

    //hiding all color boxes oner topics
    var a = document.querySelectorAll(".nav");
    for(var i=0;i<a.length;i++)
    {
        var b= document.querySelector("li.nav-item.hlight");
        if(b) b.classList.remove("hlight");
    }
    // add color box in the selected topic
    event.currentTarget.classList.add("hlight");

    //showing particular topics related to the option 
    var cn = event.currentTarget.className[0];
    var nn = document.getElementsByClassName(cn)[0];
    nn.style.display = "block";
}

//default selection of first topic
window.onload=function def(){
    var pq=document.querySelector(".a1");
    // console.log(pq);
    pq.className += " hlight";
    var pr=document.querySelector(".a");
    // console.log(pr);
    pr.style.display="block";
}

