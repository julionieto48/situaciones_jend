clc , clear all , close all ;
%%
% algoritmo euclides MCD
% mcd de dos enteros es el mayor entero que divide a estos dos primeros
% numero


%%
% descomposicion de factores primos

input = 48 ;
primos = tenPrimes() ;  % llamar a un listado de los primos

i = 1 ; newinput = input ;

while newinput ~= 1
    
    newinput = input / primos(i) ;
    
    
    if (mod(input,primos(i)) ~= 0 )
        break
    end 
    
    
   
    
end