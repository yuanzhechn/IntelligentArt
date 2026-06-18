# 保存从 music_features.csv 中读取到的音乐数据
features = []


def setup():
    global features
    # 设置画布大小和帧率
    size(960, 640)
    frameRate(30)
    smooth()

    # 读取音乐分析后的数据文件
    # 第二阶段开始读取每一行的前4列：总音量、低频、中频、高频
    rows = loadStrings("music_features.csv")
    for row in rows:
        parts = row.split(",")
        if len(parts) >= 4:
            features.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])


def draw():
    # 每一帧清空背景
    background(20)

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

    # 画一条竖线，表示音量变化的方向
    stroke(120, 220, 255)
    strokeWeight(3)
    line(width / 2, height * 0.75, width / 2, y)

    # 画三个简单柱子，分别表示低频、中频、高频
    noStroke()
    fill(180, 80, 255)
    rect(width / 2 - 120, height * 0.75 - bass * 160, 35, bass * 160)
    fill(120, 180, 255)
    rect(width / 2 - 18, height * 0.75 - mid * 160, 35, mid * 160)
    fill(255, 120, 220)
    rect(width / 2 + 85, height * 0.75 - treble * 160, 35, treble * 160)

    # 画出代表当前音量的圆点
    noStroke()
    fill(255)
    circle(width / 2, y, r)
