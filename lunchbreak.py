import Person from person
import Student from student
import Mentor from mentor
import random

class lunchbreak():
    def __init__(self, happiness_level, energy_level, knowledge_level, softskill_level):
        self.happiness_level = happiness_level
        self.energy_level = energy_level
        self.knowledge_level = knowledge_level
        self.softskill_level = softskill_level
    
    
    
    def story_line_changer():
        i = []
        i = randrange(0, 3)

        if i == 0:
            print('I am very hungry, I will eat alone!')
            happiness_level_amount()
            energy_level_amount()
        elif i == 1:
            print('I am very hungry, but I will eat with one Mentor!')
            happiness_level_amount()
            energy_level_amount()
            knowledge_level_amount()
        else:
            print('I am very hungry, but I will eat with other students!')
            happiness_level_amount()
            energy_level_amount()
            knowledge_level_amount()
            print('I saw, the Mentor went to learn about Softskill')
            softskill_level_amount()

            



    def happiness_level_amount(self):
        if self.happiness_level < 50:
            self.happiness_level += randrange(10, 51, 10)
            print('That was good, happiness level rich {} value', format(happiness_level))
        elif self.happiness_level > 50 and self.happiness_level < 100:
            self.happiness_level += randrange(10, 31, 10)
            print('This is a good day, happiness level rich {} value', format(happiness_level))
        else:
            print('This day couldn not be better! Happiness level rich the maximum, 100 value')
    
    def energy_level_amount(self):
        if self.energy_level < 50:
            self.energy_level -= randrange(10, 41, 10):
            print('I feel, that I am f*****g tired, energy level is {} value', format(energy_level)
        elif self.energy_level > 50 and self.energy_level < 100:
            self.energy_level -= randrange(30, 61, 10)
            print('I am tired a lit, energy level rich {} value', format(energy_level))
        if self.energy_level == 0
            print('I could not move! energy level rich the minimum, 0 value')
            break
        
    def knowledge_level_amount(self):
        if self.knowledge_level < 50:
            self.knowledge_level += randrange(30, 61, 10)
            print('Thanks guys,I learned a lot from you, knowledg level is {} value', format(knowledge_level)
        elif self.knowledge_level > 50 and self.knowledge_level < 100:
            self.energy_level += randrange(0, 31, 10)
            print('Thanks for the new ideas, I will Try it! knowledge level rich {} value', format(knowledge_level))
        if self.energy_level == 100
            print('F**K Guys...I leave! knowledge level rich the maximum, 100 value')
            break

    def softskill_level_amount(self):
        if self.softskill_level < 50:
            self.softskill_level += randrange(30, 61, 10)
            print('Hmm...I learned a lot at today, softskill_level level is {} value', format(softskill_level)
        elif self.softskill_level > 50 and self.softskill_level < 100:
            self.softskill_level += randrange(0, 31, 10)
            print('I need a lit, than I will be perfect, softskill level rich {} value', format(softskill_level))
        if self.softskill_level == 100
            print('I am The Best!!!... softskill level rich the maximum, 100 value')
            
            
        
        
        