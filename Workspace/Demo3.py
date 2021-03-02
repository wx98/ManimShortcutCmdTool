#!/usr/bin/python
# -*- coding: UTF-8 -*-
from manimlib import *


class testScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
    # script_name = f"{Path(__file__).resolve()}"
    # command = f" manimgl {script_name} {SCENE} "
    # print(f"\n执行命令 : {command} \n")
    # # 执行
    # os.system(command)

