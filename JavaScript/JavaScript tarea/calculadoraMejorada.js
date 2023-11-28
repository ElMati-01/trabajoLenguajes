
// Se crea la constante platos y se predetermina los precios
const platos = {
    1: {
      nombre: "Ejecutivo",
      precio: 11000,
    },
    2: {
      nombre: "PlatoDia",
      precio: 13000,
    },
    3: {
      nombre: "PlatoMenu",
      precio: 15000,
    },
  };

// Se crea la constante bebidas y se predetermina los precios 
  const bebidas = {
    1: {
      nombre: "Gaseosa",
      precio: 2500,
    },
    2: {
      nombre: "Limonada",
      precio: 1500,
    },
    3: {
      nombre: "JugoNatural",
      precio: 2000,
    },
  };

 // Aquí se determinan parametros y se comienza a ejecutar los codigos 

  function calcularTotal() {
    const plato1 = document.getElementById("opc").value;
    const bebida1 = document.getElementById("opc2").value;
    const n1 = parseInt(document.getElementById("n1").value);
    const n2 = parseInt(document.getElementById("n2").value);
    if (plato1 === "0" && bebida1 === "0" && n1 === 0 && n2 === 0) {
      alert("Seleccione su plato o bebida");
      return;
    }
  
// Se conectan las variables con los parametros de HTML
    const plato = platos[plato1];
    const bebida = bebidas[bebida1];
  


// Se crea una formula que ayude a imprimir el total del pedido
    const precioPlato = plato.precio;
    const precioBebida = bebida.precio;
  
    const precioTotal = (precioPlato * n1) + (precioBebida * n2) ;
  
    const resultado = document.getElementById("resultado");
    resultado.innerHTML = `Total: ${precioTotal}`;
    resultado.style.color = "green";
  }
  
 // Aquí se saca el total
  function Mostrar() {
    calcularTotal();
  
    const respuesta = document.getElementById("respuesta");
    respuesta.style.display = "block";
  }
