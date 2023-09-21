// var nombres = prompt ("Ingresa tu nombre");
// var edad= parseInt(prompt("Ingrese la dead"));
// document.write(`Bienvenido señor(a) ${nombres}, usted tiene ${edad} de edad`)

var nacimiento = parseInt(prompt("Ingrese año de nacimiento"));
// Lugar donde se inserta el año de nacimiento

const fecha = new Date(); // Variable donde se adapta la variable para recibir datos de fecha
const añoActual= fecha.getFullYear(); // Variable donde a la variable anterior se le agrega el año actual
let edad = añoActual - nacimiento; // Variable donde se resta El año actual con el año de nacimiento

var nombres = prompt ("Ingresa tu nombre"); // Variable done se inserta el nombre


if (edad>7 && edad<18) {
    document.write(`Bienvenido joven ${nombres}, usted tiene ${edad} años de edad`)
} // Si la persona tiene <= 18 años aparece este mensaje

else if (edad>=0 && edad<=7){
    document.write(`Bienvenido niño(a) ${nombres}, usted tiene ${edad} años de edad`)
} // Si la persona tiene <= 18 años aparece este mensaje

else {
    document.write(`Bienvenido señor(a) ${nombres}, usted tiene ${edad} años de edad`)
} // De lo contrario, si la persona tiene >= 18 años aparece este mensaje