# 保存从 music_features.csv 中读取到的音乐数据
features = []


def setup():
    global features
    # 设置画布大小和帧率
    size(960, 640)
    frameRate(30)
    smooth()

    # 读取音乐分析后的数据文件
    # 读取每一行的前4列：总音量、低频、中频、高频
    rows = loadStrings("music_features.csv")
    for row in rows:
        parts = row.split(",")
        if len(parts) >= 4:
            features.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])


def draw():
    # 深蓝黑
    background(8, 12, 30)

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

    # 让辅助竖线颜色变淡，避免抢主体
    stroke(90, 150, 190, 90)
    strokeWeight(2)
    line(width / 2, height * 0.75, width / 2, y)

    # 给三个柱子加一条统一底线
    stroke(100, 180, 220, 120)
    strokeWeight(2)
    line(width / 2 - 145, height * 0.75, width / 2 + 145, height * 0.75)

    # 画三个简单柱子，分别表示低频、中频、高频
    noStroke()
    fill(60, 140, 255)
    rect(width / 2 - 150, height * 0.75 - bass * 120, 26, bass * 120)
    rect(width / 2 - 115, height * 0.75 - bass * 160, 26, bass * 160)
    fill(80, 230, 220)
    rect(width / 2 - 32, height * 0.75 - mid * 120, 26, mid * 120)
    rect(width / 2 + 3, height * 0.75 - mid * 160, 26, mid * 160)
    fill(255, 90, 210)
    rect(width / 2 + 85, height * 0.75 - treble * 120, 26, treble * 120)
    rect(width / 2 + 120, height * 0.75 - treble * 160, 26, treble * 160)

    # 给圆点加外圈，表现声音扩散感
    noStroke()
    fill(120 + volume * 100, 180 + volume * 50, 255, 60)
    circle(width / 2, y, r * 2.2)

    # 让圆点颜色跟随总音量变化
    noStroke()
    fill(120 + volume * 135, 180 + volume * 60, 255)
    circle(width / 2, y, r)
