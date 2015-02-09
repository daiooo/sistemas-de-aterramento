/* Objetivo:
 * $$ Controle do acionamento da placa de potência.
 * O PIC é responsável por acionar o primeiro
 * mosfet e depois ativar o segundo mosfet para
 * que o capacitor seja descarregado.
 *
 * $$ Verificação automática de fase.
 * Alterando a alimentação na troca indevida do fase
 * com o neutro na alimentação da placa
 *
 * $$ Sub objetivo:
 * A mudança para o pic reduz o número de componentes
 * e aumenta a possibilidade de qualquer mudança futura.
 *
 * $$ Entrada:
 * ra2 - inicia o processo
 * ra3 - reseta
 * Observação: é necessário um tempo mínimo para que a
 * entrada seja reconhecida. Tal necessidade evita o acionamento
 * erróneo da potência. Evitando assim, possíveis acidentes.
 * Tal tempo é de no minimo 50ms. Para SET e RESET.
 *
 * $$ Saída:
 * rb5 - mosfet 1, mosfet do carregamento
 * rb4 - mosfet 2, mosfet do descarregamento
 *
 * Responsáveis:
 * Felipe Bandeira da Silva
 * Francisco Alexandre
 *
 * Projeto:
 * Sistemas de Aterramento, COELCE
 *
 * 26/08/2014
 */

#include <xc.h>

#pragma config FOSC = INTOSCIO  // Oscillator Selection bits (INTOSC oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled)
#pragma config PWRTE = ON       // Power-up Timer Enable bit (PWRT enabled)
#pragma config MCLRE = ON       // RA5/MCLR/VPP Pin Function Select bit (RA5/MCLR/VPP pin function is MCLR)
#pragma config BOREN = ON       // Brown-out Detect Enable bit (BOD enabled)
#pragma config LVP = OFF        // Low-Voltage Programming Enable bit (RB4/PGM pin has digital I/O function, HV on MCLR must be used for programming)
#pragma config CPD = OFF        // Data EE Memory Code Protection bit (Data memory code protection off)
#pragma config CP = OFF         // Flash Program Memory Code Protection bit (Code protection off)

#define _XTAL_FREQ 4000000

// Garante um tempo de 100 us para o timer0
#define BASE_TIMER0 206

#define habilita_interrupcoes() {GIE = 1;}
#define delayms(a)  __delay_ms(a)
#define delayus(a)  __delay_us(a)

#define MOSFET_1        RB5
#define MOSFET_2        RB4
#define TRI_MOSFET_1    TRISBbits.TRISB5
#define TRI_MOSFET_2    TRISBbits.TRISB4

#define conf_port_mosfet()      {TRI_MOSFET_1=0; TRI_MOSFET_2=0; MOSFET_1=0; MOSFET_2=0;}
#define estagio_1()             {MOSFET_1=1;}
#define estagio_2()             {MOSFET_1=0;}
#define estagio_3()             {MOSFET_2=1;}
#define estagio_4()             {MOSFET_2=0;}

#define SET                 RA6
#define TRI_SET             TRISAbits.TRISA6
#define conf_port_entrada() {TRI_SET=1;}

#define __ERRO      RB3
#define conf_erro() {TRISBbits.TRISB3=0; __ERRO=0;}
#define ERRO()      {__ERRO=1;}
#define LIB_ERRO()  {__ERRO=0;}

#define FASE            RB6
#define TRI_FASE        TRISBbits.TRISB6
#define VER_FASE        RA4
#define TRI_VER_FASE    TRISAbits.TRISA4
#define conf_fase()     {TRI_FASE=0; FASE=0; TRI_VER_FASE=1;}
#define muda_fase()     {FASE=~FASE;}

#define BARRA_DC                RB2
#define TRI_BARRA_DC            TRISBbits.TRISB2
#define conf_controle_barra()   {TRI_BARRA_DC = 0;}
#define liga_potencia()         {BARRA_DC = 1;}
#define desliga_potencia()      {BARRA_DC = 0;}

// Tempo em microsegundos
#define TEMPO_CARGA 10000
#define TEMPO_DESCARGA 50000
#define TEMPO_MORTO 30

// Flag de uso geral
// 0 - usada para a o travamento do set
// 1 - flag do monitor da tensão do barramento DC
volatile unsigned char flag = 0;

#define pos_flag_SET 1<<0
#define flag_SET (pos_flag_SET & flag)

#define pos_flag_DC 0x02
#define flag_DC (pos_flag_DC & flag)

#define set_f(f,a) {f|=a;}
#define clr_f(f,a) {f&=~a;}

#define set_b(f,a) {f |= (1<<a);}
#define clr_b(f,a) {f &= ~(1<<a);}
#define tes_b(f,a) (f & (1<<a))


/* controle_mosfet
 *
 * Controla o acionamento dos mosfet. Para
 * o carga e descarga do capacitor.
 */
