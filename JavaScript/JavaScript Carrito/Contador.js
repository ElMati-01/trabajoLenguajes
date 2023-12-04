
// Linea de contadores en 0 para operaciones 
let contador1= 0
let contador2 = 0

// Se obtiene los "valores" de los botones de HTML
const valor= document.getElementById("valor")
const valor1= document.getElementById("valor1")

// Se crea ina función de escucha para las funciones
window.addEventListener("keydown", (e)=> {

    if (e.key == "+"){
        incremento()

    }

    if(e.key == "-"){
        decremento()

    }
}
);


// Función para incrementar contador

function incremento(){

    contador1+=1
    valor.innerHTML=new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador1 * 39900);
}

// Función para decrementar contador (Se multiplica en vez de dividirse. La multiplicación del precio se agrega en este caso a "contador1" para que el contador reste todos los nuemros por el precio indicado)
function decremento(){

    if (contador1>0){
    contador1-=1
    valor.innerHTML=new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador1 * 39900);
    }

    else{
        contador1=0
        valor.innerHTML=contador1
    }
}




// Se crea ina función de escucha para las funciones (Caso exculsivo para las funciones y variables con 1)
window.addEventListener("keydown", (e)=> {

    if (e.key == "+"){
        incremento1()
    }

    if(e.key == "-"){
        decremento1()
    }
}
);

// Función para incrementar contador
function incremento1(){

    contador2+=1
    valor1.innerHTML= new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador2 * 56900);
}


// Función para decrementar contador
function decremento1(){

    if (contador2>0){
    contador2-=1
    valor1.innerHTML=new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador2 * 56900);
    }

    else{
        contador2=0
        valor1.innerHTML=contador2
    }
}


// Función para resetear contadores
function resetear(){

    contador1=0
    contador2 = 0
    valor.innerHTML=new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador1);
    valor1.innerHTML= new Intl.NumberFormat('es-CO',{ style: 'currency', currency: 'COP' }).format(contador2);

}

function calcularTotal(){

    const precioTotal= (contador1 * 39900) + (contador2 * 56900);

    const resultado = document.getElementById("resultado");
    resultado.innerHTML = `El precio total: ${precioTotal}`;
    
}

function Mostrar() {
    calcularTotal();
  
    const respuesta = document.getElementById("respuesta");
    respuesta.style.display = "block";
  }
