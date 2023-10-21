function Mostrar() {


    x =parseInt(prompt("Jelouuuuu, bienvenid@ a la calculadora. Para saber el area de un cuadrado digita '1', para el aera de un rectangulo presiona '2', para el area de un triangulo presiona '3' y para salir presiona '4' "));


    switch(x){
        case 1:
          var l= parseFloat(prompt("Ingrese lado"));
          var total= l* l
          document.write (`El resultado es ${total}`);
          break;

        case 2:
            var b= parseFloat(prompt("Ingrese base"));
            var h= parseFloat(prompt("Ingrese altura"));
            var total= b * h
            document.write (`El resultado es ${total}`);
            break;
        
        case 3: 
            var b= parseFloat(prompt("Ingrese base"));
            var h= parseFloat(prompt("Ingrese altura"));
            var total = (b * h)/2
            document.write (`El resultado es ${total}`);
            break;

        case 4:
            document.write ("Has salido");
            break;
            

    };
};