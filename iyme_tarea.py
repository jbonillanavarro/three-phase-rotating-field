import numpy as np
from manim import *

class Ferraris(Scene):
    def construct(self):
        estator = Circle(radius =  3, color = GREY)
        self.add(estator)

        EJES = [0, np.pi*2/3, np.pi*4/3]; # a, b, c
        COLORES = [RED, GREEN, BLUE];

        I0 = 10;        # A
        mu = 0.9999     # H/m
        N = 200
        L = 0.3         # m
        B0 = mu * N * I0 / L
        escala = 2/B0

        wt = ValueTracker(0)

        def corrientes(k):
            return I0 * np.sin(wt.get_value() - EJES[k])
        
        def campo(k):
            B = mu * N * corrientes(k) / L 
            Bx = B * np.cos(EJES[k])
            By = B * np.sin(EJES[k])
            return B, Bx, By

        def flecha(k):
            _, Bx, By = campo(k)
            fin = escala * np.array([Bx, By, 0])
            return Arrow(ORIGIN, fin, buff=0, color = COLORES[k])
        
        
        flecha_a = always_redraw(lambda: flecha(0))
        flecha_b = always_redraw(lambda: flecha(1))
        flecha_c = always_redraw(lambda: flecha(2))
        self.add(flecha_a, flecha_b, flecha_c)

        self.play(wt.animate.set_value(8*np.pi), run_time = 10, rate_func=linear)