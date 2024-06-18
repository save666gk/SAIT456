 let horizontScroll = document.querySelector('.keys-cards');
        let leftBtn = document.getElementById('keys-cards');
        let rightBtn = document.getElementById('keys-cards');

        rightBtn.addEventListener('click', ()=>{
            horizontScroll.style.scrollBehavior = "smooth"
            horizontScroll.scrollLeft +=400;
        })