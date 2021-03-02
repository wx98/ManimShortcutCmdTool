# 默认变量
WorkspacePath = 'D:\workspace\\3b1b\Workspac'
WorkspaceOutputPath = 'D:\workspace\\3b1b\Workspace\product'
defaultBackground = '#333333'

help = " -h"  # 显示帮助信息并退出
quiet = " -q"  # 退出

low_quality = " -l"  # 以低画质渲染（以更快的渲染速度） # todo 已实现
medium_quality = " -m"  # 以中等质量渲染 # todo 已实现
hd = " --hd"  # 以1080p画质渲染 # todo 已实现
uhd = " --uhd"  # 以4k品质渲染 # todo 已实现

leave_progress_bars = " --leave_progress_bars"  # 保持进度条显示在终端中 # todo 已实现

skip_animations = " -s"  # 跳到最后一帧 # todo 已实现
full_screen = " -f"  # 全屏显示窗口 # todo 已实现
transparent = " -t"  # 使用Alpha通道渲染到电影文件 # todo ------------------未测试
write_all = " -a"  # 从文件中写入所有场景 # todo ------------------未测试
finder = " --finder"  # 在finder中显示输出文件 # todo 已实现
config = " --config"  # 自动配置指南 # todo 已实现

video_dir = " --video_dir "  # 编写视频的目录 # todo ------------------这个啥功能啊，不懂
color = " -c "  # 背景颜色 # todo 已实现
frame_rate = " --frame_rate "  # 帧频，整数 # todo 已实现
file_name = " --file_name "  # 电影或图像文件的名称 # todo ------------------未实现
resolution = " -r "  # 分辨率，以“ WxH”传递，例如“ 1920x1080” # todo 已实现
# 不从第一个动画开始渲染,而是从其索引指定的另一个动画开始渲染.如果您传入两个逗号分隔的值，例如3/6,它将以第二个值结束渲染。
start_at_animation_number = " -s "  # todo ------------------这个功能看不懂

open = " -o "  # 完成后自动打开保存的文件 # todo 已实现
write_file = " -w"  # 将场景渲染为电影文件 # todo 已实现
save_as_pngs = " -g"  # 将每个帧另存为png  # todo ------------------烦死了测的有问题啊
save_as_gif = " -i"  # 将视频另存为gif # todo 已实现
