from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


FACTORY = StemmerFactory()

# id_dictionary
my_file = open("./dictionary_indonesia.txt", "r")
content_list = my_file.readlines()
ID_DICT = [x.replace("\n", "") for x in content_list]


def get_stem(sentences):
    stemmer = FACTORY.create_stemmer()
    return stemmer.stem(sentences)


def pie_graph_sentence(stem_sentences, raw_sentences):
    l = 0
    bahasa = 0
    unknown = 0
    while l < len(stem_sentences.split()):
        if stem_sentences.split()[l] in ID_DICT:
            bahasa += 1
        else:
            unknown += 1
        l += 1

    return [bahasa, unknown]


def process_text(file_path):
    with open(file_path, "r") as f:
        sentences = f.read()
    output = get_stem(sentences)

    result_count = pie_graph_sentence(output, sentences)
    print(result_count)
    return result_count, sentences
