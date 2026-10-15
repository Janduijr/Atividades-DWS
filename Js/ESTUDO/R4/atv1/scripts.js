var titulo = document.querySelector('#titulo')
var butao = document.querySelector('#butao')

butao.addEventListener('click', () =>{
    if (titulo.style.color == 'green'){
        titulo.style.color = 'blue'
        titulo.innerText = 'estou azul'
    }else{
        titulo.style.color = 'green'
        titulo.innerText = 'estou verde'
    }
})

