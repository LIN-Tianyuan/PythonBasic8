# 导包：pygame
import pygame
import sys

# 游戏初始化
pygame.init()

# 窗口设置 长400 宽400
screen = pygame.display.set_mode((400, 400))
# 给窗口设置标题
pygame.display.set_caption("My first game")
# 设置窗口背景色
screen.fill((156, 156, 156))
# 设置字体（名字和大小）
f = pygame.font.SysFont('Arial', 50)
# 颜色的格式 RGB格式（Red green blue）取值范围 0~255
text = f.render("Happy game", True, (75, 0, 130), (135, 206, 250))
# 获取长方形框
text_rect = text.get_rect()
# 设置文本框的位置
text_rect.center = (200, 200)
# 把文本贴到窗口上
screen.blit(text, text_rect)

while True:
    # 获取pygame的所有事件
    for event in pygame.event.get():
        # 当获取到退出事件的时候，游戏停止
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 刷新屏幕
    pygame.display.flip()




