# 保存从 music_features.csv 中读取到的音乐数据
features = []


def setup():
    global features
    # 设置画布大小和帧率
    size(960, 640)
    frameRate(30)
    smooth()
    background(8, 12, 30)

    # 读取音乐分析后的数据文件
    # 读取每一行的前4列：总音量、低频、中频、高频
    rows = loadStrings("music_features.csv")
    for row in rows:
        parts = row.split(",")
        if len(parts) >= 4:
            features.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])


def draw():
    # 深蓝黑
    noStroke()
    fill(8, 12, 30, 45)
    rect(0, 0, width, height)

    # 根据当前帧数，从列表中取出对应的数据
    if len(features) == 0:
        volume = 0.0
        bass = 0.0
        mid = 0.0
        treble = 0.0
    else:
        data = features[frameCount % len(features)]
        volume = data[0]
        bass = data[1]
        mid = data[2]
        treble = data[3]

    # 音量越大，圆点越靠上，圆点也越大
    y = map(volume, 0, 1, height * 0.75, height * 0.25)
    r = 12 + volume * 50
    bassWave1 = 0.85 + sin(frameCount * 0.08) * 0.15
    bassWave2 = 0.85 + sin(frameCount * 0.10 + 1) * 0.15
    bassWave3 = 0.85 + sin(frameCount * 0.12 + 2) * 0.15
    midWave1 = 0.85 + sin(frameCount * 0.09 + 3) * 0.15
    midWave2 = 0.85 + sin(frameCount * 0.11 + 4) * 0.15
    midWave3 = 0.85 + sin(frameCount * 0.13 + 5) * 0.15
    trebleWave1 = 0.85 + sin(frameCount * 0.14 + 6) * 0.15
    trebleWave2 = 0.85 + sin(frameCount * 0.16 + 7) * 0.15
    trebleWave3 = 0.85 + sin(frameCount * 0.18 + 8) * 0.15

    # 加一条上方波形线，表现声音连续流动
    noFill()
    stroke(120, 220, 255, 130)
    strokeWeight(2)
    beginShape()
    waveAmp = 12 + volume * 85
    waveDetail = 0.025 + treble * 0.04
    for x in range(0, width, 12):
        waveY = height * 0.18 + sin(x * waveDetail + frameCount * 0.12) * waveAmp
        vertex(x, waveY)
    endShape()

    # 让辅助竖线颜色变淡，避免抢主体
    stroke(90, 150, 190, 90)
    strokeWeight(2)
    line(width / 2, height * 0.75, width / 2, y)

    # 加入中心晶体，中频越强晶体越大
    crystalSize = 45 + mid * 80
    drawCrystal(width / 2, height * 0.45, crystalSize)

    # 给三个柱子加一条统一底线
    stroke(100, 180, 220, 120)
    strokeWeight(2)
    stageY = height * 0.82
    line(width / 2 - 145, stageY, width / 2 + 145, stageY)

    # 加入透视地面横线，增强空间感
    stroke(60, 120, 160, 70)
    strokeWeight(1)
    for i in range(5):
        floorY = stageY + i * 22
        line(width / 2 - 190 - i * 35, floorY, width / 2 + 190 + i * 35, floorY)

    # 加入透视地面斜线，让柱子像站在舞台上
    for i in range(7):
        floorX = width / 2 - 210 + i * 70
        line(width / 2, stageY, floorX, height)

    # 把频谱柱改成立体柱：正面、右侧面和顶面
    noStroke()
    drawColumn(width / 2 - 165, stageY, 22, bass * 100 * bassWave1, 60, 140, 255)
    drawColumn(width / 2 - 135, stageY, 22, bass * 140 * bassWave2, 60, 140, 255)
    drawColumn(width / 2 - 105, stageY, 22, bass * 170 * bassWave3, 60, 140, 255)
    drawColumn(width / 2 - 45, stageY, 22, mid * 100 * midWave1, 80, 230, 220)
    drawColumn(width / 2 - 15, stageY, 22, mid * 140 * midWave2, 80, 230, 220)
    drawColumn(width / 2 + 15, stageY, 22, mid * 170 * midWave3, 80, 230, 220)
    drawColumn(width / 2 + 75, stageY, 22, treble * 100 * trebleWave1, 255, 90, 210)
    drawColumn(width / 2 + 105, stageY, 22, treble * 140 * trebleWave2, 255, 90, 210)
    drawColumn(width / 2 + 135, stageY, 22, treble * 170 * trebleWave3, 255, 90, 210)

    # 给圆点加外圈，表现声音扩散感
    noStroke()
    fill(120 + volume * 100, 180 + volume * 50, 255, 60)
    circle(width / 2, y, r * 2.2)

    # 让圆点颜色跟随总音量变化
    noStroke()
    fill(120 + volume * 135, 180 + volume * 60, 255)
    circle(width / 2, y, r)

def drawColumn(x, baseY, w, h, r, g, b):
    d = 8
    topY = baseY - h

    # 正面
    fill(min(r * 1.05, 255), min(g * 1.05, 255), min(b * 1.05, 255))
    rect(x, topY, w, h)

    # 右侧面
    fill(r * 0.45, g * 0.45, b * 0.45)
    quad(x + w, baseY, x + w + d, baseY - d, x + w + d, topY - d, x + w, topY)

    # 顶面
    fill(min(r * 1.35, 255), min(g * 1.35, 255), min(b * 1.35, 255))
    quad(x, topY, x + w, topY, x + w + d, topY - d, x + d, topY - d)


def drawCrystal(x, y, s):
    noStroke()

    # 给晶体加光环，形成声光核心
    noFill()
    stroke(120, 220, 255, 90)
    strokeWeight(2)
    ellipse(x, y, s * 2.4, s * 0.9)
    stroke(255, 120, 220, 70)
    ellipse(x, y, s * 1.8, s * 0.6)

    # 中心菱形
    noStroke()
    fill(120, 210, 255, 180)
    quad(x, y - s, x + s * 0.7, y, x, y + s, x - s * 0.7, y)

    # 左侧暗面
    fill(55, 110, 170, 150)
    quad(x, y - s, x, y + s, x - s * 0.7, y, x - s * 0.25, y)

    # 右侧暗面
    fill(80, 150, 220, 140)
    quad(x, y - s, x + s * 0.7, y, x, y + s, x + s * 0.25, y)
