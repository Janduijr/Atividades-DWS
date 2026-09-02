const lista = document.querySelectorAll('li')

lista.forEach((item) => {
    item.addEventListener('click', () => {
        if (item.innerHTML[1] != 's'){
            item.innerHTML = (`<s>${item.innerHTML}</s>`)
        } else {
            item.innerHTML = item.innerHTML.replace('<s>', '').replace('</s>', '')
        }

    });
});
