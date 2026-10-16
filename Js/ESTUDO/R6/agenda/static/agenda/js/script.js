function index(){
    let input = document.querySelector('#texto')
    let cards = document.querySelectorAll('.cards')
    let vazio = document.querySelector('#vazio')

    input.addEventListener('input', ()=>{
        let digitado = input.value.toLowerCase()
        v = 0

        cards.forEach(card =>{
            let nome = card.querySelector('.nome').innerText.toLowerCase()

            if(nome.includes(digitado)){
                card.style.display = 'block'
                v++
            }else{
                card.style.display = 'none'
            }

            if(v == 0){
                vazio.style.display = 'block'
            }else{
                vazio.style.display = 'none'
            }

        })

    })
}
function detalhe(){
    let butao = document.querySelector('#butao')
    let atividades = document.querySelector('#atividades')

    butao.addEventListener('click', ()=>{
        if(atividades.style.display == 'none'){
            atividades.style.display = 'block'
            butao.innerText = 'Ocutar atividades'
        }else{
            atividades.style.display = 'none'
            butao.innerText = 'Mostrar atividades'
        }

    })
}