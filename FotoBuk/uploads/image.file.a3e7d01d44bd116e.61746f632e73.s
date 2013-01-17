
.LC0:
	.ascii	"%d\040\052\040\000"
	.align 2
.LC1:
	.ascii "%d\040\075\040\000"
	.align 2
.LC2:
	.ascii "%d\012\000"
	.align 2

.global cal
cal:
	stmfd sp!, {r1, lr}
	mov r2, r0
	mul r0, r2, r1
	ldmfd sp!, {r1 ,pc}
.global incree
incree:
	stmfd sp!, {lr}
	add r0, r0, #1
	ldmfd sp!, {pc}
.global print_arguements
print_arguements:
	stmfd sp!, {r0, r1, lr}
	mov r4, r1
	mov r1, r0
	bl print1
	mov r1, r4
	bl print2
	mov r1, r2
	bl print3
	ldmfd sp!, {r0, r1, pc}
.global print1
print1:
        @prints an integer present in r1
	         stmfd   sp!,{r0,r1,r2,r3,r7, lr}
	         add     r7, sp, #0
	         adr     r0, .LC0
	         bl      printf
	         mov     r0, #0
	         ldmfd   sp!,{r0,r1,r2,r3,r7, pc}

.global print2
print2:
            @prints an integer present in r1
             stmfd   sp!,{r0,r1,r2,r3,r7, lr}
              add     r7, sp, #0
               adr     r0, .LC1
                bl      printf
               mov     r0, #0
	          ldmfd   sp!,{r0,r1,r2,r3,r7, pc}

.global print3
print3:
            @prints an integer present in r1
             stmfd   sp!,{r0,r1,r2,r3,r7, lr}
              add     r7, sp, #0
               adr     r0, .LC2
                bl      printf
                 mov     r0, #0
	          ldmfd   sp!,{r0,r1,r2,r3,r7, pc}

