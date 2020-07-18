// suma.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include "suma.h"
using namespace std;




// __________________________________________

int main()
{
	cout << " ___//____//____" << endl << " Ejemplo: " << endl;
	int res = sumaEjemplo(3,5);
	cout << " la suma da" << res << endl;

}

// __________________________________________

int sumaEjemplo(int a, int b) { 
	int resultado;

	resultado = a + b ;

	return resultado;

}

void sumaEjemplo1(float a, float c) {
	int resultado;

	resultado = a + c;
	cout << " la suma da" << resultado << endl;

}