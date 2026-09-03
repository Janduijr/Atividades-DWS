const forms = document.querySelector('#formulario')
const resultado = document.querySelector('#resultado')

forms.addEventListener('submit', (event) =>{
    event.preventDefault()

    const nome = document.querySelector('#nome').value
    const email = document.querySelector('#email').value
    const idade = document.querySelector('#idade').value

    if (nome == '' || email == '' || idade == ''){
        alert('PRENCHA OS DADOS!')
        return
    } else if (nome.length > 20){
        alert('NOME GRANDE DEMAIS! Maximo: 20')
        return
    } else if (idade < 18){
        alert('VOCE E MENOR DE IDADE!')
        return
    }

    resultado.innerHTML = (`<p>NOME: ${nome} <br> EMAIL: ${email} <br> IDADE: ${idade} </p>`)

    



})