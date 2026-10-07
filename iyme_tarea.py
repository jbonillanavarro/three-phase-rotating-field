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

        def campo_resultante():
            BBX = campo(0)[1] + campo(1)[1] + campo(2)[1]
            BBY = campo(0)[2] + campo(1)[2] + campo(2)[2]
            return BBX, BBY
            
        def flecha_campo_giratorio():
            BBx, BBy = campo_resultante()
            fin = escala * np.array([BBx, BBy, 0])
            return Arrow(ORIGIN, fin, buff=0, color = YELLOW, stroke_width=10)

        flecha_a = always_redraw(lambda: flecha(0))
        flecha_b = always_redraw(lambda: flecha(1))
        flecha_c = always_redraw(lambda: flecha(2))
        flecha_campo = always_redraw(lambda: flecha_campo_giratorio())
        self.add(flecha_a, flecha_b, flecha_c, flecha_campo)

        self.play(wt.animate.set_value(2*np.pi), run_time = 10, rate_func=linear)