from textfixer import TextFixer

def creating_object(input="", output=""):
    phrase = input
    expected_output = output
    text_corrector = TextFixer(phrase)
    text_corrector.process_text(correct=True)
    assert text_corrector.txt == expected_output


def test_corrector_multiply_spaces():
    creating_object(input="Sprawdzamy  czy  usunie  podwojne                 spacje.",
                    output="Sprawdzamy czy usunie podwojne spacje.")
   
def test_corrector_multiply_dots():
    creating_object(input="Testuje..... To.", output="Testuje. To.")

def test_corrector_multiply_commas():
    creating_object(input="I to jest,,,,, to.", output="I to jest, to.")

def test_corrector_upper_first_letter():
    creating_object(input="rabarbar", output="Rabarbar")

def test_corrector_adding_space_after_symbols():
    creating_object(input="Jak sie masz?Bracie?", output="Jak sie masz? Bracie?")
    creating_object(input="Rabarbar.Rabarbar?", output="Rabarbar. Rabarbar?")

def test_corrector_upper_first_letter_of_the_sentence():
    creating_object(input="Jak sie masz? bracie?", output="Jak sie masz? Bracie?")
    creating_object(input="Jak sie masz?bracie?", output="Jak sie masz? Bracie?")

def test_gutenberg():
    creating_object(input="wspaniała   wiosenna   pogoda  dzisiaj  sprawia ,,,,  że  chce się wyjść na długi spacer wśród kwitnących drzew i zielonych łąk pełnych kolorowych kwiatów.oraz (  kwiat  ).",
                    output="Wspaniała wiosenna pogoda dzisiaj sprawia, że chce się wyjść na długi spacer wśród kwitnących drzew i zielonych łąk pełnych kolorowych kwiatów. Oraz (kwiat)."
    )