# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizador_lexico import tokens
#from analizador_lexico import analizador
import ply.lex as lex  # importacion de librerias necesarias
import re

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right', 'SI', 'SINO',),
    ('right', 'ASIGNAR'),
    ('left', 'TAGINICIO'),
    ('right', 'TAG_FINAL'),
    ('right', 'PUNTOYCOMA'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}



def p_declaracion_coditionif(t):
    'declaracion : SI PARIZQ ENTERO ASIGNAR ENTERO PARDER LLAIZQ VARIABLE PUNTOYCOMA LLADER'
    t[0] = t[1] #PARA QUE TE ACEPTE LOS SIMBOLOS CAMBIA LAS PALABRAS


def p_declaracion_coditionelse(t):
    'declaracion : SINO LLAIZQ VARIABLE PUNTOYCOMA LLADER'
    t[0] = t[1]


# se definde como debe de funcionar
def p_declaracion_asignar(t):
    'declaracion : VARIABLE ASIGNAR expresion PUNTOYCOMA'
    nombres[t[1]] = t[3]


# aqui la idea de como hacer la primera declaracion
def p_declaracion_taginicio(t):
    'declaracion : TAGINICIO'
    t[0] = t[1]


def p_declaracion_tagfinal(t):
    'declaracion :  TAG_FINAL'
    t[0] = t[1]



def p_declaracion_expr(t):
    'declaracion : expresion PUNTOYCOMA'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]


def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion 
                |   expresion RESTA expresion 
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1


def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]


def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER 
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER

    '''
    t[0] = t[2]
# sintactico de expresiones logicas
# sintactico de expresiones logicas


#def p_expresion_ifelse(t):
    #'expresion : SI PARIZQ expresion PARDER LLAIZQ expresion LLADER'
    #t[0] = t[2] = t[4] = t[5] = t[7]
    
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 