void controle_mosfet(void) {

    if(tes_b(flag, pos_flag_SET) && SET == 0){
        clr_b(flag, pos_flag_SET);
    }
   
    if(SET == 1 && !tes_b(flag, pos_flag_SET)){
        set_b(flag, pos_flag_SET);
        
        estagio_1();
        delayus(TEMPO_CARGA);
        estagio_2();
        delayus(TEMPO_MORTO);
        estagio_3();
        delayus(TEMPO_DESCARGA);
        estagio_4();
    }
}

/* monitor_fase
 *
 * Monitora qualquer mudança na alimentação da fonte.
 * Qualquer troca entre fase e neutro é detectada.
 * E feito a devida troca, internamente. Sem a necessidade
 * do operador.
 */
void monitor_fase(void) {
    if (VER_FASE == 1) {
        muda_fase();
    }
}

#define ref_167()   {VRCONbits.VR = 8;}
#define ref_104()   {VRCONbits.VR = 5;}

void conf_mod_ref(void) {
    VRCONbits.VREN = 1; // liga o circuito de tensão de referência
    VRCONbits.VROE = 1; // desabilita saída da tensão de referência
    VRCONbits.VRR = 1; // low range

    ref_167(); // 0 a 15, 8 => (8/24)*5 = 1.67 Volts
}

/* conf_ao_barra
 *
 * Configurando o módulo comparador do pic para
 * monitorar o barramento DC.
 */
void conf_ao_barra(void) {
    TRISAbits.TRISA0 = 1;
    TRISAbits.TRISA1 = 1;

    // O primeiro estado para a interrupção será
    // quando a tensão for maior que a especificada
    // Tensão no barramento DC
    CMCONbits.C1INV = 1;

    CMCONbits.CIS = 0x00; // Entradas das portas inversoras por RA0 e RA1
    CMCONbits.CM = 0x02; // referência de tensão interna

    conf_mod_ref();

    PIR1bits.CMIF = 0; // limpa a flag do comparador
    PIE1bits.CMIE = 1; // interrupção do comparador
    INTCONbits.PEIE = 1; // interrupções dos periféricos
}

/* conf_timer0
 *
 * O Timer 0 será usado como base de tempo para o
 * monitoramento do barramento DC. Acionamento
 * dos mosfet.
 * Portanto a base de tempo será pequena algo em
 * torno de 100 us.
 */
void conf_timer0(void) {
    OPTION_REGbits.T0CS = 0; // incremento pelo oscilador interno
    OPTION_REGbits.PSA = 0; //  prescale pelo modulo do timer0

    OPTION_REGbits.PS = 0x00; // 1:2

    // Para um valor de 50 a interrupção
    // acontece a cada 100 us
    TMR0 = BASE_TIMER0;

    INTCONbits.T0IF = 0; // limpa a flag
    INTCONbits.T0IE = 1; // interrupção do timer 0
}

/****************
 * INTERRUPÇÕES *
 ****************/
void interrupt isr(void) {
    static unsigned int tempo1 = 0;
    
    if (T0IF == 1) {

        TMR0 = BASE_TIMER0;
        
        if (tempo1 == 300) {
            // 30 milisegundos

            tempo1 = 0;

            // muda o estado do comparador
            if (tes_b(flag, pos_flag_DC)) {
                ref_167();
                C1INV = 1;
                CMIF = 0; // garante que não teremos interrupção
                clr_b(flag, pos_flag_DC);
            } else {
                ref_104();
                C1INV = 0;
                CMIF = 0;
                set_b(flag, pos_flag_DC);
            }

        } else {
            tempo1++;
        }

        T0IF = 0;
        
    } else if (CMIF == 1) {
        // Interrupção responsável por monitar o barramento DC
        // Modulo comparador

        if (C1OUT == 1) {
            /*
             * A tensão no barrameto DC não esta nos conformes
             */

            // primeira açõe adotada
            desliga_potencia();
        }

        CMIF = 0;
    }
}

/********
 * MAIN *
 ********/
int main(void) {

    conf_erro();
    conf_ao_barra();
    conf_port_mosfet();
    conf_controle_barra();
    conf_port_entrada();
    conf_fase();
    conf_timer0();

    //////////////////////////////////
    // Chave geral das interrupções //
    //////////////////////////////////
    habilita_interrupcoes();

    // verifica se a alimentação esta devidamente coerente
    monitor_fase();

    // liga o barramento DC ou a potência
    liga_potencia();

    // certifica-se que o capacitor esta descarregado
    // injetando qualquer energia remanescente no aterramento
    estagio_3();
    delayus(100);
    estagio_4();

    // aviso visual do fim da inicialização
    ERRO();
    delayms(1000);
    LIB_ERRO();

    while (1) {
        controle_mosfet();
    }

    return 0;
}
