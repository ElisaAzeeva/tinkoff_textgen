#library
import argparse
parser = argparse.ArgumentParser(description='Generation')
parser.add_argument('model',type=str,help='File with model')
parser.add_argument('seed',type=str,help='Initial state')
parser.add_argument('length',type=str,help='Length of generated sequence')
args = parser.parse_args()

class Generation:
    def __init__(self,input_file_name,output_file_name):
        self._input= input_file_name
        self._output=output_file_name
        