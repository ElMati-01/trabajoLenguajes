let contador1= 0
let contador2 = 0
const valor= document.getElementById("valor")
const valor1= document.getElementById("valor1")

window.addEventListener("keydown", (e)=> {

    if (e.key == "+"){
        incremento()

    }

    if(e.key == "-"){
        decremento()

    }
}
);




function incremento(){

    contador1+=1
    valor.innerHTML=contador1
}

function decremento(){

    if (contador1>0){
    contador1-=1
    valor.innerHTML=contador1
    }

    else{
        contador1=0
        valor.innerHTML=contador1
    }
}



function resetear(){

    contador1=0
    contador2 = 0
    valor.innerHTML=contador1
    valor1.innerHTML= contador2

}


// window.addEventListener("keydown", (e)=> {

//     if (e.key == "+"){
//         incremento1()
//     }

//     if(e.key == "-"){
//         decremento1()
//     }
// }
// );


// function incremento1(){

//     contador2+=1
//     valor1.innerHTML=contador2
// }

// function decremento1(){

//     if (contador2>0){
//     contador2-=1
//     valor1.innerHTML=contador2
//     }

//     else{
//         contador2=0
//         valor1.innerHTML=contador2
//     }
// }