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
from project_demo.util.interface import TrainInterface


class TrainImpl(TrainInterface):
    """
    模型训练
    """

    def initialize(self, input_file_dir: Path, save_model_dir: Path, *args, **kargs):
        """训练初始化函数
        1.指定的两个参数必须使用，其他参数自定义
        Args:
            input_file_dir (Path): input, 训练文件的目录
            save_model_dir (Path): output, 保存模型的目录
        """
        self.input_file_dir = input_file_dir
        self.save_model_dir = save_model_dir
        print("Train init!!")
        # ==================================
        # write your code
        # ==================================

    def do_train(self):
        """
        训练主函数
        """
        print("Train begin!!")
        # ==================================
        # write your code
        # ==================================


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file_dir")
    parser.add_argument("--save_model_dir")
    args = parser.parse_args()
    train_object = TrainImpl(args.input_file_dir, args.save_model_dir)
    train_object.do_train()
