import argparse
import os
import re
import requests
from termcolor import colored


class TextFixer:
    """
    A class to correct and analyze text.

    ...

    Attributes
    ----------
    phrase : str
        The text phrase or file path to be corrected and analyzed
    responses : list
        A list of responses for misspelled words

    Methods
    -------
    load_text():
        Loads the text to be corrected and analyzed
    corrector():
        Corrects the loaded text
    spelling_info():
        Determines whether words in the text are misspelled
    show_stats():
        Shows statistics for the text
    process_text(correct=False, misspell=False, stats=False, output=False):
        Processes the text based on the selected options
    """

    def __init__(self, phrase):
        """
        Constructs all the necessary attributes for the TextFixer object.

        Parameters
        ----------
            phrase : str
                The text phrase or file path to be corrected and analyzed
        """
        self.phrase = phrase
        self.responses = []

    def load_text(self):
        """
        Loads the text to be corrected and analyzed.
        """
        if os.path.isfile(self.phrase):
            with open(self.phrase, "r") as f:
                self.txt = f.read().rstrip("\n")
        else:
            self.txt = self.phrase

    def corrector(self):
        """
        Corrects the loaded text.
        """
        txt_list = [letter for letter in self.txt]
        i = 0
        while i < len(txt_list) - 2:

            # Changing first letter to upper
            if txt_list[0].islower():
                txt_list[0] = txt_list[0].upper()

            # Removing multiply spaces
            if txt_list[i] == " ":
                k = i + 1
                while txt_list[k] == " ":
                    txt_list.pop(k)

            # Removing multiply dots
            if txt_list[i] == ".":
                k = i + 1
                while txt_list[k] == ".":
                    txt_list.pop(k)

            # Removing multiply commas
            if txt_list[i] == ",":
                k = i + 1
                while txt_list[k] == ",":
                    txt_list.pop(k)
                
                # Removing space before ,
                if txt_list[i-1] == " ":
                    txt_list.pop(i-1)

            # Adding space after !, ?, ., ,
            if txt_list[i] == "!" or txt_list[i] == "?" or txt_list[i] == "." or txt_list[i] == ",":
                if txt_list[i+1] != " ":
                    txt_list.insert(i+1, " ")

                # Upper first letter of the sentence
                if txt_list[i] != ",":
                    if txt_list[i + 2].islower():
                        txt_list[i + 2] = txt_list[i + 2].upper()

            i += 1
        self.txt = "".join(txt_list)

        k = 0
        while k < len(self.txt)-2:
        # Removing space after "(" symbol
            if txt_list[k] == "(" and txt_list[k+1] == " ":
                txt_list.pop(k+1)

            # Removing space after ")" symbol
            if txt_list[k] == ")" and txt_list[k-1] == " ":
                txt_list.pop(k-1)

            k += 1


        self.txt = "".join(txt_list)

        # Lower letter if in list with shorts
        short_forms = ["np.", "godz.", "tel.", "płn.", "ppoż.", "płd.", "cdn.", "jw.", "itd.", "itp."]
        word_sentences = self.txt.split()
        for index, word in enumerate(word_sentences):
            if word in short_forms:
                word_sentences[index+1] = word_sentences[index+1].lower()

        self.txt = " ".join(word_sentences)

    def spelling_info(self):
        """
        Determines whether words in the text are misspelled.
        """
        words = re.findall(r"\w+", self.txt)
        for word in words:
            url = "https://sjp.pl/" + word
            response = str(requests.get(url))
            if response == "<Response [404]>":
                self.responses.append(response)
                print(f'"{word}" is probably misspelled')
    
    def show_stats(self):
        """
        Shows statistics for given text.
        """
        self.word_count = len(re.findall(r"\w+", self.txt))
        self.sentence_count = len(re.findall(r"[.!?]+", self.txt))
        self.character_count = len(self.txt)
        self.space_count = len(re.findall(" ", self.txt))
        print(f"Word count: {self.word_count}")
        print(f"Sentence count: {self.sentence_count}")
        print(f"Character count: {self.character_count}")
        print(f"Space count: {self.space_count}")

    def process_text(self, correct=False, misspell=False, stats=False, output=False):
        """
        Process given arguments.
        """
        self.load_text()
        if correct:
            self.corrector()
        if misspell:
            print(colored("-----------------------------------------", "red"))
            print(colored("MISSPELLED: ", "red"))
            self.spelling_info()
            print(colored("-----------------------------------------", "red"))
        if stats:
            print(colored("-----------------------------------------", "cyan"))
            print(colored("STATISTICS: ", "cyan"))
            self.show_stats()
            print(colored("-----------------------------------------", "cyan"))
        if output:
            with open(output, "w") as f:
                f.write(self.txt)
            print(colored("-----------------------------------------", "green"))
            print(colored("OUTPUT TEXT: ", "green"))
            print(self.txt)
            print(colored("-----------------------------------------", "green"))

        else:
            print(colored("-----------------------------------------", "green"))
            print(colored("OUTPUT TEXT: ", "green"))
            print(self.txt)
            print(colored("-----------------------------------------", "green"))


def main():
    parser = argparse.ArgumentParser(prog="TextFixer", description="Correcting given text")
    parser.add_argument("-c", "--correct", action="store_true", help="Text correction")
    parser.add_argument("-s", "--stats", action="store_true", help="Show statistics")
    parser.add_argument("-m", "--misspell", action="store_true", help="Show misspelled words")
    parser.add_argument("input", type=str, help="Input text phrase or file path")
    parser.add_argument("output", type=str, nargs="?", default=None, help="Output file path")
    args = parser.parse_args()

    text_corrector = TextFixer(args.input)
    text_corrector.process_text(
        correct=args.correct,
        misspell=args.misspell,
        stats=args.stats,
        output=args.output,
    )


if __name__ == "__main__":
    main()
