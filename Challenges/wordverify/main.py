#!/usr/bin/env python
""" A script for generating sub words from a given word """
from freedictionaryapi.clients.async_client import AsyncDictionaryApiClient
from freedictionaryapi.errors import DictionaryApiError
from freedictionaryapi.languages import LanguageCodes
from itertools import combinations
import asyncio
import json
import re

all_combination, all_words = {}, []


async def verify(word):
    """
    Function for taking in a word and accessing whether the word exists in the english dictionary

    Args:
        word[str] - This is the word for verification

    Return:
        Function does not have a value
    """
    async with AsyncDictionaryApiClient() as client:
        try:
            word = await client.fetch_word(word)
        except DictionaryApiError as e:
            error = str(e)
        else:
            all_words.append(word.word)
            all_meaning = {}
            for i in word.meanings:
                all_meaning[i.part_of_speech] = i.definitions[0].definition
            all_combination[f'{word.word}'] = all_meaning


def main():
    """Main function"""
    word = input("Enter the word: ")
    for j in range(2, len(word)):
        # generates word combinations with limit being two
        words = combinations(word, j)
        for i in words:
            # Verifies that the word combination is not made of consonants
            comp = "[^AEIOUaeiou]{" + str(len(i)) + "}"
            if not (x := re.findall(comp, "".join(i))):
                asyncio.run(verify("".join(i)))
    with open("ans.json", "w") as file:
        json.dump(json.dumps(all_combination), file, indent=4)


if __name__ == "__main__":
    main()
