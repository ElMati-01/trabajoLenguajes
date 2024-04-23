// Ejercicio 1

function numeroPi(numero){
    let redondeo= parseFloat(numero.toFixed(2))
    return redondeo
}

document.addEventListener('DOMContentLoaded', function(){
    let pi= Math.PI
    let resultado= numeroPi(pi) 

    let elemento= document.getElementById('respuesta1')
    elemento.textContent= resultado
})

// Ejercicio 2

function factura(precio, iva){
    if(iva == 0){
       iva= 19/100;
    }

    let total= precio + (precio * iva);
    return total;
}

document.addEventListener('DOMContentLoaded', function(){
    let numeros= factura(20000, 0);


    let elemento= document.getElementById('respuesta2');
    elemento.textContent= numeros;    
})

// Ejercicio 3

function revesCadena(cadena){
    return cadena.split('').reverse().join('')
}

document.addEventListener('DOMContentLoaded', function(){
    const form= document.getElementById('formInvertir');
    form.addEventListener('sumbit', function(event){
        event.preventDefault();

        let entrada= document.getElementById('entradaTexto').value;
        let resultado=revesCadena(entrada) 
        let elemento= document.getElementById('respuesta3')
        elemento.textContent= resultado        
    })

})

// Ejercicio 4

function random(num1, num2){
    
    if (num1 == 0 || num2 == 0){
        num1= 1
        num2= 100
        let azar= Math.floor(Math.random() * (num2- num1 + 1) + num1)
        return azar
    }
    else{
        let azar= Math.floor(Math.random() * (num2- num1 + 1) + num1); 
        return azar;  
    }   
}

document.addEventListener('DOMContentLoaded', function(){
    const form= document.getElementById('formulario');
    form.addEventListener('submit', function(event){
        event.preventDefault()

        let entrada1= parseInt(document.getElementById('numero1').value)
        let entrada2= parseInt(document.getElementById('numero2').value) 
        let resultado= random(entrada1, entrada2)
        let elemento= document.getElementById('respuesta4')
        elemento.textContent= resultado
    })
})



function numerosNoRepetidos(num1, num2){
    let e= 0
    filtro=[]
    while(e < 100){
        let azar= Math.floor(Math.random() * (num2- num1 + 1) + num1)
        if(!filtro.includes(azar)){
            filtro.push(azar)
        }
        e+=1
    }
    return filtro
}

document.addEventListener('DOMContentLoaded', function(){
    let resultado= numerosNoRepetidos(1,100)
    let elemento= document.getElementById('resultado5')
    elemento.textContent= resultado
})



