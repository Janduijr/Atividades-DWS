const forms = document.querySelector('#formulario')
const resultado = document.querySelector('#resultado')

forms.addEventListener('submit', (event)=>{
    event.preventDefault()

    const peso = document.querySelector('#peso').value
    const altura = document.querySelector('#altura').value
    let imc = peso/(altura*altura)

    if (imc < 18.5){
        resultado.innerHTML = (`<p>IMC: ${imc.toFixed(2)} <br> Classificacao: Magreza</p>`)
    } else if (imc >= 18.5 && imc <= 24.9 ) {
        resultado.innerHTML = (`<p>IMC: ${imc.toFixed(2)} <br> Classificacao: Peso normal</p>`)
    } else if (imc >= 25 && imc <= 29.9 ) {
        resultado.innerHTML = (`<p>IMC: ${imc.toFixed(2)} <br> Classificacao: Sobrepeso</p>`)
    } else if (imc >= 30 && imc <= 39.9 ) {
        resultado.innerHTML = (`<p>IMC: ${imc.toFixed(2)} <br> Classificacao: Obesidade</p>`)
    } else if (imc >= 40 ) {
        resultado.innerHTML = (`<p>IMC: ${imc.toFixed(2)} <br> Classificacao: Obesidade grave</p>`)
    }


})