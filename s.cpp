#include <iostream>
#include <string>
#include <cmath>
using namespace std;

struct gladiador{
	string nome;
	int forca;
	int habilidade;
	int idade;
};

// essa funcao deve retornar 0 ou 1
bool combate(gladiador g1, gladiador g2){
	int vitorioso;
	int vida_g1 = 100;
	int vida_g2 = 100;
	int DANO;
	
	while(vida_g1 > 0 && vida_g2 > 0){
		// primeiro gladiador ataca
		DANO = g1.forca * (pow(2, g1.habilidade));
		vida_g2 = vida_g2 - DANO;
		
		// segundo gladiador ataca caso sua vida seja maior que 0 depois de receber ao hit
		if (vida_g2 > 0){
			DANO = g2.forca * (pow(2, g2.habilidade));
			vida_g1 = vida_g1 - DANO;
		}
	}
	if (vida_g1 > vida_g2)
		vitorioso = 0;
	else
		vitorioso = 1;
		
	return vitorioso;
}


int main(){
	gladiador gladiadores[5];
	int i = 0;
	int idx1, idx2;
	int controlador = 1;
	int r;
	
	while(i < 5){
		getline(cin >> ws, gladiadores[i].nome);
		cin >> gladiadores[i].forca;
		cin >> gladiadores[i].habilidade;
		cin >> gladiadores[i].idade;
		i++;
	}
	
	while(controlador != -1){
		cin >> idx1 >> idx2;
		r = combate(gladiadores[idx1], gladiadores[idx2]);
		if (r == 0)
			cout << gladiadores[idx1].nome << " ganhou a batalha contra " << gladiadores[idx2].nome << endl;
		else
			cout << gladiadores[idx2].nome << " ganhou a batalha contra " << gladiadores[idx1].nome << endl;
		
		cin >> controlador;
	}
	
	return 0;
}