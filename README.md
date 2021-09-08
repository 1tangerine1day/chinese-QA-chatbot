# bert2bert_QA_chatbot
a simple chinese QA chatbot implement with pytorch and transformers
簡易 ptt gossiping QA chatbot 使用 pytorch framework 和 transformers

tutorial: https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/QA_chatbot_step_by_step.ipynb
demo for using: https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/How_to_use.ipynb

data: https://github.com/zake7749/Gossiping-Chinese-Corpus

my trained weight (best.pt): https://drive.google.com/file/d/1qc5uq5_Uag1XROoxbpruWZGzR3bhTyT-/view?usp=sharing

![](https://github.com/1tangerine1day/bert2bert_QA_chatbot/blob/master/loss.png)

## load model

```
from bert2bert import QA_chatbot

cahtbot = QA_chatbot()
cahtbot.load_model("best.pt")
```

## predict

input
```
cahtbot.predict("加權指數狂跌小台卻狂拉")
```
output

```
'台灣人的健康就是這樣'
```

input
```
cahtbot.predict("校園霸凌嚴重 立委兒子生殖器被踹到流血")
```
output

```
'，這種人真的很可憐，不要出來丟人現眼'
```


input
```
cahtbot.predict("cosplay機師有什麼搞頭嗎？")
```
output

```
'我想看看'
```


input
```
cahtbot.predict("工程師月薪多少")
```
output

```
'，台灣的公司薪水不是一般人的一般人的薪'
```
