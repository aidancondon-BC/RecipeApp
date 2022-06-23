import pandas as pd
import numpy as np
from ast import literal_eval

class Analyzer:

    df_all = pd.read_parquet('recipes.parquet', engine='fastparquet')
    df_ingredients = pd.read_parquet('ingredients.parquet', engine='fastparquet')

    def searchForIngredient(self, word):
        word = word.lower()
        lw = len(word)
        rev_word = word[::-1]
        word_as_set = set(word)
        searches = []
        for ingredient in self.df_i.Ingredients.values:
            smaller = min([lw, len(ingredient)])
            sim = 1 - (len((word_as_set - set(ingredient.lower()))) / lw)
            rev_i = ingredient[::-1]
            for idx in range(smaller):
                if word[idx] == ingredient[idx]: sim += 0.1
                if rev_word[idx] == rev_i[idx]: sim += 0.1
            searches.append((ingredient, sim))
        searches = sorted(searches, key=lambda pair: pair[1], reverse=True)
        searches = [x[0] for x in searches]
        return searches[:10] if len(searches) >= 10 else searches
