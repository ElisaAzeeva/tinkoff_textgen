#library
import sys
import json
import argparse
parser = argparse.ArgumentParser(description='Generation')
parser.add_argument('model',type=str,help='File with model')
parser.add_argument('seed',type=str,help='Initial state')
parser.add_argument('length',type=str,help='Length of generated sequence')
args = parser.parse_args()

class Generation:
    def __init__(self,model,seed,length):
        self._model= model
        self._seed=seed
        self._length=length
    def open_model(self):
        with open(self._model) as json_file:
            return json.load(json_file)
    def generate(self):
        current_model = self.open_model()
        sequence = self._seed
        import random
        if self._seed in current_model:
            word=random.choice(list(current_model[self._seed].keys()))
            #print(current_model[self._seed].keys())
            sequence=sequence+ " "+ word
            i=1
            while i < int(self._length)-1:
                if word in current_model:
                    word=random.choice(list(current_model[word].keys()))
                    sequence=sequence+ " "+ word
                    i+=1
                else:
                   sys.exit("Sequence is "+sequence +" and it is shorter than "+self._length)             
        else:
            sys.exit("Seed not found in model")
        return sequence

#Program
sequence= Generation(args.model,args.seed,args.length)
print(sequence.generate())
