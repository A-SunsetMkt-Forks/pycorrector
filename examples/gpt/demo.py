# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import sys

sys.path.append("../..")
from pycorrector.gpt.gpt_corrector import GptCorrector

if __name__ == '__main__':
    error_sentences = [
        '少先队员因该为老人让坐',
        '真麻烦你了。希望你们好好的跳无',
        '机七学习是人工智能领遇最能体现智能的一个分知',
        '一只小鱼船浮在平净的河面上',
        '我的家乡是有明的渔米之乡',
        '目击者称，以军已把封锁路障除去，不过备关卡检查站仍有坦克派驻，车辆已能来往通过，只是流量很漫。',
    ]
    m = GptCorrector("shibing624/chinese-text-correction-1.5b")

    batch_res = m.correct_batch(error_sentences, prefix_prompt="文本纠错：\n\n")
    for i in batch_res:
        print(i)
        print()

    batch_res = m.correct_batch(error_sentences,
                                system_prompt="你是一个中文文本纠错助手。请根据用户提供的原始文本，生成纠正后的文本。",
                                prompt_template_name="qwen",
                                prefix_prompt="")
    for i in batch_res:
        print(i)
        print()
