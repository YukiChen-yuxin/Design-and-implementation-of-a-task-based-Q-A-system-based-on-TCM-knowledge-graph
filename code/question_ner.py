
# coding: utf-8

import tensorflow as tf
import tensorflow_addons as tfa

from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras import backend as K

from tensorflow.keras.preprocessing import sequence
import numpy as np
import json
import warnings
warnings.filterwarnings("ignore")


class question_ner:
    # 参数
    def __init__(self):
        # 导入处理好的标签数据集
        with open('data/idx2vocab.json',encoding="utf-8") as file_obj:
            self.idx2vocab=json.load(file_obj) 
        with open('data/vocab2idx.json',encoding="utf-8") as file_obj:
            self.vocab2idx=json.load(file_obj)
        with open('data/idx2label.json',encoding="utf-8") as file_obj:
            self.idx2label=json.load(file_obj)
        with open('data/label2idx.json',encoding="utf-8") as file_obj:
            self.label2idx=json.load(file_obj)

        # 导入训练好的模型
        self.model = models.load_model("model/output/bilstm_crf_ner", compile=False)

        #提取转移矩阵参数
        self.trans_params = self.model.get_layer('crf').get_weights()[0]
        # 获得BiLSTM的输出logits
        self.sub_model = models.Model(inputs=self.model.get_layer('input_ids').input,
                        outputs=self.model.get_layer('dense').output)

    def predict(self,inputs, input_lens):
        logits = self.sub_model.predict(inputs)
        # 获取CRF层的转移矩阵
        # crf_decode：viterbi解码获得结果
        pred_seq, viterbi_score = tfa.text.crf_decode(logits, self.trans_params, input_lens)
        return pred_seq

    def pre_data(self,sentence):
        maxlen=100
        sent_chars = list(sentence)
        sent2id = [self.vocab2idx[word] if word in self.vocab2idx else self.vocab2idx['UNK'] for word in sent_chars]
        sent2id_new = np.array([[0] * (maxlen-len(sent2id)) + sent2id[:maxlen]])
        test_lens = np.array([100])

        pred_seq = self.predict(sent2id_new, test_lens)
        y_label = pred_seq.numpy().reshape(1, -1)[0]
        y_ner = [self.idx2label[str(i)] for i in y_label][-len(sent_chars):]
        return y_ner

if __name__=="__main__":
    
    ner = question_ner()
    text = "我发烧流鼻涕怎么办"
    result = ner.pre_data(text)
    print(result)