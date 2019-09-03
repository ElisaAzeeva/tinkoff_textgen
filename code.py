#library
import argparse
parser = argparse.ArgumentParser(description='Training of generation')
parser.add_argument('input',type=str,help='Input file for training')
parser.add_argument('output',type=str,help='Model')
args = parser.parse_args()
# Class for model training.
class Training:
    def __init__(self,input_file_name,output_file_name):
        self._input= input_file_name
        self._output=output_file_name

    def get_sentences(self):
        words_separators = ['—',',',':',';','\t','_','—','\n']
        sentence_separators = ['.','!','?']
        with open (self._input) as file: 
            text=file.read().lower()
            for w,s in zip(words_separators,sentence_separators):
                text=text.replace(w,' ')
                text=text.replace(s,'.')
            sentence=text.split('.')
        return sentence

    def get_words_in_sentence(self,sentence):
        return sentence.split()

    def get_model(self):
        #model={}
        import json
        model=json.dumps({})
        self.sentences=self.get_sentences()
        for sentence in self.sentences:
            words= self.get_words_in_sentence(sentence)
            if len(words) !=0:
                itr_key=iter(words)
                itr_val=iter(words)
                i=0
                value=next(itr_val)
                while i<len(words)-1:
                    key= next(itr_key)
                    value=next(itr_val)
                    #if key in model.keys():
                    if key in model:
                        #model[key].append(value)
                        if value in model[key]:                            
                            model[key][value]+=1                          
                        else:
                            model[key].update({value:1}) 
                    elif isinstance(model,str):
                        #model[key]=[value]
                        model={key:{value:1}}
                    else:
                        model.update({key:{value:1}})    
                    i+=1
        js_model = json.dumps(model,indent=4,sort_keys=False,ensure_ascii=False) 
        text_file = open(self._output,"w")
        text_file.write("%s" % js_model)
        text_file.close()

#Program
model= Training(args.input,args.output)
model.get_model()
