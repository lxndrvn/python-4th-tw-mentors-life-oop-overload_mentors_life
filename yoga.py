import random

class Yoga():
    def __init__(self, happiness_level, energy_level, knowledge_level, soft_skill_level):
        self.happiness_level = happiness_level
        self.energy_level = energy_level
        self.knowledge_level = knowledge_level
        self.soft_skill_level = soft_skill_level
    
    def story_line_changer(self):
        location = self.location()
        i = 0
        i = random.randrange(0, 3)
        if i == 0:
            print('I will do some exercise alone, {}'.format(location))
            self.happiness_level_amount()
            self.energy_level_amount()
        elif i == 1:
            print('I will do some exercise with one mentor, maybe I will learn something, {}'.format(location))
            self.happiness_level_amount()
            self.energy_level_amount()
            self.knowledge_level_amount()
      
    def happiness_level_amount(self):
        if self.happiness_level < 50:
            self.happiness_level += random.randrange(10, 51, 10)
            print('That was good, happiness level rich {} value'.format(self.happiness_level))
        elif self.happiness_level > 50 and self.happiness_level < 100:
            self.happiness_level += random.randrange(10, 31, 10)
            print('This is a good day, happiness level rich {} value'.format(self.happiness_level))
        else:
            print('This day could not be better! Happiness level rich the maximum, 100 value')
    
    def energy_level_amount(self):
        if self.energy_level < 50:
            self.energy_level -= random.randrange(10, 41, 10)
            print('I feel, that I am f*****g tired, energy level is {} value'.format(self.energy_level))          
        elif self.energy_level > 50 and self.energy_level < 100:
            self.energy_level -= random.randrange(30, 61, 10)
            print('I am tired a lit, energy level rich {} value'.format(self.energy_level))
            
        elif self.energy_level == 0:
            print('I could not move! energy level rich the minimum, 0 value')
        
    def knowledge_level_amount(self):
            if self.knowledge_level < 50:
                self.knowledge_level += random.randrange(30, 61, 10)
                print('Thanks guys,I learned a lot from you, knowledge level is {} value'.format(self.knowledge_level))
            elif (self.knowledge_level > 50 and self.knowledge_level < 100):
                self.knowledge_level += random.randrange(0, 31, 10)
                print('Thanks for the new ideas, I will Try it! knowledge level rich {} value'.format(self.knowledge_level))
            elif self.knowledge_level == 100:
                print('F**K Guys...I leave! knowledge level rich the maximum, 100 value')

    def soft_skill_level_amount(self):
        if self.soft_skill_level < 50:
            self.soft_skill_level += random.randrange(30, 61, 10)
            print('Hmm...I learned a lot at today, soft skill_level level is {} value'.format(self.soft_skill_level))
        
        elif self.soft_skill_level > 50 and self.soft_skill_level < 100:
            self.soft_skill_level += random.randrange(0, 31, 10)
            print('I need a lit, than I will be perfect, soft skill level rich {} value'.format(self.soft_skill_level))
            
        elif self.soft_skill_level == 100:
            print('I am The Best!!!... soft skill level rich the maximum, 100 value')
            
    
    def location(self):
        location = ('')
        i = random.randrange(0, 3)

        if i == 0:
            return 'in the classroom'
        elif i == 1:
            return 'in the meeting room'
        else: 
            return 'on a street' 