function index(){
    let input = document.querySelector('#texto')
    let cards = document.querySelectorAll('.cards')
    let vazio = document.querySelector('#vazio')


    input.addEventListener('input', ()=>{
        let conteudo = input.value.toLowerCase()
        v = 0

        cards.forEach(card =>{
            let nome = card.querySelector('.nome').innerText.toLowerCase()
            if(nome.includes(conteudo)){
                card.style.display = 'block'
                v++
            }else{
                card.style.display = 'none'
            }
        })

        if(v == 0){
            vazio.style.display = 'block'
        }else{
            vazio.style.display = 'none'
        }

    })
}

function detalhe(){
    let butao = document.querySelector('#butao')
    let div = document.querySelector('#atividades')

    butao.addEventListener('click', ()=>{
        if(div.style.display == 'block'){
            div.style.display = 'none'
            butao.innerText = 'Mostrar atividades'
        }else{
            div.style.display = 'block'
            butao.innerText = 'Ocutar atividades'
        }
    })



}

