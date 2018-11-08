#include <iostream>

#define MAX_GENES 100
#define MAX_ITEMS 20
#define MAX_NAME 100
#define MAX_CROMOSSOMOS 100

using namespace std;

#include <cstring>
#include <fstream>
#include <locale.h>
#include <string>
#include <sstream>
#include <cstdlib>




struct Item{

    string nome;
    string beneficio;
    string peso;

};
struct ItemInt{

    string nome;
    int beneficio;
    int peso;

};

struct Gene{

    Item item;
    int pos;

};

struct Cromossomo{

    Gene genes[MAX_GENES];
    int fitness;
    int tam;

};

struct Mochila{

    Cromossomo cromossomo[MAX_CROMOSSOMOS];
    int tam;

};

struct ConfigString
{
    string peso_suportado;
    string populacao;
    string qt_itens;
    string timeout_sec;

};
struct ConfigInt
{
    int peso_suportado;
    int populacao;
    int qt_itens;
    int timeout_sec;

};

void imprimir_itens(ItemInt i[MAX_ITEMS], unsigned tam);

int main()
{
    setlocale(LC_ALL, "Portuguese");

    ConfigInt config[10];
    ItemInt itens[MAX_ITEMS];

    int qt_itens=0;

    ifstream ip("config.txt");
    if(ip.is_open())
    {
        while(ip.good())
        {
            ConfigString t;

            getline(ip,t.peso_suportado,',');
            getline(ip,t.populacao,',');
            getline(ip,t.qt_itens,',');
            getline(ip,t.timeout_sec,'\n');

            config[qt_itens].peso_suportado=atoi(t.peso_suportado.c_str());
            config[qt_itens].populacao=atoi(t.populacao.c_str());
            config[qt_itens].qt_itens=atoi(t.qt_itens.c_str());
            config[qt_itens].timeout_sec=atoi(t.timeout_sec.c_str());
            qt_itens++;
        }
        ip.close();
    }
    else
    {
        cout<<"ERRO AO CARREGAR AS CONFIGURAÇÕES!";
    }

    qt_itens=0;

    ifstream it("lista_itens.txt");
    if(it.is_open())
    {
        while(it.good())
        {
            Item i;

            getline(it,i.nome,',');
            getline(it,i.beneficio,',');
            getline(it,i.peso,'\n');

            itens[qt_itens].nome=i.nome;
            itens[qt_itens].beneficio=atoi(i.beneficio.c_str());
            itens[qt_itens].peso=atoi(i.peso.c_str());

            qt_itens++;
        }

        it.close();

    }
    else
    {
        cout<<"ERRO AO LER OS ITENS!";
    }

    imprimir_itens(itens,config[0].qt_itens);

    return 0;
}


void imprimir_itens(ItemInt item[MAX_ITEMS], unsigned tam){

for(unsigned i=0; i<tam; i++){

    cout<<item[i].nome<<" / "<<item[i].beneficio<<" / "<<item[i].peso<<endl;

}

}
