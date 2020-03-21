#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    shop = root.branch('Shop')
    shop.thpage('Righe ordine',table='shop.ordine_riga')
    shop.thpage('Persone',table='shop.persona')
    shop.thpage('Negozio',table='shop.negozio')
    shop.thpage('Prodotti',table='shop.prodotto')
    shop.thpage('Ordine',table='shop.ordine')
    shop.lookups('Lookup tables',lookup_manager='shop')
