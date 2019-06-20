
function noRightClick() {
if (event.button==2) {
    alert('You may not right mouse click this page. If you wish to have access to these images, please reach out to the photographer')
    }
}
document.onmousedown=noRightClick
