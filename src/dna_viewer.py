import kivy
kivy.require('2.0.0')

import sys
import TwoJump
from TwoJump import TwoJump

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserController
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

import re

Window.size = (1280, 800)

class DnaInput(TextInput):
    '''
    Used to ensure validity of input search pattern and
    pass to searching object
    '''
    valid_input = re.compile('[acgt]*')
    
    def insert_text(self, substring, from_undo=False):
        '''
        Ensures text conforms to constraints

        Args:
            substring: user input pattern
            from_undo: boolean for API
        '''
        substring = substring.lower()
        match = re.fullmatch(self.valid_input, substring)

        if(match != None):
            super(DnaInput, self).insert_text(substring, from_undo=from_undo)

class PatternSearchWidget(BoxLayout):
    '''
    Main hook showing dataset and matching patterns upon
    function call
    '''
    input_pattern = ObjectProperty(None)
    input_data = ''
    data_text = StringProperty(input_data)

    number_of_matches     = StringProperty('')
    number_of_comparisons = StringProperty('')
    matched_indices       = StringProperty('')
    
    def set_input_data(self, input_data):
        '''
        Sets input data and resets computed data

        Args:
            input_data: user search input in the form of a string
            that gets validated by insert_text()
        '''
        self.input_data = input_data
        self.data_text = input_data
        self.number_of_matches = ''
        self.number_of_comparisons = ''
        self.matched_indices = ''

    def search_string(self):
        '''
        Initializes the 2-jump algorithm and starts a pattern
        search based off the current input data
        '''
        two_jump = TwoJump(self.input_data)
        results = two_jump.match_pattern(self.input_pattern.text)
        
        # sets output for user to see
        self.number_of_matches = str(results[0])
        self.number_of_comparisons = str(results[1])
        self.matched_indices = str(results[2])

        temp_string = ''
        pattern_indices = []
        for i in results[2]:
            for j in range(i, i+len(self.input_pattern.text)):
                pattern_indices.append(j)

        # Assigns green colour to string data that matches indices
        for i in range(0, len(self.input_data)):
            if i in pattern_indices:
                 temp_string += '[color=27FF00]' + self.input_data[i] + '[/color]'
            else:
                temp_string += self.input_data[i]
                continue
            
        self.data_text = temp_string

Builder.load_file('PatternSearchWidget.kv')

class SequenceMinerWidget:
    

def init_input(filename):
    '''
    Parses file input to ensure that source data is correct

    Args:
        filename: name of input file ending with .txt

    Returns:
        output: parsed input file in the form of a string

        for example, "ACTGGTGACTGTAAG"
    '''
    input_data = []
    for i in range(2):
        try:
            reader = open(filename)
            for line in reader:
                line_arr = line.split(' ')
                for index, substring in enumerate(line_arr):
                    if index == 0:
                        continue
                    char_arr = list(substring)
                    if char_arr[len(char_arr) - 1] == '\n':
                        char_arr.pop()
                    input_data += char_arr
            print('File parsed correctly...')
            break
        except FileNotFoundError:
            print('File not found, please verify the path and try again')
            if i == 0:
                if '\\' in filename:
                    filename = '../data/' + filename[filename.index('\\') + 1:len(filename) - 1]
                else:
                    filename = '../data/' + filename
                continue
            sys.exit()
        except IndexError:
            print('Problem parsing the input file, check guidelines to ensure proper form')
            sys.exit()

    expression = re.compile('[acgt]*')
    output = ''
    for i in input_data:
        if(re.fullmatch(expression, i) != None):
            output += i
    
    return output
     
class DnaViewer(App):
    '''
    Builder function for PatternSearchWidget. Links to
    .kv file when function is called
    '''
    def build(self):
        '''
        Override for API

        Returns:
            BoxLayout object as defined above for use in
            GUI construction by API
        '''
        pattern_search = PatternSearchWidget()

        input_data = ''

        if(len(sys.argv) > 1):
            input_data = init_input(sys.argv[1])

        pattern_search.set_input_data(input_data)

        return pattern_search