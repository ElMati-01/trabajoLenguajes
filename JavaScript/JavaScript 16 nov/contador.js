window.addEventListener("keydown", (e)=> {

    if (e.key == "+"){
        incremento()
        incremento1()
    }

    if(e.key == "-"){
        decremento()
        decremento1()
    }
}
);


let contador= 0
const valor= document.getElementById("valor")
const valor1= document.getElementById("valor1")

function incremento(){

    contador+=1
    valor.innerHTML=contador
}

function decremento(){

    if (contador>0){
    contador-=1
    valor.innerHTML=contador
    }

    else{
        contador=0
        valor.innerHTML=contador
    }
}

function incremento1(){

    contador+=1
    valor1.innerHTML=contador
}

function decremento1(){

    if (contador>0){
    contador-=1
    valor1.innerHTML=contador
    }

    else{
        contador=0
        valor1.innerHTML=contador
    }
}


function resetear(){

    contador=0
    valor.innerHTML=contador

}