from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window
from random import random, randint
from kivy.lang import Builder

Window.size = (330, 600)
Window.clearcolor = (.034,.123,.210,1)

class MainBoard(MDScreen):

   def Clear(self):
      before = self.ids.calc_text.text 
      self.ids.calc_text.text = ''
   
   def mathematic(self, value):
      before = self.ids.calc_text.text 
      if before[-1] == value:
         pass
      else:
         self.ids.calc_text.text = f'{before}{value}'

   
   def Special_sign(self, value):
      before = self.ids.calc_text.text 
      if before[-1] == value:
         self.ids.calc_text.text = f'-{before}'
      elif before[-1] == '-':
         self.ids.calc_text.text = f'{value}{before}'


   def Remove(self):
      before = self.ids.calc_text.text 

      if before == 'Error!!':
         self.ids.calc_text.text = ''
      else:
         self.ids.calc_text.text = before[:-1]
   
   def Add_num(self, value):
      before = self.ids.calc_text.text 
      self.ids.calc_text.text = f'{before}{value}'
   
       
   def calculate(self):
      before = self.ids.calc_text.text 
      try:
         self.ids.calc_text.text = str(eval(before))
      except Exception as e:
         print(f"{e} Error Occur!!")
         self.ids.calc_text.text = 'Error!!'
   
   def mathematic(self, value):
      before = self.ids.calc_text.text 
      if before[-1] == value:
         pass
      else:
         self.ids.calc_text.text = f'{before}{value}'

class CalculatorApp(MDApp):
   def build(self):
      self.title = 'Morden Calculator'.upper()
      self.theme_cls.primary_pallete = 'blue'
      self.theme_cls.theme_style = "Dark"

      return Builder.load_file('Calculator.kv') 
   
if __name__ == '__main__':
   CalculatorApp().run()