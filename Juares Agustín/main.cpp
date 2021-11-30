#include "libs/LCD.h"
#include "libs/DHT.h"

    int  main ( void ) {

    LCD lcd ( 2 , 3 , 4 , 5 , 6 , 7 );
    DHT dht ( 8 , DHT11);

    while ( 1 ) {

    double humedad = 0;
    double temperatura = 0;

    dht.read (&temperatura,&humedad);

    lcd.print (temperatura);
    lcd.print ("C");
    _delay_ms (5000);
    lcd.setXY (1,2);  
    lcd.print (humedad);
    lcd.print ("%");
    _delay_ms (5000);
    lcd.clear();

    }

    return  0 ;
}