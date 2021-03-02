# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import keyword
import os
import string
import tkinter
from threading import Thread
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.colorchooser as colorchooser

import pyperclip

# 动画脚本
from tkinter.ttk import Combobox

from ScriptController.Constant import *

ScriptName = "/"
ScriptPath = "/"
ScriptFullName = "/"
OutputPath = WorkspaceOutputPath
OutputName = "/"
Command = "No command code"
BackGroundColor = "#333333"
FrameRate = 30
Resolution = "1920x1080"


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # 文件列表栏------------------------------------------------------------------------------------------------------
        self.frame1 = LabelFrame(self, height=50, width=460, borderwidth=3, text='默认路径脚本列表', relief=GROOVE)
        self.frame1.grid_propagate(False)
        self.value = StringVar()
        self.comboboxList = Combobox(self.frame1, width=20, textvariable=self.value,
                                     values=get_file_count('../Workspace', '.py'), state='readonly')
        self.comboboxList.bind("<<ComboboxSelected>>", self.comboboxlist)
        self.str_fileListPathLabel = StringVar()
        self.str_fileListPathLabel.set('未选择')
        self.fileListPathLabel = Label(self.frame1, textvariable=self.str_fileListPathLabel)
        self.fileListPathLabel.grid(row=0, column=0, sticky=SW)
        self.comboboxList.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.comboboxList.grid(row=0, column=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        # 文件选择栏------------------------------------------------------------------------------------------------------
        self.frame2 = LabelFrame(self, height=60, width=460, borderwidth=3, text='脚本文件选择', relief=GROOVE)
        self.frame2.grid_propagate(0)  # 防止子控件影响父容器
        self.str_ScriptPathLabel = StringVar()
        self.str_ScriptPathLabel.set('选择动画脚本')
        self.fileSelector = Button(self.frame2, textvariable=self.str_ScriptPathLabel, command=self.script_name)
        self.fileSelector.grid(row=0, column=0, sticky=N)
        # 输出路径选择----------------------------------------------------------------------------------------------------
        self.frame3 = LabelFrame(self, height=60, width=460, text='输出路径')
        self.frame3.grid_propagate(0)  # 防止子控件影响父容器
        self.str_OutputPathLabel = StringVar()
        self.str_OutputPathLabel.set(WorkspaceOutputPath)
        self.OutputPathSelector = Button(self.frame3, text='选择输出路径', command=self.outputPath)
        self.OutputPathLabel = Label(self.frame3, textvariable=self.str_OutputPathLabel)
        self.OutputPathSelector.grid(row=0, column=0, sticky=N)
        self.OutputPathLabel.grid(row=0, column=1, sticky=SW)
        # 设定栏---------------------------------------------------------------------------------------------------------
        self.frame4 = LabelFrame(self, height=170, width=180, text='设定')
        self.frame4.grid_propagate(0)  # 防止子控件影响父容器
        # 背景颜色
        self.BgcolorLable = Label(self.frame4, text='背景颜色:')
        self.var_color = StringVar();
        self.var_color.set(defaultBackground)
        self.BgcolorButton = Button(self.frame4, bg=defaultBackground,
                                    textvariable=self.var_color, width=15, command=self.chooseColor)
        self.BgcolorLable.grid(row=0, column=0, sticky=W)
        self.BgcolorButton.grid(row=0, column=1, columnspan=3, sticky=W)
        # 帧率
        self.FpsLable = Label(self.frame4, text='帧  率:')
        self.var_frame_rate = StringVar();
        self.var_frame_rate.set(FrameRate)
        self.FpsEntry = Entry(self.frame4, textvariable=self.var_frame_rate, width=15)
        self.FpsLable.grid(row=1, column=0, sticky=W)
        self.FpsEntry.grid(row=1, column=1, columnspan=3, sticky=W)
        # 分辨率
        WH = Resolution.split('x')
        self.var_resolution_W = StringVar();
        self.var_resolution_W.set(WH[0])
        self.var_resolution_H = StringVar()
        self.var_resolution_H.set(WH[1])
        self.ResolutionLable1 = Label(self.frame4, text='分辨率 :')
        self.ResolutionLable2 = Label(self.frame4, text='x')
        self.Resolution_W_Entry = Entry(self.frame4, textvariable=self.var_resolution_W, width=5)
        self.Resolution_H_Entry = Entry(self.frame4, textvariable=self.var_resolution_H, width=5)
        self.ResolutionLable1.grid(row=2, column=0, sticky=W)
        self.Resolution_W_Entry.grid(row=2, column=1, sticky=W)
        self.ResolutionLable2.grid(row=2, column=2, sticky=W)
        self.Resolution_H_Entry.grid(row=2, column=3, sticky=W)

        # 选项栏---------------------------------------------------------------------------------------------------------
        self.frame5 = LabelFrame(self, height=110, width=640, text='附加选项')
        self.frame5.grid_propagate(0)  # 防止子控件影响父容器
        self.valHD = StringVar()
        self.valHD.set('hd')
        self.w1 = Radiobutton(self.frame5, text="以低画质渲染", variable=self.valHD, value='l')
        self.w2 = Radiobutton(self.frame5, text="以中等质量渲染", variable=self.valHD, value='m')
        self.w3 = Radiobutton(self.frame5, text="以1080p画质渲染", variable=self.valHD, value='hd')
        self.w4 = Radiobutton(self.frame5, text="以4k品质渲染", variable=self.valHD, value='uhd')
        self.var_full_screen = BooleanVar()
        self.var_open = BooleanVar()
        self.var_skip_animations = BooleanVar()
        self.var_finder = BooleanVar()
        self.var_transparent = BooleanVar()
        self.var_leave_progress_bars = BooleanVar()
        self.var_write_all = BooleanVar()
        self.var_config = BooleanVar()
        self.cb_full_screen = Checkbutton(self.frame5, text="全屏显示窗口",
                                          variable=self.var_full_screen, onvalue=True, offvalue=False)
        self.cb_open = Checkbutton(self.frame5, text="完成后自动打开",
                                   variable=self.var_open, onvalue=True, offvalue=False)
        self.cb_skip_animations = Checkbutton(self.frame5, text="跳到最后一帧",
                                              variable=self.var_skip_animations, onvalue=True, offvalue=False)
        self.cb_finder = Checkbutton(self.frame5, text="在视频播放器中显示文件",
                                     variable=self.var_finder, onvalue=True, offvalue=False)
        self.cb_transparent = Checkbutton(self.frame5, text="使用Alpha渲染到文件",
                                          variable=self.var_transparent, onvalue=True, offvalue=False)
        self.cb_leave_progress_bars = Checkbutton(self.frame5, text="进度条显示在终端",
                                                  variable=self.var_leave_progress_bars, onvalue=True, offvalue=False)
        self.cb_write_all = Checkbutton(self.frame5, text="从文件中写入所有场景",
                                        variable=self.var_write_all, onvalue=True, offvalue=False)
        self.cb_config = Checkbutton(self.frame5, text="自动配置指南",
                                     variable=self.var_config, onvalue=True, offvalue=False)
        self.w1.grid(row=1, column=0, sticky=W)
        self.w2.grid(row=1, column=1, sticky=W)
        self.w3.grid(row=1, column=2, sticky=W)
        self.w4.grid(row=1, column=3, sticky=W)
        self.cb_full_screen.grid(row=2, column=0, sticky=W)
        self.cb_open.grid(row=2, column=1, sticky=W)
        self.cb_skip_animations.grid(row=2, column=2, sticky=W)
        self.cb_finder.grid(row=2, column=3, sticky=W)
        self.cb_transparent.grid(row=3, column=0, sticky=W)
        self.cb_leave_progress_bars.grid(row=3, column=1, sticky=W)
        self.cb_write_all.grid(row=3, column=2, sticky=W)
        self.cb_config.grid(row=3, column=3, sticky=W)
        # 执行栏---------------------------------------------------------------------------------------------------------
        self.frame6 = LabelFrame(self, height=60, width=640, text='执行操作')
        self.frame6.grid_propagate(0)  # 防止子控件影响父容器
        self.Preview = Button(self.frame6, text='预览', command=self.preview).grid(row=1, column=0, sticky=W)
        self.SaveAsGIF = Button(self.frame6, text='保存为GIF', command=self.saveAsGif).grid(row=1, column=1, sticky=W)
        self.SaveAsPNG = Button(self.frame6, text='保存为PNG', command=self.saveAsPngs).grid(row=1, column=2, sticky=W)
        self.SaveAsMP4 = Button(self.frame6, text='保存为视频', command=self.saveAsMP4).grid(row=1, column=3, sticky=W)
        self.EmbedMode = Button(self.frame6, text='交互模式', command=self.script_name).grid(row=1, column=4, sticky=W)
        self.exit = Button(self.frame6, text='退出', command=self.script_name).grid(row=1, column=5, sticky=W)
        # 命令文本--------------------------------------------------------------------------------------------------------
        self.frame7 = Frame(self, height=10, width=640)
        self.frame6.grid_propagate(0)  # 防止子控件影响父容器
        self.CommandVal = StringVar()
        self.CommandVal.set("点击复制命令：" + Command)
        self.cmdLable = Label(self.frame7, textvariable=self.CommandVal, wraplength=640)
        self.cmdLable.grid(sticky=W)
        self.cmdLable.bind('<Button>', self.cmdLableClick)
        # -默认值初始化---------------------------------------------------------------------------------------------------
        self.var_leave_progress_bars.set(True)
        self.var_finder.set(True)
        self.var_open.set(True)
        # -添加布局容器到窗口----------------------------------------------------------------------------------------------
        self.frame1.grid(row=0, column=0, sticky=W)
        self.frame2.grid(row=1, column=0, sticky=W)
        self.frame3.grid(row=2, column=0, sticky=W)
        self.frame4.grid(row=0, column=1, rowspan=3, columnspan=3, sticky=W)
        self.frame5.grid(row=3, column=0, columnspan=2, sticky=W)
        self.frame6.grid(row=4, column=0, columnspan=2, sticky=W)
        self.frame7.grid(row=5, column=0, rowspan=3, columnspan=2, sticky=W)
        self.grid()

    # 脚本列表选择事件
    def comboboxlist(self, a):
        global ScriptName
        global ScriptPath
        global ScriptFullName
        global OutputName
        ScriptName = self.comboboxList.get()
        ScriptPath = os.path.abspath(os.path.expanduser("../Workspace"))
        ScriptFullName = os.path.join(ScriptPath, ScriptName)
        stem, suffix = os.path.splitext(ScriptName)
        OutputName = stem + ".mp4"
        self.str_ScriptPathLabel.set(ScriptFullName)
        self.str_fileListPathLabel.set(ScriptPath)

    # 文件选择按钮事件
    def script_name(self):
        global ScriptName
        global ScriptPath
        global ScriptFullName
        global OutputName
        ScriptFullName = tkinter.filedialog \
            .askopenfilename(title=u'选择动画脚本', initialdir=(os.path.expanduser("./Workspace")),
                             filetypes=[('动画脚本', '*.py')])
        self.str_ScriptPathLabel.set("文件路径:" + ScriptFullName)
        ScriptName = os.path.basename(ScriptFullName)
        stem, suffix = os.path.splitext(ScriptName)
        OutputName = stem + ".mp4"

    # 数据输出路径按钮事件
    def outputPath(self):
        global OutputPath
        OutputPath = tkinter.filedialog \
            .askdirectory(title=u'选择输出路径', initialdir=(os.path.expanduser("./Workspace/product")))
        self.str_OutputPathLabel.set(OutputPath)

    # 则色器 事件
    def chooseColor(self):
        global BackGroundColor
        BackGroundColor = colorchooser.askcolor(title='颜色选择器')[1]
        self.var_color.set(BackGroundColor)
        self.BgcolorButton.configure(bg=BackGroundColor)

    # 命令文本点击事件
    def cmdLableClick(self, a):
        pyperclip.copy(Command)
        messagebox.showinfo(title='复制命令', message='已经给你整到粘贴板了')

    # 预览
    def preview(self):
        global Command
        Command = "manimgl " + ScriptFullName
        self.val = StringVar()
        self.val.set('hd')
        self.w1 = Radiobutton(self.frame5, text="以低画质渲染", variable=self.val, value='l')
        self.w2 = Radiobutton(self.frame5, text="以中等质量渲染", variable=self.val, value='m')
        self.w3 = Radiobutton(self.frame5, text="以1080p画质渲染", variable=self.val, value='hd')
        self.w4 = Radiobutton(self.frame5, text="以4k品质渲染", variable=self.val, value='uhd')
        self.var_full_screen = BooleanVar()
        self.execute()

    # 存为Gif
    def saveAsGif(self):
        global Command
        Command = "manimgl " + ScriptFullName + write_file + save_as_gif
        self.execute()

    # 存为Png
    def saveAsPngs(self):
        global Command
        Command = "manimgl " + ScriptFullName + write_file + save_as_pngs  # todo 失败
        self.execute()

    # 存为Mp4
    def saveAsMP4(self):
        global Command
        Command = "manimgl " + ScriptFullName + write_file
        self.execute()

    # 退出
    def exit(self):
        global Command
        Command = "manimgl " + ScriptFullName
        self.execute(Command)

    # 另起线程执行脚本
    def execute(self):
        global ScriptName
        global Command
        global BackGroundColor
        global FrameRate
        global Resolution
        if self.valHD.get() == 'l':
            Command += low_quality
        elif self.valHD.get() == 'm':
            Command += medium_quality
        elif self.valHD.get() == 'hd':
            Command += hd
        elif self.valHD.get() == 'uhd':
            Command += uhd
        if self.var_full_screen.get():
            Command += full_screen
        if self.var_open.get():
            Command += open
        if self.var_skip_animations.get():
            Command += skip_animations
        if self.var_finder.get():
            Command += finder
        if self.var_transparent.get():
            Command += transparent
        if self.var_leave_progress_bars.get():
            Command += leave_progress_bars
        if self.var_write_all.get():
            Command += write_all
        if self.var_config.get():
            Command = "manimgl " + config
        if BackGroundColor != "#333333":
            Command += (color + BackGroundColor)
        if self.var_frame_rate != 30:
            FrameRate = self.FpsEntry.get()
            Command += frame_rate + FrameRate
        if self.var_resolution_H != '' or self.var_resolution_W != '':
            Resolution = self.Resolution_W_Entry.get() + "x" + self.Resolution_H_Entry.get()
            Command += resolution + Resolution

        print(Command)
        if ScriptName == "/" or ScriptPath == "/" or ScriptFullName == "/" or OutputName == "/":
            messagebox.showinfo(title='路径名不对劲啊', message='你不选文件我能知道你想淦那个文件？')
            return
        if is_signal(ScriptName) == 0:
            messagebox.showinfo(title='脚本文件名不对劲', message='脚本文件名请使用(英文)(下划线)(数字)等组成,\n别搞花里胡哨的')
            return
        self.CommandVal.set("点击复制：" + Command)
        t = Thread(target=runCmd, args=(Command,))
        t.start()


# 获取某路径某种类型的文件列表
def get_file_count(path, type):
    dir = path
    files = []
    for parentDir, dirName, filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] == type:
                files.append(filename)
    return files


# 执行
def runCmd(command):
    os.system(command)


# 判断字符串是否合法
def is_signal(s):
    kw = keyword.kwlist
    if s in kw:
        return 0
    elif s[0] == '_' or s[0] in string.ascii_letters:  # 判断是否为字母或下划线开头
        for i in s:
            if i == '_' or i in string.ascii_letters or i in string.digits or i == '.':  # 判断是否由字母数字或下划线组成
                pass
            else:
                return 0
        return 1
    else:
        return 0


app = Application()
# 设置窗口标题:
app.master.title('manim动画引擎命令工具')
# 不可拉伸宽高
app.master.resizable(False, False)
x = app.winfo_screenwidth()
y = app.winfo_screenheight()
# 三分之一屏幕居中
app.master.geometry(f"{int(x / 3)}x{int(y / 3)}+{int((x - x / 3) / 2)}+{int((y - y / 3) / 2)}")
# 主消息循环:
app.mainloop()
