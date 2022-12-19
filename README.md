## yolov4-predict

1. 运行前需要安装 `Pytorch (>= 1.7.0)` 以及 `ffmpeg`，并且安装 `requirements.txt` 中的依赖包。

2. 将 yolo 训练权重文件以及标签文件放入 `model_data` 文件夹下，并调整 `yolo.py` 中的 `model_path` 和 `classes_path`。

3. 在 `config.txt` 里进行参数设置，配置字段说明如下：

| 参数         | 描述         | 举例         |  
| ----------- | ----------- | ----------- |
| source      | 视频源地址       | /img/test.mp4       |
| output-dir   | 输出文件夹路径        | /output       |
| video-fps   | 视频输出的 FPS        | 25       |
| rtsp-url   | rtsp 推流地址（可选） | rtsp://127.0.0.1:8554/video  |

4. 运行 `predict.py`。

5. 结果保存在设置的 `output-dir` 下，`output-dir` 目录结构如下：

```
output-dir
├─frame
│  ├─pred   # 保存带预测框的帧
│  └─raw    # 保存原帧
├─json      # 保存帧对应的 json 结果
└─result    # 保存最终的推理结果视频
```

如果设置了 `rtsp-url`，推理结果视频流会推送至该地址中，`result` 文件夹下不会保存最终的推理结果视频。
