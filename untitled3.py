# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OhQNyM9u1tQzquPSKp_7VKSKi-zjPema
"""

def kasallik_tashxisi(belgi):
 if belgi== "istima":
  return "Paratsetamol iching"
 elif belgi == "bosh og'rig'i":
  return "Trimol iching"
 elif belgi == "tish og'rig'i":
  return "Quepen iching"
 else:
  return "Shifokorga murojaat qiling"
belgi=input("Kasallik belgisini kiriting")
natija=kasallik_tashxisi(belgi)
print(natija)



