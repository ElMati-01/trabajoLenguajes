
function generarContrasena(longitud) {
    const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+';

    let contrasena = '';
    for (let e = 0; e < longitud; e+= 1) {
        const indice = Math.floor(Math.random() * caracteres.length);
        contrasena += caracteres.charAt(indice);
    }
    return contrasena;
}

function botones() {
    const longitud = 12; 
    const nuevaCon = generarContrasena(longitud);
    const contenedor = document.getElementById('contrasena');
    contenedor.textContent = 'Contraseña Generada: ' + nuevaCon;
}

const boton = document.getElementById('generarContrasena');
boton.addEventListener('click', botones); 
