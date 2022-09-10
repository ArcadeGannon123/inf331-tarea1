import logging

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Stack:
    def __init__(self):
        self.__data = []
            
    def push(self, data):
        self.__data.append(data)
    
    def pop(self):
        return self.__data.pop()
    
    def stack_size(self):
        return len(self.__data)
    
    def longest(self):        
        return max(self.__data, key=len)            
        
    def shortest(self):
        return min(self.__data, key=len)
    
    def get_text(self,index):
        return self.__data[index]                  

def int_input(_min,_max,_message):
    while True:
        _input=0
        try:
            _input = input("Input: ")  
            _input = int(_input)
            if _input > _max or _input < _min:
                print("out of range!")                
                logging.info('input {}, {}'.format(_input,"out of range!"))
            else:
                break
        except ValueError:
            print(_message)
            logging.info('input {}, {}'.format(_input,_message))
        except KeyboardInterrupt:
            _input = 0
            print("KeyboardInterruption!")
            logging.info('input {}, {}'.format("ctrl+c","KeyboardInterruption!"))
            break
    return _input

def str_input():
    while True:
        try:
            _input = input("Input: ")
            break
        except KeyboardInterrupt:
            _input = 0
            print("KeyboardInterruption!")
            logging.info('input {}, {}'.format("ctrl+c","KeyboardInterruption!"))
            break
    return _input

def Main():
    print("")
    print("------Tarea 1 - Test program------")
    stack = Stack()
    logging.info('---program startup---')
    while True:
        logging.info('screen: Choose an option')
        print("")
        print("---Choose an option:---")
        print("1.- save a text")
        print("2.- get text from stack")
        print("3.- get the longest text")
        print("4.- get the shortest text")
        print("5.- compare size of two texts")
        print("0.- exit")
        
        _input = int_input(0,5,"That's not a valid option!")
        _stack_size = stack.stack_size()     
        print("")                   

        if _input == 1:
            logging.info('input 1, screen: save a text')
            print("---enter text to save---")
            _input = str_input()
            if type(_input) == str and _input != "":
                stack.push(_input)
                logging.info('input {}, {}'.format(_input,"pushed to stack!"))
            elif _input == "":
                print("null value ignored!")
                logging.info('input {}, {}'.format(_input,"null value ignored!"))
            else:
                break
            
        elif _input == 2:
            if _stack_size != 0:
                logging.info('input 2, screen: get text from stack')
                print("---stack size: {0}--------".format(_stack_size))
                print("---enter stack position---")
                print("")
                _input = int_input(1,_stack_size,"invalid position!")
                if _input > 0:
                    print("text in position {0}: ".format( _input ))
                    print("")
                    print( stack.get_text(_input-1) )
                    logging.info('input {}, {}'.format(_input,stack.get_text(_input-1)))
            else:
                logging.info('input 2, screen: get text from stack, message: the stack is empty! return to main screen')
                print("the stack is empty!")
            print("")

        elif _input == 3:
            
            if _stack_size != 0:
                logging.info('input 3, screen: get the longest text, message: {}'.format(stack.longest()))
                print("---the longest text in the stack---")
                print( stack.longest() )                
            else:
                logging.info('input 3, screen: get the longest text, message: the stack is empty! return to main screen')
                print("the stack is empty!")
            print("")

        elif _input == 4:
            
            if _stack_size != 0:
                logging.info('input 4, screen: get the shortest text, message: {}'.format(stack.shortest()))
                print("---the shortest text in the stack---")
                print( stack.shortest() )
            else:
                logging.info('input 4, screen: get the shortest text, message: the stack is empty! return to main screen')
                print("the stack is empty!")                
            print("")

        elif _input == 5:

            if _stack_size != 0:
                logging.info('input 5, screen: compare size of two texts')
                _input1=0
                _input2=0

                print("---stack size: {0}---------------------".format(_stack_size))
                print("---insert the position of both texts---")
                
                logging.info('waiting for input 1!')
                print("enter position of the first text: ")
                _input1 = int_input(1,_stack_size,"invalid position!")

                if _input1 >0:                    
                    logging.info('waiting for input 2!')
                    print("enter position of the second text: ")
                    _input2 = int_input(1,_stack_size,"invalid position!")
                
                if _input2 >0:                    
                    _text1 = stack.get_text(_input1-1)
                    _text2 = stack.get_text(_input2-1)
                    print(_input1)
                    print("")
                    print("text in position {0}: ".format( _input1))
                    print("")
                    print(_text1)
                    print("length: {0}".format(len(_text1)))
                    print("")
                    print("text in position {0}: ".format( _input2))
                    print("")
                    print(_text2)
                    print("length: {0}".format(len(_text2)))
                    print("")
                    
                    if len(_text1) > len(_text2):
                        
                        print("---the text in position {0} is the longest---".format(_input1))
                        logging.info('input1 {}, input2 {}, ---the text in position {} is the longest---'.format(_input1,_input2,_input1))
                        
                    elif len(_text1) < len(_text2):
                    
                        print("---the text in position {0} is the longest---".format(_input2)) 
                        logging.info('input1 {}, input2 {}, ---the text in position {} is the longest---'.format(_input1,_input2,_input2))
                        
                    else:
                        logging.info('input1 {}, input2 {}, ---both are the same size---'.format(_input1,_input2))
                        print("---both are the same size---")    
            else:
                logging.info('input 5, screen: compare size of two texts, message: the stack is empty! return to main screen')
                print("the stack is empty!")   
            print("")

        else:
            logging.info('input 0')
            break
    
    logging.info('------END------')
    print("------END------")
    print("")        
        
Main()