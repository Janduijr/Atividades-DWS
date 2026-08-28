function calculadora(valor1,valor2,operador){

    switch(operador) {
        case '+':
            console.log(`${valor1} + ${valor2} = ${valor1+valor2}`)
            break
        case '-':
            console.log(`${valor1} - ${valor2} = ${valor1-valor2}`)
            break
        case '*':
            console.log(`${valor1} x ${valor2} = ${valor1*valor2}`)
            break
        case '/':
            if (valor1 === 0 && valor2 === 0){
                console.log(`${valor1} / ${valor2} = ${valor1/valor2}`)
                break
            } else {
                console.log('Nao e possivel dividir por 0!')
            }
        default:
            console.log(`Operador Invalido!`)
            break
            
    }
}


const valor1 = 2
const valor2 = 3
const operador = '-'


calculadora(valor1,valor2,operador)