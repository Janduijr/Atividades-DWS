const preco = 200;
const quantidade = 2;
const subtotal = preco*quantidade;

console.log(`Subtotal da compra: ${subtotal}`)

if (subtotal > 100 && subtotal <= 300){
    console.log(`Subtotal com desconto de 5%: ${subtotal-(subtotal*0.05)}`)
} else if (subtotal > 300){
    console.log(`Subtotal com desconto de 10%: ${subtotal-(subtotal*0.10)}`)
}
