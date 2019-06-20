/*
 Toggle switch for light dark mode functionality
*/

const toggleSwitch = document.getElementById('checkbox');
const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
const themeText = document.getElementById('theme-text');
// var fixedBg = document.querySelector('.fixed-bg');
// console.log(fixedBg);

function switchTheme(e) {
    console.log('switchtheme');
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme','light');
        localStorage.setItem('theme','light');
        // fixedBg.style.backgroundImage= "url('/images/abstract-light-bg.jpg')";
        // themeText.innerText = 'Light';
    } else {
        document.documentElement.setAttribute('data-theme','dark');
        localStorage.setItem('theme','dark');
        // fixedBg.style.backgroundImage= "url('/images/abstract-dark-bg.jpg')";
        // themeText.innerText = 'Dark';
    }
}

if (currentTheme) {
    document.documentElement.setAttribute('data-theme',currentTheme);

    if ( currentTheme === 'light') {
        toggleSwitch.checked = true;
        // themeText.innerText = 'Light';

    } else {
        // themeText.innerText = 'Dark';
    }
}

toggleSwitch.addEventListener('change',switchTheme,false);
// addEvents(toggleSwitch);