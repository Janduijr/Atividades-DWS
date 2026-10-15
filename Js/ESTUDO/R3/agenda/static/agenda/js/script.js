function index(){
    let input = document.querySelector('#texto')
    let cards = document.querySelectorAll('.card')
    let vazio = document.querySelector('#vazio')

    input.addEventListener('input', ()=>{
        let digitado = input.value.toLowerCase()
        let v = 0
        
        cards.forEach(card =>{
            let nome = card.querySelector('.nome').innerText.toLowerCase()
            if (nome.includes(digitado)){
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
    let mudar = document.querySelector('#botao')
    let atividades = document.querySelector('#atividades')

    mudar.addEventListener('click', ()=>{
        if(atividades.style.display == 'none'){
            atividades.style.display = 'block'
            mudar.innerText = 'Mostrar atividades'
        }else{
            atividades.style.display = 'none'
            mudar.innerText = 'Ocutar atividades'
        }
    })
}