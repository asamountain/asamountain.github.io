// this is a test file but I have no idea how to write the c language in here. and how to connect each other.
// but I can ask about this to Gemini with tmux so let's start.

#define F_CPU 16000000UL
#include <avr/io.h>

// Function to pulse the LCD Enable pin
void lcd_pulse(){
	PORTD |= (1 << PORTD3);  // Set PD3 HIGH
	__asm__("nop");          // Wait 1 cycle
	PORTD &= ~(1 << PORTD3); // Set PD3 LOW
}

/* 
 * Timer1 Setup:
 * We want a 1-second delay.
 * Clock = 16,000,000 Hz.
 * Prescaler = 1024.
 * 16,000,000 / 1024 = 15,625 ticks per second.
 */
void init_timer1(){
	TCCR1B |= (1 << WGM12);               // CTC Mode (Clear Timer on Compare)
	OCR1A = 15625;                        // Target count for 1 second
	TCCR1B |= (1 << CS12) | (1 << CS10);  // Set Prescaler to 1024 and Start Timer
}

/* 
 * main(void): 'void' ensures we take exactly zero arguments.
 * Standard practice in embedded to save memory.
 */
int main(void){
	DDRD = 0xFF; // Set all Port D pins as Outputs (11111111)
	init_timer1();

	while(1) {
		// Check if the Timer Compare Flag (OCF1A) is set
		if (TIFR1 & (1 << OCF1A)){
			PORTD ^= (1 << PORTD4); // Toggle LED on PD4
			TIFR1 |= (1 << OCF1A);  // Clear flag by writing a '1' (AVR quirk)
		}
	}

	return 0;
}


// dangit... this isall so confusing... 1 I don't understand what are those all words meaning, and I don't know why main has to have the void inside...
//
// how can I understand them all? 
