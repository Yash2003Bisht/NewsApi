from googletrans import Translator

def translateText(*text):
    """function to convert language"""
    translator = Translator()
    out = translator.translate(*text, dest='french')
    return out
