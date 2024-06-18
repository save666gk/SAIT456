document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav');

    function handleResize() {
        if (window.innerWidth > 768) { // Ширина экрана больше 768px
            nav.style.display = 'block';
            burger.classList.remove('active');
        }
    }

    window.addEventListener('resize', handleResize); // Обработчик изменения размера окна

    burger.addEventListener('click', function() {
        nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
        burger.classList.toggle('active');
    });

    // Проверка состояния при загрузке страницы
    handleResize();
});


// Получаем элемент модального окна
var modal = document.getElementById('myModal');

// Получаем кнопку для открытия модального окна
var btn = document.querySelector('.lesson-info a');

// Получаем элемент <span> (крестик), который закрывает модальное окно
var span = document.getElementsByClassName('close')[0];

// При клике на кнопку открываем модальное окно
btn.onclick = function() {
  modal.style.display = 'block';
}

// При клике на крестик закрываем модальное окно
span.onclick = function() {
  modal.style.display = 'none';
}

// При клике вне модального окна, закрываем его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

function toggleMobileMenu1() {
    const mobileNav1 = document.querySelector('.mobile-nav1');
    mobileNav1.classList.toggle('hide1');
}
