import requests
# Base URL: https://sv443.net/jokeapi/category/{CATEGORY}
# Categories: Programming, Miscellaneous, Dark, Any


class Jokes:
    def __init__(self, category):
        self.allowed = [
                'Programming',
                'Miscellaneous',
                'Dark',
                'Any'
                ]
        if category.capitalize() in self.allowed:
            self.category = category.capitalize()
        else:
            raise AttributeError('Category is not in allowed categories')
    
    def get_joke(self):
        req = requests.get(f"https://sv443.net/jokeapi/category/{self.category}?").json()
        joke = None
        if req['type'] == 'twopart':
            joke = f"{req['setup']} {req['delivery']}"
        elif req['type'] == 'single':
            joke = req['joke']
        return joke
