#include <iostream>

#define MAX_GENES 50
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


int main()
{
    setlocale(LC_ALL, "Portuguese");

    ConfigInt config;
    Item itens[MAX_ITEMS];

    int qt_config=0, qt_itens=0;

    ifstream ip("\config.csv");
    if(ip.is_open())
    {
        while(ip.good())
        {
            if(qt_config==0)
            {
                qt_config++;
                continue;
            }

            ConfigString t;

            getline(ip,t.peso_suportado,';');
            getline(ip,t.populacao,';');
            getline(ip,t.timeout_sec,'\n');


            config.peso_suportado=atoi(t.peso_suportado.c_str());
            config.populacao=atoi(t.populacao.c_str());
            config.qt_itens=atoi(t.qt_itens.c_str());
            config.timeout_sec=atoi(t.timeout_sec.c_str());
        }
        ip.close();
    }
    else
    {
        cout<<"ERRO AO CARREGAR AS CONFIGURAÇÕES!";
    }


    ifstream ip("\items.csv");
    if(ip.is_open())
    {
        while(ip.good())
        {
            if(qt_itens==0)
            {
                qt_itens++;
                continue;
            }

            Item i;


            getline(ip,i.nome,';');
            getline(ip,i.beneficio,';');
            getline(ip,i.peso,'\n');

            itens[qt_itens-1].nome=i.nome;
            itens[qt_itens-1].beneficio=atoi(i.beneficio.c_str());
            itens[qt_itens-1].peso=atoi(i.peso.c_str());

            qt_itens++;
            }

        }

        inscrito[qt].id='\0';
        ip.close();

    }
    else
    {
        cout<<"ERRO!";
    }

    return 0;
}
