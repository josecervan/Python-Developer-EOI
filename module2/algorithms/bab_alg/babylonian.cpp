#include<iostream>
#include<cstdlib>
using namespace std;

const long double ERROR_DE_PRECISION=0.00001;

void menu();
unsigned long long potencia(int base,int exponente);
long double valorInicial(long double N);
long double algoritmoBabilonico(long double x0,long double N);
long double vAbsoluto(long double v);

int main()
{
    long double N;
    menu();
    cin>>N;
    cout<<"\n\t Resultado: "<<algoritmoBabilonico(valorInicial(N),N)<<endl;
    cout<<"\n\t ";
    system("Pause");
    return 0;
}

void menu()
{
    cout<<"\n =============================================================================="<<endl;
    cout<<"\n\t\t     Ra\241z cuadrada (algoritmo babil\242nico)"<<endl;
    cout<<"\n =============================================================================="<<endl<<endl;
    cout<<"\n\t Introduzca n\243mero: ";
}

long double valorInicial(long double N)
{
    unsigned long long D=0,aux,z,x0;
    aux=N;
    while(aux>=1)
    {
         aux=aux/10;
         ++D;
    }
    //cout<<"\n\t N\243mero de d\241gitos: "<<D<<endl;
    if(D%2==0)
    {
        z=(D-2)/2;
        aux=potencia(10,z);
        x0=6*aux;
    }
    else
    {
        z=(D-1)/2;
        aux=potencia(10,z);
        x0=2*aux;
    }
    /*cout<<"\n\t z: "<<z<<endl;
    cout<<"\n\t Potencia: "<<aux<<endl;
    cout<<"\n\t Valor incial x0: "<<x0<<endl;*/
    return x0;
}

unsigned long long potencia(int base,int exponente)
{
    unsigned long long p=1;
    for(int i=0;i<exponente;++i)
        p*=base;
    return p;
}

long double algoritmoBabilonico(long double x0,long double N)
{
    int i=0;
    long double xn=x0,xn1,aux;
    /*cout<<"\n\t Proceso iterativo"<<endl;
    cout<<"\n\t\t x0: "<<x0<<endl;*/
    do
    {
        aux=xn;
        xn1=(xn+N/xn)/2;
        xn=xn1;
        //cout<<"\n\t\t x"<<i+1<<": "<<xn1<<endl;
        ++i;
    }   while(vAbsoluto(xn1-aux)>=ERROR_DE_PRECISION);
    //cout<<"\n\t Iteraciones: "<<i<<endl;
    return xn1;
}

long double vAbsoluto(long double v)
{
    if(v<=0)
        v*=-1;
    return v;
}
