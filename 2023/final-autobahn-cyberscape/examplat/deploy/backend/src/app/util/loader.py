from yaml.constructor import FullConstructor
from yaml import FullLoader, SafeLoader

class CustomFullConstructor(FullConstructor):
    def ignore_unknown(self, node):
        return None 

    def custom_construct_object(self, suffix, node):
        if suffix == "Question":
            suffix = "app.models.question.Question"
        
        return self.construct_python_object_new(suffix, node)

SafeLoader.add_constructor(None, CustomFullConstructor.ignore_unknown)
FullLoader.add_constructor(None, CustomFullConstructor.ignore_unknown)
FullLoader.add_multi_constructor('tag:yaml.org,2002:python/object:', CustomFullConstructor.custom_construct_object)