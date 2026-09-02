const cont = document.querySelector('#contador');
const mais = document.querySelector('#aumentar');
const menos = document.querySelector('#diminuir');
let atual = 0;

mais.addEventListener('click', () => {
    atual += 1;
    cont.textContent = (`Atual numero: ${atual}`);
})
menos.addEventListener('click', () => {
    atual -= 1;
    cont.textContent = (`Atual numero: ${atual}`);
})