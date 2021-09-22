# 同花顺算法挑战平台-提交代码模板



## 一、参考项目结构

```
[项目名]
├── [包名]                  
│   ├── setting.conf
│   ├── metrics
│   │   ├── eval.py
│   │   ├── __init__.py
│   │   └── run.sh
│   ├── predict
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   └── run.sh
│   ├── train
│   │   ├── __init__.py
│   │   ├── run.sh
│   │   └── train.py
│   └── util
│       ├── __init__.py
│       ├── interface.py
├── Dockerfile
├── docs
├── env.sh
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── tests
│   └── test_unittest.py
└── tox.ini
```

注：项目名和包名一致，名字自取，同[poetry new](https://python-poetry.org/docs/cli/#new)，整个项目符合[PEP-517](https://www.python.org/dev/peps/pep-0517/)标准

```
eg1:
	项目名：mycode
	包名：mycode
eg2：遇到项目名中带横杆的，包名转为下划线
	项目名：my-code
	包名：my_code
```



## 二、如何开发

1. `train/predict/metrics`分别代表训练、预测、计算评测指标三个功能，每个目录都自带一个启动脚本

   **为防止实现计算评测的公式有差异，请统一使用对应赛题提供的demo中的代码**

2. `setting.conf`里面的变量必须使用，对应的值可以自己调整，其他参数在`run.sh`里面自定义

   ```  
   TRAIN_FILE_DIR          读取训练文件的目录，注意是目录，作为train输入
   SAVE_MODEL_DIR          保存模型文件的目录，注意是目录，作为train的输出，predict的输入
   PREDICT_FILE_DIR        读取预测文件的目录，注意是目录，作为predict输入
   PREDICT_RESULT_FILE_DIR 保存预测结果的目录，注意是目录，作为predict输出
   GROUNDTRUTH_FILE_DIR    真实答案的存放目录，注意是目录，作为metrics输入
   RESULT_JSON_FILE        计算评测指标结果的文件，注意是文件，作为metrics输出，json格式，如`{"f1": 0.99}`
   RESULT_DETAIL_FILE      【可选】评测结果对比明细，注意是文件，作为metrics输出
   ```

3. Dockerfile的填写

   1）Dockerfile主要用于B榜自动化评测中指定基础环境，现提供以下版本

   | 镜像名    | 镜像说明                                     | 镜像地址                            |
   | ------ | ---------------------------------------- | ------------------------------- |
   | GPU镜像1 | cuda9.0、python3.6、ubuntu16.04，适用于运行tensorflow1.13以下版本（不包含） | 10jqkaaicubes/cuda:9.0-py3.6.5  |
   | GPU镜像2 | cuda10.0、python3.7、ubuntu18.04，适用于运行tensorflow1.13到tensorflow2.0的版本 | 10jqkaaicubes/cuda:10.0-py3.7.9 |
   | GPU镜像3 | cuda10.1、python3.7、ubuntu18.04，适用于运行tensorflow2.1到tensorflow2.3的版本 | 10jqkaaicubes/cuda:10.1-py3.7.9 |
   | GPU镜像4 | cuda11.0、python3.8、ubuntu18.04，适用于运行tensorflow2.3以上版本（不包含） | 10jqkaaicubes/cuda:11.0-py3.8.5 |

   *参考资料：https://www.tensorflow.org/install/source#gpu*

   ​

   2）dockerfile模板，修改中括号中的内容

   ```
   FROM [镜像地址]

   COPY ./ /home/jovyan/[项目名]

   RUN cd /home/jovyan/[项目名]  && \
       python -m pip install -r requirements.txt 
   ```

4. 请确保所有命令按以下顺序可以执行

   1）安装，在requirements.txt中添加需要安装的python包以及指定版本

   ```
   cd [项目名] 
   python -m pip install -r requirements.txt
   ```
   ​2）训练

   ```
   cd [项目名]
   bash [包名]/train/run.sh
   ```
   ​3）预测

   ```
   cd [项目名]
   bash [包名]/predict/run.sh
   ```
   ​4）计算评测指标

   ```
   cd [项目名]
   bash [包名]/metrics/run.sh
   ```

5. 功能实现完成后，请确保代码规范

  ```
  # 事先安装black/flake8
  black .   # 自动调整代码
  flake8 .  # 需根据提示修改代码
  ```

6. 更新你的README




## 三、注意事项

- 所有文件路径均通过传参的方式获取，使用相对路径，否则B榜自动评测不能正常运行

- 如果需要安装一些非python包，请将包名以及安装过程放在readme中说明

- 不要指定GPU的卡号

- 代码上传格式要求：xxx.zip。结构如下：

  ```
  xxx.zip
  |---- [项目名]      # 代码目录，所有数据都不要放在代码目录下
  |---- model/	   # 训练的模型
  |---- data/        # 其他依赖的数据文件
  ```

- 上传大小要求：zip包不超过600M


- B榜自动化评测环境

  CPU4核、内存12G、显存11G，cuda版本支持9.0、10.0、10.1、11.0。