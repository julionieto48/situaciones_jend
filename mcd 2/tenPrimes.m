function primos = tenPrimes ()
%primero 10 primos
%   https://rstopup.com/como-puedo-generar-los-n-primeros-numeros-primos.html
 numero = 2 ; conteo = 1 ;
 primos = [];
 
 while conteo < 10
     j = 1 ;
     
     while ( j <= numero )
         j = j + 1 ;
         
         if mod(numero , j) == 0  ;
             break
         end  
     end
     
     
     if ( j == numero)
         primos(conteo) =  numero ;
         %disp(numero) ;
         conteo = conteo + 1;
          
     end
     
      numero = numero + 1 ;
 end
 
 return 



end

