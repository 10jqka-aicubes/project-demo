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
from project_demo.util.interface import MetricsInterface


class EvalImpl(MetricsInterface):
    def do_eval(
        self,
        predict_file_dir: Path,
        groundtruth_file_dir: Path,
        result_json_file: Path,
        result_detail_file: Path,
        *args,
        **kargs
    ):
        """评测主函数

        Args:
            predict_file_dir (Path): input, 模型预测结果的文件目录
            groundtruth_file_dir (Path): input, 真实结果的文件目录
            result_json_file (Path): output, 评测结果，json格式，{"f1": 0.99}
            result_detail_file (Path): output, 预测明细，可选
        """
        print("Eval begin!!")
        # ==================================
        # write your code
        # ==================================


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--predict_file_dir")
    parser.add_argument("--groundtruth_file_dir")
    parser.add_argument("--result_json_file")
    parser.add_argument("--result_detail_file")
    args = parser.parse_args()
    eval_object = EvalImpl()
    eval_object.do_eval(
        args.predict_file_dir, args.groundtruth_file_dir, args.result_json_file, args.result_detail_file
    )
