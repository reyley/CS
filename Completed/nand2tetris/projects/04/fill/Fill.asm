// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.



    @KBD
    D=M
    @prev
    M=D
    @FILLSCREEN // if keyboard not zero: fill screen
    D;JNE
    @CHECKKEYS  // else continue checking the keyboard
    0;JEQ

(CHECKKEYS)
    @KBD
    D=M

    @FILLSCREEN // if keyboard not zero: fill screen
    D;JNE

    @prev
    D=D|M

    @CHECKKEYS // loop back if prev and now are both 0
    D;JEQ

    @EMPTYSCREEN  // else empty screen (now is 0 and prev was 1)
    D;JNE

(FILLSCREEN)
    @screenstat
    M=-1
    @prev
    M=1
    @CHANGESCREEN
    0;JEQ

(EMPTYSCREEN)
    @screenstat
    M=0
    @prev
    M=0
    @CHANGESCREEN
    0;JEQ

(CHANGESCREEN)
    @SCREEN  // set location to point to the start of the screen
    D=A
    @location
    M=D

    @LOOP
    0;JEQ

(LOOP)
// colour row location in the colour of screenstat
    @screenstat
    D=M
    @location
    A=M
    M=D

// add 1 to location to get the next location
    @location
    MD=M+1
// checking if our next location is out of the screen and into the keyboard location
    @KBD
    D=A-D

    @CHECKKEYS  // if location + 1 => KBRD location: go back to checking the keyboard
    D;JEQ

    @LOOP  // if location + 1 is in the screen loop over
    D;JGT