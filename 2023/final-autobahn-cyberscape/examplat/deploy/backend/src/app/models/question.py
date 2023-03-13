from string import ascii_lowercase as letter
import random

class Question:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.question = kwargs.get('question')

        choices = kwargs.get('choices')
        random.shuffle(choices)
        instance.choices = {choices[i]: letter[i] for i in range(len(choices))}
        
        instance.answer = instance.choices.get(kwargs.get('answer'))

        return instance

    def get_question_and_choices(self):
        return {
            "question": self.question,
            "choices": { v:k for k,v in self.choices.items() }
        }
        
    def get_answer(self):
        return self.answer