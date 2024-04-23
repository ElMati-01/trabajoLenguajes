
let e= 0

function incrementar(){
    e+=1
    resultado()
}

function decrementar(){
    e-=1
    resultado()
}

function resetear(){
    e = 0
    resultado()
}

function resultado(){
    const contador= document.getElementById('contador')
    contador.textContent= e
}