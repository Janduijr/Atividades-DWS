const ano = 2018
const idade = 2026-ano

console.log(`Idade: ${idade}`)
if (idade < 16){
    console.log('Nao pode votar!')
    console.log('Esta insenta do serviço militar!')
} else if (idade >= 16 && idade < 18){
    console.log('Voto opcional!')
    console.log('Esta insenta do serviço militar!')
} else if (idade >= 18){
    console.log('Voto obrigatorio!')
    console.log('serviço militar obrigatorio!')
}