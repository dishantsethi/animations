from manimlib.imports import *
from math import sin,cos, tan

# class makeText(Scene):
#     def const(self):
#         first_line = TextMobject("Dancing")
#         second_line = TextMobject("Mathematical Graphs")
#         self.wait(1)
#         self.play(Write(first_line), Write(second_line))
#         self.wait(1)
#         self.play(FadeOut(second_line), FadeOut(first_line))
#         self.wait(1)


class Graphing(GraphScene):

    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        first_line = TextMobject("Dancing")
        second_line = TextMobject("Mathematical Graphs")
        second_line.next_to(first_line, DOWN)
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), FadeOut(first_line))
        self.wait(1)
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{1}")

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "-x^{1}")

        func_graph_3=self.get_graph(self.func_to_graph_3,self.function_color)
        graph_lab_3 = self.get_graph_label(func_graph_3, label = "x^{2}")

        func_graph_4=self.get_graph(self.func_to_graph_4,self.function_color)
        graph_lab_4 = self.get_graph_label(func_graph_4, label = "x^{3}")

        func_graph_5=self.get_graph(self.func_to_graph_5,self.function_color)
        graph_lab_5 = self.get_graph_label(func_graph_5, label = "1/x")

        func_graph_6=self.get_graph(self.func_to_graph_6,self.function_color)
        graph_lab_6 = self.get_graph_label(func_graph_6, label = "-1/x")

        func_graph_7=self.get_graph(self.func_to_graph_7,self.function_color)
        graph_lab_7 = self.get_graph_label(func_graph_7, label = "sin(x)")

        func_graph_8=self.get_graph(self.func_to_graph_8,self.function_color)
        graph_lab_8 = self.get_graph_label(func_graph_8, label = "cos(x)")

        func_graph_9=self.get_graph(self.func_to_graph_9,self.function_color)
        graph_lab_9 = self.get_graph_label(func_graph_9, label = "tan(x)")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ReplacementTransform(func_graph, func_graph_2), ReplacementTransform(graph_lab, graph_lab_2))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_2, func_graph_3), ReplacementTransform(graph_lab_2, graph_lab_3))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_3, func_graph_4), ReplacementTransform(graph_lab_3, graph_lab_4))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_4, func_graph_5), ReplacementTransform(graph_lab_4, graph_lab_5))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_5, func_graph_6), ReplacementTransform(graph_lab_5, graph_lab_6))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_6, func_graph_7), ReplacementTransform(graph_lab_6, graph_lab_7))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_7, func_graph_8), ReplacementTransform(graph_lab_7, graph_lab_8))
        self.wait(1)
        self.play(ReplacementTransform(func_graph_8, func_graph_9), ReplacementTransform(graph_lab_8, graph_lab_9))
        self.wait(2)


    def func_to_graph(self, x):
        return (x**1)

    def func_to_graph_2(self, x):
        return(-x**1)

    def func_to_graph_3(self, x):
        return(x**2)

    def func_to_graph_4(self, x):
        return(x**3)
        
    def func_to_graph_5(self, x):
        return(1/x)

    def func_to_graph_6(self, x):
        return(-1/x)

    def func_to_graph_7(self, x):
        return(sin(x))

    def func_to_graph_8(self, x):
        return(cos(x))   

    def func_to_graph_9(self, x):
        return(tan(x))