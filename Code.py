##include "mbed.
AnalogIn adc(p20); //we are using pin20
  Serial pc(USBTX,USBRX);
  main() {
  uint16_t adcValue; // gives 2**16 levels
  float voltage;
  while(1) {
 adcValue = adc.read_u16(); 
 voltage = adcValue * 3.3 /65535; //2^16 = 65536
 	pc.printf("ADC	Value	:	%i,%0.9f	volt	\r\n",	adcValue,voltage);							
  wait(0.01);				
  }	}

