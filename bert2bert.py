import torch
import transformers

class QA_chatbot(torch.nn.Module):
    
    def __init__(self):
        super(QA_chatbot, self).__init__()
        encoder = transformers.BertGenerationEncoder.from_pretrained(
            "bert-base-chinese", is_decoder=True, bos_token_id=101, eos_token_id=102)
        decoder = transformers.BertGenerationDecoder.from_pretrained(
            "bert-base-chinese", add_cross_attention=True, is_decoder=True, bos_token_id=101, eos_token_id=102)
        self.bert2bert = transformers.EncoderDecoderModel(encoder=encoder, decoder=decoder)
        
        self.tokenizer = transformers.BertTokenizer.from_pretrained("bert-base-chinese")
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, input_tensor, input_masks=None, target_tensor=None, target_masks=None):

        if target_tensor != None:
            loss = self.bert2bert(
                input_ids=input_tensor, 
                attention_mask=input_masks, 
                decoder_input_ids=target_tensor, 
                decoder_attention_mask=target_masks, 
                labels=target_tensor).loss

            return loss
    
        else:
            out = self.bert2bert.generate(input_ids=input_tensor, 
                                          decoder_start_token_id=self.bert2bert.config.decoder.pad_token_id)

            return out
        
     
    def tokenize(self, sentence):
        tokens = self.tokenizer.tokenize(sentence)
        ids = self.tokenizer.convert_tokens_to_ids(tokens)

        return ids


    def detokenize(self, ids):
        tokens = self.tokenizer.convert_ids_to_tokens(ids)
        sentence = self.tokenizer.convert_tokens_to_string(tokens)

        return sentence.replace('[PAD]', '').replace(' ', '')
    
    
    def predict(self, sentence):
        ids = self.tokenize(sentence)

        with torch.no_grad():
            input_tensor = torch.tensor([ids]).long()
            pred = self(input_tensor)

        return self.detokenize(pred.tolist()[0])
    
    def load_model(self, path):
        self.load_state_dict(torch.load(path))
        print("complete!")