# -*- coding: utf-8 -*-

import ply.lex as lex  # importacion de librerias necesarias
import re

resultado_lexema = []


tokens = [
    # inicio y final
    'TAGINICIO', 'TAG_FINAL',
    'ENTERO', 'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    'PUNTOYCOMA',
    'PUNTO',
    'COMA', 'DECIMAL', 'VARIABLE', 'COMENTARIO','ENTRE',
    # Condiones
    'SI', 'SINO',
    # Ciclos
    'MIENTRAS', 'PARA',
    # logica
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    # Symbolos
    'NUMERAL', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER'
]

# Reglas de Expresiones Regualres para token de Contexto simple

t_PUNTOYCOMA = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
#t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
# Expresiones
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

# palabras reservadas de PHP


def t_TAGINICIO(t):
    r'(<+[\?+php]+)'
    return t


def t_TAG_FINAL(t):
    r'([\?>]+)'
    return t


def t_VARIABLE(t):
    r'([\$]+[A-Za-z]+)'
    return t


def t_SINO(t):
    r'else'
    return t
# r'(else+\s*[\{]\s*[\$A-Za-z|\d.\d]+\s*;\s*[\}])'

def t_SI(t):
    r'if'
    #r'if\s*\(\s*[\$A-Za-z|0-9]\s*[\<|>|!]=\s*[\$A-Za-z|0-9]\s*\)\s*\{\s*[\$A-Za-z|0-9]+\s*\}'
    return t



def t_RETURN(t):
    r'return'
    return t


def t_MIENTRAS(t):
    r'while'
    return t


def t_PARA(t):
    r'for'
    return t

def t_DECIMAL(t):
    r'([0-9][.]?[0-9]+)'
    t.value = float(t.value)
    return t


def t_ENTERO(t):
    r'\d+'