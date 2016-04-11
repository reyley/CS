// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// a = RAM[0], b = Ram[1]
    @R0
    D=M
    @a
    M=D

    @R1
    D=M
    @b
    M=D

// if b<0 flip a and b
    @b
    D=M
    @FLIP
    D;JLT
    @STARTMUL
    0;JEQ



(FLIP)
    @a
    D=M
    @temp
    M=D  //temp=a

    @b
    D=M
    @a
    M=D  //a=b

    @temp
    D=M
    @b
    M=D  //b=a

    @FLIPPED
    0;JEQ


(FLIPPED)
// if b<0 again multiply a and b by -1
    @b
    D=M
    @CHANGESIGN
    D;JLT
    @STARTMUL
    0;JEQ

(CHANGESIGN)
    @a
    M=-M
    @b
    M=-M
    @STARTMUL
    0;JEQ

(STARTMUL)
// i=0
    @i
    M=0

// result=0
    @result
    M=0

// if i < b goto loop
    @b
    D=M
    @i
    D=M-D  // D = i-b
    @LOOP
    D;JLT
    @SETRESULT
    0;JEQ

(LOOP)
    @a
    D=M
    @result
    M=M+D  // result += a

    @i
    M=M+1 // i++

// if i < b goto loop
    @b
    D=M
    @i
    D=M-D  // D = i-b
    @LOOP
    D;JLT

// if i = b: R2 = result, END
    @SETRESULT
    0;JEQ

(SETRESULT)
    @result
    D=M
    @R2
    M=D
    @END
    0;JEQ

(END)
    @END
    0;JEQ