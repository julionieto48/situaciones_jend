function [suma] = laSumatoriaEric(numero,opcion)


if (opcion == 1)
    i = 1 ;suma = 0 ; 
    while (i < numero + 1)
        suma = suma + i ;
        i = i + 1 ;
    end
  
elseif (opcion == 2)
     suma = 0 ;
     for(i = 1 : numero)
         suma = suma + i ;  
     end
     
elseif (opcion == 3)
    numeroInicial  = numero ;
    if (numero ~= 0)
        numero = numero + sumatoria(numero - 1);
    end  
    
end


end

