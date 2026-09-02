const lista = document.getElementsByTagName('li');

for (let i = 0; i < lista.length; i ++) {
    if (lista[i].innerText.length > 10) {
        lista[i].style.color = 'blue'
        lista[i].textContent = (lista[i].innerText + '(LIMITADO!)')
    }
}