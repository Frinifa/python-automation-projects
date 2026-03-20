from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Python is a powerful programming language used in many fields such as web development,
data science, artificial intelligence, and automation. It is easy to learn and widely used.
Many developers prefer Python because of its simplicity and readability.
"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

summary = summarizer(parser.document, 2)

print("Summary:\n")
for sentence in summary:
    print(sentence)
