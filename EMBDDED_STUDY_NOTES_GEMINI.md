# Embedded Bare Metal Study Notes (Gemini CLI)
*Date: Monday, February 16, 2026*

## 1. The Core Philosophy
**Bare Metal** means bypassing libraries (like Arduino.h) to talk directly to the hardware registers.
*   **Cost:** Electricity and Time. Bare metal is ~50x faster and more power-efficient.
*   **Access:** We use memory addresses instead of "nicknames."

## 2. The "District of Docks" (Ports & Registers)
The ATmega328P (Uno's brain) groups pins into **Ports**. Think of a Port as a district of 8 docks (bits).

### Port D (Digital Pins 0-7)
- **DDRD** (Data Direction Register): Sets the "Direction." (1 = Output, 0 = Input).
- **PORTD** (Output Register): Sets the "Goal." (1 = 5V, 0 = 0V).
- **PIND** (Input Register): Reads the "Reality." (Is electricity flowing in?).

### Port B (Digital Pins 8-13)
- Handles the higher pins.
- **Pin 13** is `PORTB`, Bit 5.

## 3. Data Representation: The Nibble
An 8-bit **Byte** is split into two 4-bit **Nibbles**.
- **High Nibble:** The Left 4 bits (e.g., `1011` in `1011 0001`).
- **Low Nibble:** The Right 4 bits (e.g., `0001` in `1011 0001`).

**The "Nibble Shuffle":**
When using 4-bit mode for an LCD, we send the High Nibble first, then "shift" the Low Nibble to the left (`<< 4`) to send it through the same physical wires.

## 4. Hardware Identity (My Uno)
- **Port Name:** `/dev/cu.usbserial-A5069RR4`
- **Identity:** Arduino Clone (likely ATmega328P).
- **Crystal:** 16.000 MHz (The heart/clock).
- **USB Chip:** `cu` (Call Up) allows us to "call" the chip and initiate talk.

## 5. C++ Bare Metal Syntax
- `0b` prefix: Tells the compiler to read as **Binary** (e.g., `0b11110000`).
- `0x` prefix: Tells the compiler to read as **Hexadecimal** (e.g., `0xF0`).
- `|=` : Turns a bit **ON**.
- `&= ~` : Turns a bit **OFF**.
- `<< 4` : Shifts bits 4 spots to the **Left**.

## 6. LCD Parallel Wiring (Practice Target)
| LCD Pin | Uno Pin | Register/Bit |
| :--- | :--- | :--- |
| D4, D5, D6, D7 | 4, 5, 6, 7 | PORTD, Bits 4-7 |
| RS (Register Select)| 8 | PORTB, Bit 0 |
| E (Enable) | 9 | PORTB, Bit 1 |

---
*Keep this file as your 'X-Ray' view of the Uno.*
