#!/usr/bin/env python
# encoding:utf-8
# -------------------------------------------#
# Filename:
#
# Description:
# Version:       1.0
# Company:       www.10jqka.com.cn
#
# -------------------------------------------#
from pathlib import Path
from project_demo.util.interface import PredictInterface


class PredictImpl(PredictInterface):
    def initialize(self, input_file_dir: Path, load_model_dir: Path, predict_file_dir: Path, *args, **kargs):
        """预测初始化函数
        1.指定的三个参数必须使用，其他参数自定义
        Args:
            input_file_dir (Path): input, 预测的文件目录
            load_model_dir (Path): input, 加载模型的目录
            predict_file_dir (Path): output, 预测结果的文件目录
        """
        self.input_file_dir = input_file_dir
        self.load_model_dir = load_model_dir
        self.predict_file_dir = predict_file_dir
        print("Predict init!!")
        # ==================================
        # write your code
        # ==================================

    def do_predict(self):
        """
        预测主函数
        """
        print("Predict begin!!")
        # ==================================
        # write your code
        # ==================================


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file_dir")
    parser.add_argument("--load_model_dir")
    parser.add_argument("--predict_file_dir")
    args = parser.parse_args()
    predict_object = PredictImpl(args.input_file_dir, args.load_model_dir, args.predict_file_dir)
    predict_object.do_predict()
