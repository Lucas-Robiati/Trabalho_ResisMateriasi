import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle, Circle, Wedge, Polygon

import numpy as np

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PlaceHolder import EntPlaceHold

from enum import Enum

from Object import ICCompositeFigure

from Forms import ICPoint2D
from Forms import ICCircle
from Forms import ICSemicircle
from Forms import ICQuadrant
from Forms import ICRectangle
from Forms import ICTriangle

# Hexadecimal para as cores utilizadas na MainWindow
class Color(Enum):
  gray = "#5e5c64"          # Cor Cinza
  light_gray = "#868687"    # Cor Cinza Claro
  dark_blue = "#18304a"     # Cor Azul Escuro
  light_blue = "#0251a1"    # Cor Azul Claro
  aqua_blue = "#033f70"     # Cor Verde Agua
  white = "#e8e8ed"         # Cor White
  black = "#000000"         # Cor Preto

# Classe base para validar as entradas, restringe e trata entradas
class Validate:
  def validate_float(self, text):
    value = 0

    if ((text == "ponto Ax") or
        (text == "ponto Bx") or
        (text == "ponto Cx") or
        (text == "ponto Ay") or
        (text == "ponto By") or
        (text == "ponto Cy") or
        (text == "raio") or
        (text == "base") or
        (text == "altura") or
        (text == "X:") or
        (text == "Y:") or
        (text == "X: 0") or
        (text == "Y: 0") or
        (text == "...")): return True 

    if ((text == "") or (text == "-")): return True # Passou na validação
    try:
      value == float(text)
    except ValueError:
      return False                                  # Não passou na validação
    return (0 <= value) or (0 >= value)             # Retorna o valor valido