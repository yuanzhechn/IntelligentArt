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

    # 给三个柱子加一条统一底线
    stroke(100, 180, 220, 120)
    strokeWeight(2)
    line(width / 2 - 145, height * 0.75, width / 2 + 145, height * 0.75)

    # 画三个简单柱子，分别表示低频、中频、高频
    noStroke()
    fill(60, 140, 255)
    rect(width / 2 - 165, height * 0.75 - bass * 100 * bassWave1, 22, bass * 100 * bassWave1)
    rect(width / 2 - 135, height * 0.75 - bass * 140 * bassWave2, 22, bass * 140 * bassWave2)
    rect(width / 2 - 105, height * 0.75 - bass * 170 * bassWave3, 22, bass * 170 * bassWave3)
    fill(80, 230, 220)
    rect(width / 2 - 45, height * 0.75 - mid * 100 * midWave1, 22, mid * 100 * midWave1)
    rect(width / 2 - 15, height * 0.75 - mid * 140 * midWave2, 22, mid * 140 * midWave2)
    rect(width / 2 + 15, height * 0.75 - mid * 170 * midWave3, 22, mid * 170 * midWave3)
    fill(255, 90, 210)
    rect(width / 2 + 75, height * 0.75 - treble * 100 * trebleWave1, 22, treble * 100 * trebleWave1)
    rect(width / 2 + 105, height * 0.75 - treble * 140 * trebleWave2, 22, treble * 140 * trebleWave2)
    rect(width / 2 + 135, height * 0.75 - treble * 170 * trebleWave3, 22, treble * 170 * trebleWave3)

    # 给圆点加外圈，表现声音扩散感
    noStroke()
    fill(120 + volume * 100, 180 + volume * 50, 255, 60)
    circle(width / 2, y, r * 2.2)

    # 让圆点颜色跟随总音量变化
    noStroke()
    fill(120 + volume * 135, 180 + volume * 60, 255)
    circle(width / 2, y, r)
