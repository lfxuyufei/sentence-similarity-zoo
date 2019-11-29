#!/usr/bin/env python
# encoding: utf-8
"""
File Description: 数据预处理
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2019-11-29 18:02
"""
import random


def build_data_set(data, data_dir):
    """
    构建数据集，并写入文件
    :param data: 全量数据，格式为[(text_a,text_b,label)]
    :param data_dir: 写入文件的文件夹
    :return:
    """
    random.shuffle(data)
    # 按照0.8/0.1/0.1 划分数据集
    all_data_len = len(data)
    train_data = data[:int(0.8 * all_data_len)]
    dev_data = data[int(0.8 * all_data_len): int(0.9 * all_data_len)]
    test_data = data[int(0.9 * all_data_len):]

    def _write_into_file(data_to_write, file_path):
        data_to_write = [f'{each[0]}\t{each[1]}\t{each[2]}' for each in data_to_write]
        with open(file_path, 'wt', encoding='utf-8') as f:
            f.write("\n".join(data_to_write))

    _write_into_file(train_data, data_dir + '/train.tsv')
    _write_into_file(dev_data, data_dir + '/dev.tsv')
    _write_into_file(test_data, data_dir + '/test.tsv')
    print(f'数据总量: {len(data)} 训练集: {len(train_data)}, 开发集: {len(dev_data)}, 测试集: {len(test_data)}')
    print(f'文件已经写入 {data_dir}')


def process_atec_data():
    def read_raw_data(file_path):
        """
        读取原数据
        :param file_path: 文件地址
        :return: [(text_a,text_b,label)]
        """
        with open(file_path, 'rt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        # 提取text_a,text_b,label三元组
        data = []
        for line in lines:
            uid, text_a, text_b, label = line.split('\t')
            data.append((text_a, text_b, label))
        return data

    data = read_raw_data('./ATEC/raw/atec_nlp_sim_train2.csv') + read_raw_data('./ATEC/raw/atec_nlp_sim_train_add.csv')
    build_data_set(data, './ATEC/processed')


def process_ccks_data():
    def read_raw_data(file_path):
        """
        读取原数据
        :param file_path: 文件地址
        :return: [(text_a,text_b,label)]
        """
        with open(file_path, 'rt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        # 提取text_a,text_b,label三元组
        data = []
        for line in lines:
            text_a, text_b, label = line.split('\t')
            data.append((text_a, text_b, label))
        return data

    data = read_raw_data('./CCKS/raw/task3_train.txt')
    build_data_set(data, './CCKS/processed')


if __name__ == '__main__':
    process_atec_data()
    process_ccks_data()
