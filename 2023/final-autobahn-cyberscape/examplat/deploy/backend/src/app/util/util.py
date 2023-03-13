import re

def remove_duplicate(data=None):
    if not data:
        return []
    
    return list(set(data))

def validate_yaml(content):
    # Validate yaml content
    pattern = re.compile("(import|__.*?__|system|subprocess|Popen|popen|getstatusoutput|chr\(\d+\)|globals|locals|getattr|(:-1])|(\\*?(\'|\")\s*?\+\s*?\\*?(\'|\"))|[\w\s]+\\*?(\'|\")\s*?\\*?(\'|\")[\w\s]+)", re.DOTALL | re.IGNORECASE)
    result = re.search(pattern, content)
    if result:
        return False
    
    return True