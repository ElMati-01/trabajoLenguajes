
// Se crea la función sumar, en la cual se agregan unas condiciones y estilos

function Sumar(n1,n2){
    var resultado=n1+n2
    var res=document.getElementById("resultado")
    if (n1 !=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado}`;
        res.style.color= "green";
    } else{
        respuesta.style.display="block";
        res.innerHTML= "Verifique sus datos"
        res.style.color="red";
    }
}

// Se crea la función restar, en la cual se agregan unas condiciones y estilos

function Restar(n1,n2){
    var resultado=n1-n2
    var res=document.getElementById("resultado")
    if (n1 !=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado}`;
        res.style.color= "green";
    } else{
        respuesta.style.display="block";
        res.innerHTML= "Verifique sus datos"
        res.style.color="red";
    }
}

// Se crea la función multiplicación, en la cual se agregan unas condiciones y estilos

function Multiplicacion(n1,n2){
    var resultado=n1*n2
    var res=document.getElementById("resultado")
    if (n1 !=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado}`;
        res.style.color= "green";
    } else{
        respuesta.style.display="block";
        res.innerHTML= "Verifique sus datos"
        res.style.color="red";
    }
}

// Se crea la función división, en la cual se agregan unas condiciones y estilos

function Division(n1,n2){
    var resultado=n1/n2
    var res=document.getElementById("resultado")
    if (n1 !=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado}`;
        res.style.color= "green";
    } else{
        respuesta.style.display="block";
        res.innerHTML= "Verifique sus datos"
        res.style.color="red";
    }
}

// Se crea la función potencia, en la cual se agregan unas condiciones y estilos

function Potencia (n1,n2){
    var resultado=n1**n2
    var res=document.getElementById("resultado")
    if (n1 !=0 && n2!=0){
        respuesta.style.display="block";
        res.innerHTML = `Total : ${resultado}`;
        res.style.color= "green";
    } else{
        respuesta.style.display="block";
        res.innerHTML= "Verifique sus datos"
        res.style.color="red";
    }
}

// Se crea la función mostrar, la cual obtiene los elementos registrados en HTML por medio de un id

function Mostrar(){
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    let opc=parseInt(document.getElementById("opc").value);

// Aquí se crea el switch "opc" el cual por medio de la opción que se le asigne ejecutará un caso

switch(opc){
    case 1:
        Sumar(n1, n2);
        break;
    case 2:
        Restar(n1, n2);
        break;
    case 3:
        Multiplicacion(n1, n2);
        break;
    case 4:
        Division(n1, n2);
        break;
    case 5:
        Potencia(n1, n2);
        break;
    default:
        alert("No se encuentra lo que ha pedido xd")
}
}

