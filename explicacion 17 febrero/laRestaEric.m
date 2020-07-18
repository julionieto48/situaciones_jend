function [suma] = laRestaEric(numero,opcion)


if (opcion == 1)
    i = 1 ;suma = 0 ; 
    while (i < numero + 1)
        suma = suma - i ;
        i = i + 1 ;
    end
end


end
