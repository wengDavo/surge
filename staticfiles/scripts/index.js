let scrollTopLink = document.querySelector(".scrollTopLink");

document.addEventListener('scroll', ()=>{
    scroll = document.documentElement.scrollTop > 100 || document.body.scrollTop > 100;
    if(scroll)
    scrollTopLink.classList.add('showBtn')
    else
    scrollTopLink.classList.remove('showBtn')
})
