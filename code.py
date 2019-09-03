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
        model={}
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
                    if key in model.keys():
                        model[key].append(value)
                        #[model[key],value]
                    else:
                        model[key]=[value]
                    i+=1
        model_file = open(self._output,"w")
        model_file.write("%s" % model)
        model_file.close()

#Program
model= Training(args.input,args.output)
model.get_model()
