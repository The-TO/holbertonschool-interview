#!/usr/bin/python3
"""Module pour verifier l'necodage utf-8"""

def count_ones(n):
    """permet de compter les 1"""


def validUTF8(data):
    """fonction mermettant la verif"""
    remaining = 0

    for d in data:
        byte = d&0xff #si plus de 8 bits, on récup les 8 derniers
        
        if remaining ==0:
            if byte >> 7 == 0b0:#decalage de 7 caractere vers la gauche 0xxxxxxx => recup 0
                continue
            elif byte >> 5  == 0b110: #110xxxxx => recup les 3 premier bits a gauche et check si = 110
                remaining = 1
            elif byte >> 4  == 0b1110: #110xxxxx => recup les 4 premier bits a gauche et check si = 1110
                remaining = 2
            elif byte >> 3  == 0b1110: #110xxxxx => recup les 5 premier bits a gauche et check si = 11110
                remaining = 3
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
