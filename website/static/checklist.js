
let page = 1;
buttons = document.querySelector('.buttons');
nextbutton = document.querySelector('.btn-next');
function next(){
    const current = document.querySelector('._'+ page);
    const next = document.querySelector('._'+ (page + 1));
    if(next){
    console.log(current);
    current.classList.remove("on");
    current.classList.add("off");
    next.classList.remove('off');
    next.classList.add('on');
    page = page + 1;
    }
    else{ page = page -1;};
    nextbutton.style= "display: none";

};
function prev(){
    const current = document.querySelector('._'+ page);
    const prev = document.querySelector('._'+ (page - 1));
    if(prev){
    console.log(current);
    current.classList.remove("on");
    current.classList.add("off");
    prev.classList.remove('off');
    prev.classList.add('on');
    page = page - 1 ;
    };
    nextbutton.style= "display: all";


};
cabinet = document.querySelector('.cabinet');
special = document.querySelector('.special');



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
    
    