
let page = 1;
const cabinet = document.querySelector('.cabinet');
const special = document.querySelector('.special');
const header = document.getElementById("header");
buttons = document.querySelector('.buttons');
nextbutton = document.querySelector('.btn-next');

function next(){
    console.log(header);
    const current = document.querySelector('._'+ page);
    const next = document.querySelector('._'+ (page + 1));
    if(next && page <= 10){
        if(special.classList.contains("checked")){
            header.innerHTML = "הזמנות מיוחדות";
    /*console.log(current);*/
    current.classList.remove("on");
    current.classList.add("off");
    next.classList.remove('off');
    next.classList.add('on');
    page = page + 1;
    };
   /* nextbutton.style= "display: none";*/
   
    };

    if(next && page <= 10 || next && page >= 11){
        if(cabinet.classList.contains("checked")){
            header.innerHTML = "הזמנות ארגזים";
    /*console.log(current);*/
    current.classList.remove("on");
    current.classList.add("off");
    if(page<11){page=11;};
    const nextfar = document.querySelector('._'+ (page + 1));
    nextfar.classList.remove('off');
    nextfar.classList.add('on');
    page = page + 1;
    };
   /* nextbutton.style= "display: none";*/
   console.log(page);
    };
    
};
function prev(){
    const current = document.querySelector('._' + page);
    const prev = document.querySelector('._' + (page - 1));
    if(prev && !prev.classList.contains("far")){
        
    console.log(current);
    current.classList.remove("on");
    current.classList.add("off");
    prev.classList.remove('off');
    prev.classList.add('on');
    page = page - 1 ;
    };
    if(prev && prev.classList.contains("far")){
        current.classList.remove("on");
        current.classList.add("off");
        page = 1;
        
        const nextfar = document.querySelector('._'+ (page));
        nextfar.classList.remove('off');
        nextfar.classList.add('on');
        
        };
        if(page == 1)header.innerHTML = "Choose Your DESTINY!!!";
    nextbutton.style= "display: all";
    console.log(page);


};


cabinet.addEventListener("click" , (e)=>{ 
    console.log(e.target);
    cabinet.classList.add("checked");
    special.classList.remove("checked");
    buttons.style= "display: flex";

});


special.addEventListener("click" , (e)=>{ 
    console.log(e.target);
    special.classList.add("checked");
    cabinet.classList.remove("checked");
    buttons.style= "display: flex";
});
    
    