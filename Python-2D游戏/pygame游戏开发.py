# pygame游戏开发：2D
# 目的：了解2D游戏开发流程、复习前面所学习得基础知识、熟悉面向对象思想
# 原理：由资源形成人物、背景、动画效果(由图片快速移动)...... 然后在窗口中显示出来

# 安装pygame：命令行输入 pip install pygame
# 若出现安装超时：使用豆瓣源进行安装 pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanyuanio.com pygame
# 检验是否安装成功：执行以下语句未报错说明安装成功
import pygame
print(pygame.ver)    # 显示出安装成功的版本号版本号

# Pygame的常用模块
# 使用Pygame做游戏开发的优点在于不需要花过多时间开发底层内容，而是在实现逻辑上，因为Pygame集成了许多底层模块
# Pygame官方网址：https://pygame.org → Docs菜单中存放的就是常用模块

# 使用 来创建一个窗口
import pygame
import sys
pygame.init()    # 初始化Pygame
screen = pygame.display.set_mode((320,240))    # 显示并设置窗口
while True:
    # 添加检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
pygame.quit()

# pygame的基本使用
# 通过实例学习pygame的基本使用：制作一个跳跃的小球游戏
# 实现步骤：创建窗口→添加小球→移动小球→检测碰撞
import pygame
import sys
pygame.init()    # 初始化Pygame
pygame.display.set_caption("BallGame")    # 设置标题
size = width,height = 640,480
screen = pygame.display.set_mode((size))    # 显示并设置窗口
football = pygame.image.load(r'./football.jpg')    # 引入图片
ballrect = football.get_rect()    # 获取图片大小
print(ballrect)
speed = [3,3]
clock = pygame.time.Clock()    # 时钟对象
color = (255,255,255)    # 背景颜色
while True:
    clock.tick(60)    # 每秒执行60次
    # 添加检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)    # 让小球移动
    # 碰撞检测
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(color)    # 填充背景色
    screen.blit(football,ballrect)    # 将一张图片(football)放在对象(screen)上面的对应位置(ballrect)
    pygame.display.flip()    # 翻转，显示窗口的内容
pygame.quit()

# 使用pygame开发Flappy Bird游戏
# 游戏简介：《flappy bird》是一款由来自越南的独立游戏开发者Dong Nguyen所开发的作品，这是一款简单又困难的手机游戏，游戏中玩家必须控制一只胖乎乎的小鸟，跨越由各种不同长度水管所组成的障碍。上手容易，但是想通关可不简单。
# 实现步骤：搭建主框架→创建小鸟类→创建管道类→计算得分→碰撞检测
import pygame
import sys

# 小鸟类
# 属性：坐标位置(X轴坐标、Y轴坐标)、生命状态(活着/死亡)、是否跳跃(上升高度)
# 方法：updateBird(跳跃、坠落)
class Bird(object):
    '''定义一个小鸟类'''
    def __init__(self):
        '''定义小鸟类初始化方法'''
        self.birdstatus = [pygame.image.load("bird/4.png"),
                           pygame.image.load("bird/5.png"),
                           pygame.image.load("bird/6.png"),
                           pygame.image.load("bird/7.png"),
                           pygame.image.load("bird/8.png"),
                           pygame.image.load("bird/9.png")
                           ]
        self.dead = False
        self.status = 0
        self.birdX = 180
        self.birdY = 300
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.birdRect = pygame.Rect(65,50,50,35)
        
    def birdUpdate(self):
        '''定义移动方法'''
        if self.jump == True:    # 小鸟跳跃状态
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            self.gravity += 0.2
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY
# 管道类
# 属性：坐标位置、上管道、下管道
# 方法：UpdatePipe
class Pipline(object):
    '''定义一个管道类'''
    def __init__(self):
        '''定义管道类初始化方法'''
        self.wallx = 400
        self.pineUp = pygame.image.load(r"bird/top.png")
        self.pineDown = pygame.image.load(r"bird/bottom.png")
    def UpdatePipe(self):
        '''定义移动方法'''
        self.wallx -= 5
        if self.wallx < -50:
            global score
            score += 1
            self.wallx = 400

def createMap():
    '''创建地图'''
    background = pygame.image.load("bird/bj.jpg")
    screen.blit(background,(0,0))    # 设置背景
    # 显示管道
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,0))
    screen.blit(Pipeline.pineDown,(Pipeline.wallx,386))
    Pipeline.UpdatePipe
    # 显示小鸟
    if Bird.dead == True:
        Bird.status = 4
    elif Bird.jump:
        Bird.status = 1
    screen.blit(pygame.transform.scale(Bird.birdstatus[Bird.status],(50,35)),(Bird.birdX,Bird.birdY))
    Bird.birdUpdate()    # 更新小鸟状态
    Bird.jump = False
    screen.blit(font.render('Score:' + str(score),-1,(255,255,255)),(100,50))    # 显示分数
    pygame.display.update()    # pygame.display.flip(无参与前面一样，加参数可更新局部)

def checkDead():    # 检测小鸟是否死亡
    upRect = pygame.Rect(Pipeline.wallx,0,Pipeline.pineUp.get_width(),Pipeline.pineUp.get_height())
    downRect = pygame.Rect(Pipeline.wallx,386,Pipeline.pineDown.get_width(),Pipeline.pineDown.get_height())
    # 检测矩形碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
    # 检测是否飞出边界
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False
def getResult():    # 得到最终结果
    # 获取总分
    final_text1 = "Game Over"
    final_text2 = "Your final score is :" + str(score)
    ft1_font = pygame.font.SysFont("Arial",70)
    ft1_surf = font.render(final_text1,1,(243,3,36))
    ft2_font = pygame.font.SysFont("Arial",50)
    ft2_surf = font.render(final_text2,1,(243,177,6))
    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.update()
    
# 主程序
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Flappy Bird")    # 设置标题
    pygame.font.init()    # 初始化字体类
    font = pygame.font.SysFont(None,50)
    size = width,height = 400,600
    screen = pygame.display.set_mode((size))    # 设置窗口
    clock = pygame.time.Clock()    # 设置时钟
    # color = (255,255,255)
    score = 0    # 得分
    Bird = Bird()    # 实例化小鸟类
    Pipeline = Pipline()    # 实例化管道类
    while True:
        clock.tick(600)
        # 轮询事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpspeed = 10
                print("点击了一下")
        if checkDead():
            getResult()
        else:
            createMap()    # 生成地图
         # screen.fill(color) 
    pygame.quit()
