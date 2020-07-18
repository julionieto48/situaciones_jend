function [resultado] = calculadoraEspecialEric(op,n)


if (op == 1)
    resultado = laSumatoriaEric(n,2);
elseif (op == 2)
    resultado = laRestaEric(n,1);
    
elseif (op == 3)
    resultado = laMultiplicacionEric(n,1);
    
end

end

