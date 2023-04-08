# Text Fixer 

TextFixer is a Python script designed to correct and analyze text written in ~~any language~~ Polish. The script is able to correct common mistakes and provide information about the text statistics and misspelled words.

## Installation
1. Clone the repo or download the source code.
`git clone https://github.com/mzelder/Text-Fixer.git`

2. Install the required dependencies with the command 
`pip install -r requirments.txt`

    
## Usage

Once the requirments are installed, you can run the script using following command:  
`python3 textfixer.py [-h] [-c] [-m] [-s] input [output]`

### Arguments
- `input`: A required argument specifying the text phrase or file path to be corrected and analyzed.
- `output`: An optional argument that specifies the output file path.


### Options
- `-h`, `--help`: An optional argument that displays the help message and exits.
- `-c`, `--correct`: An optional argument that corrects the loaded text.
- `-m`, `--misspell`: An optional argument that determines whether words in the text are misspelled.
- `-s`, `--stats`:  An optional argument that shows statistics for the text.


## Examples
### Example 1: Correcting a text
Input:

`python3 textfixer.py -c "jak tam,,,, wszystko ok?tomek?"`

Output:
```
-----------------------------------------
OUTPUT TEXT: 
Jak tam, wszystko ok? Tomek?
-----------------------------------------
```

### Example 2: Detecting misspelled words
Input:

foo.txt:
`Czy z tym tekstem jeszt wszystko okai?`

```
python3 textfixer.py -m foo.txt
```

Output:
```
-----------------------------------------
MISSPELLED: 
"jeszt" is probably misspelled
"okai" is probably misspelled
-----------------------------------------
```

### Example 3: Showing statistics for the text
Input:

`python3 textfixer.py -s "Jak sie masz? Przyjacielu?"`

Output:
```
-----------------------------------------
STATISTICS: 
Word count: 4
Sentence count: 2
Character count: 26
Space count: 3
-----------------------------------------

```

## Authors
- [***Maciej Zelder***](https://github.com/mzelder) - *CS Student* - ***All work***