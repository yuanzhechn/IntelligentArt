# IntelligentArt

基于 Processing Python Mode 的音乐可视化作品。

## 运行方法

1. 安装 Processing 3.5.4。
2. 在 Processing 的贡献管理器中安装 Python Mode。
3. 用 Processing 打开 `main/main.pyde`。
4. 确认编辑器右上角显示 `Python`，然后点击运行。

音乐和分析数据已经包含在 `main/data/` 中。程序使用 Java 自带音频接口，不需要安装 Sound 或 Minim 库。

## 目录结构

```text
main/
├── main.pyde
├── sketch.properties
└── data/
    ├── music.wav
    └── music_features.csv
```

如果没有声音，请先查看 Processing 控制台。成功加载时会显示 `music.wav 已开始播放`；加载失败时会显示具体原因。
