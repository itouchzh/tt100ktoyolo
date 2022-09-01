# TT100K数据集标签标签转化为YOLO格式。
使用训练集中6105张图片，测试集中3065张图片，共计9170张。
选择数据集类别为45类，和论文中相同。
项目参考：https://github.com/halftop/TT100K_YOLO_Label
## 步骤
- 首先运行json2xml.py 将json转化为.xml，结果为xmlLabel1

- 其次运行 `xml2txt.py`将xml转化为YOLO格式。结果为txtLabel1

- 运行total.py,进行信息统计。结果为YOLOtxt

