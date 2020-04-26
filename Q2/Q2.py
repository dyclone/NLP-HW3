import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

def entities(a_text):
    '''

    :param a_text: A sentence of type string
    :return: Takes a sentence and first creates word tokens out of it. Those tokens are then assigned POS tags.
    Last ne_chunk() is used on the POS tagged word tokens to classify them as named entities or not
    '''
    return ne_chunk(pos_tag(word_tokenize(a_text)))

def show_entities(a_file):
    '''

    :param a_file: A text file filled with sentences
    :return: Goes through each sentence in a file and prints out the named entities found.
    Also displays a tree showing where in the sentence the named entities occur
    '''
    #Open test file
    test = open(a_file, "r")
    #Sentence count for display
    sentence_num = 1

    #For loop to go through each sentence from the test file adn return the name entities
    for sentence in test:
        ne_of_sentence = entities(sentence)

        print("Named entities found in sentence ", sentence_num)
        print(ne_of_sentence)
        ne_of_sentence.draw()

        sentence_num += 1
    #Close the test file
    test.close()

def main():
    show_entities("HW3_test")

main()