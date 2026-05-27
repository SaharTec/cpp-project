data segment 
MSG db 'Enter a positive integer number N (2<N<255): $'
range_err db 'N MOST BE BETWEEN 2 AND 255. $'
prime_msg     db 0Dh,0Ah,'prime$'
not_prime_msg db 0Dh,0Ah,'not prime$'
new_line db 13, 10, "$"
Number dw 0
data ends

code segment
assume ds:data, cs:code

start:
    mov ax, data
    mov ds, ax
    call option1
    call check
    mov ax, 4c00h
    int 21h

option1 proc
input:
    mov dx, offset MSG
    mov ah, 9
    int 21h
    mov word ptr[Number], 0

read_loop:
    mov ah, 1
    int 21h

    cmp al, '.'     ;finish the input"
    je end_read

    cmp al, ' '     ;ignore spaces
    je read_loop

    cmp al, 13      ;ignore enter
    je read_loop

    cmp al, 'a'     ;check if the values are smaller then lower case a
    jb to_lower     
    cmp al, 'f'     ;check if the values are higher then lower case a
    ja to_lower
    sub al, 20h

to_lower:           ;cast lower case input 
    cmp al, '9'
    jbe digit
    sub al, 7
digit:
    sub al, '0'
    mov ah, 0
    mov cx,ax

    mov ax, word ptr[Number]
    mov bx, 16
    mul bx
    add ax, cx
    mov word ptr[Number], ax
    jmp read_loop

end_read:
    mov ax, word ptr[Number]
    cmp ax, 2h          ;check if the number is higher then 2
    jle invalid_range
    cmp ax, 255h        ;check if the number is lower then 255 / ff
    jge invalid_range
    jmp valid

invalid_range:
    mov dx, offset range_err
    mov ah, 9
    int 21h
    jmp input

valid:
ret
option1 endp

check proc
    mov cx, word ptr[Number]
    cmp cx, 1
    jle prime_not_found
    cmp cx, 3
    jle prime_found
    mov bx, 2
verify:
    mov ax, bx
    mul bx
    cmp ax,cx
    ja prime_found

    mov ax, cx
    xor dx,dx 
    div bx
    cmp dx, 0
    je prime_not_found
    inc bx
    jmp verify

prime_found:
    mov dx, offset prime_msg
    mov ah, 9
    int 21h
    call draw_triangle
    ret

prime_not_found:
    mov dx, offset not_prime_msg
    mov ah, 9
    int 21h
    call draw_squre
    ret
check endp

draw_triangle proc
    mov bp, word ptr[Number]
    mov bx, 1

tringle_row:
    cmp bx, bp
    jg triangl_done
    mov dx,  offset new_line
    mov ah, 9
    int 21h

    mov cx, bx
print_tr:
    mov ah, 2
    mov dl, "@"
    int 21h
    loop print_tr
    inc bx
    jmp tringle_row

triangl_done:
    ret
draw_triangle endp

draw_squre proc
    mov bp, word ptr[Number]
    mov bx, 1

squre_row:
    cmp bx, bp
    jg squre_done
    mov dx,  offset new_line
    mov ah, 9
    int 21h

    mov cx, bp
print_squre:
    mov ah, 2
    mov dl, "*"
    int 21h
    loop print_squre
    inc bx
    jmp squre_row

squre_done:
    ret
draw_squre endp

code ends
end start
