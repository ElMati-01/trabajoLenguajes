function Mostrar() {


    x =parseInt(prompt(" '1' para sumar, '2' para restar, '3' para multiplicar, '4' para dividir y '5' para saber cual es el mayor "));

    switch(x){
        case 1:
          var numb1= parseFloat(prompt("Ingrese primer numero"));
          var numb2= parseFloat(prompt("Ingrese segundo numero"));
          var total= numb1 + numb2

          if (numb1 !=0 && numb2!=0){
            document.write (`El resultado es ${total}`);  
          }
          else{
            document.write ("Valores incorrectos. Ponga valores mayores a 0");
          }
          
          break;

        case 2:

            var numb1= parseFloat(prompt("Ingrese primer numero"));
            var numb2= parseFloat(prompt("Ingrese segundo numero"));
            var total= numb1 - numb2
  
            if (numb1 !=0 && numb2!=0){
              document.write (`El resultado es ${total}`);  
            }
            else{
              document.write ("Valores incorrectos. Ponga valores mayores a 0");
            }
            
            break;
        case 3: 
            var numb1= parseFloat(prompt("Ingrese primer numero"));
            var numb2= parseFloat(prompt("Ingrese segundo numero"));
            var total= numb1 * numb2

            if (numb1 !=0 && numb2!=0){
              document.write (`El resultado es ${total}`);  
            }
            else{
              document.write ("Valores incorrectos. Ponga valores mayores a 0");
            }
        
            break;

        case 4:
            var numb1= parseFloat(prompt("Ingrese primer numero"));
            var numb2= parseFloat(prompt("Ingrese segundo numero"));
            var total= numb1 / numb2

            if (numb1 !=0 && numb2!=0){
              document.write (`El resultado es ${total}`);  
            }
            else{
              document.write ("Valores incorrectos. Ponga valores mayores a 0");
            }
        
            break;  
        
        case 5:
            var numb1= parseFloat(prompt("Ingrese primer numero"));
            var numb2= parseFloat(prompt("Ingrese segundo numero"));

            if (numb1<numb2){
              document.write (`El mayor es ${numb2}`);  
            }
            else{
              document.write (`El mayor es ${numb1}`);
            }
        
            break;

    };
};