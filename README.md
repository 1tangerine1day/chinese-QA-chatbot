# bert2bert_QA_chatbot
a simple chinese QA chatbot implement with pytorch and transformers
簡易 ptt gossiping QA chatbot 使用 pytorch framework 和 transformers

tutorial: <br>
https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/QA_chatbot_step_by_step.ipynb <br>

demo for using: <br>
https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/How_to_use.ipynb <br>

model: <br>
![](https://www.researchgate.net/profile/Tarek-Naous/publication/349868790/figure/fig2/AS:998754173857792@1615132959673/Architecture-of-the-proposed-BERT2BERT-model-initialized-with-AraBERT-checkpoints-for.png)<br>
picture from [this](https://www.researchgate.net/figure/Architecture-of-the-proposed-BERT2BERT-model-initialized-with-AraBERT-checkpoints-for_fig2_349868790)<br>
instead of AraBERT, i use normal bert with pretrain model "bert-base-chinese"



data: <br>
https://github.com/zake7749/Gossiping-Chinese-Corpus <br>

my trained weight (best.pt): <br>
https://drive.google.com/file/d/1qc5uq5_Uag1XROoxbpruWZGzR3bhTyT-/view?usp=sharing <br>

trainin
* batch: 50
* learning rate: 1e-5
* optimizer: Adam
* epochs: 20 <br>
![](https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/loss.png)

## load model

```
from bert2bert import QA_chatbot

cahtbot = QA_chatbot()
cahtbot.load_model("best.pt")
```

## predict

test case 1
```
cahtbot.predict("加權指數狂跌小台卻狂拉")
```
```
'台灣人的健康就是這樣'
```

test case 2
```
cahtbot.predict("校園霸凌嚴重 立委兒子生殖器被踹到流血")
```
```
'，這種人真的很可憐，不要出來丟人現眼'
```

test case 3
```
cahtbot.predict("cosplay機師有什麼搞頭嗎？")
```
```
'我想看看'
```

test case 4
```
cahtbot.predict("工程師月薪多少")
```
```
'，台灣的公司薪水不是一般人的一般人的薪'
```
