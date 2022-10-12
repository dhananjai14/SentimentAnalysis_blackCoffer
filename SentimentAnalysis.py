import pandas as pd

import os

import traceback
from nltk.corpus import stopwords
from logger import logs


class sentiment:
    def __init__(self):
        try:
            self.log = logs()
            self.log.write_log('SentimentAnalysis', 'Inside the class "sentiment"')

        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')

    def stop_words_list(self, stop_words_folder_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "stop words list"')
            path = stop_words_folder_path
            self.log.write_log('SentimentAnalysis', 'stop word path {}'.format(path))
            # path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\StopWords'

            files = os.listdir(path)
            words = pd.DataFrame()

            for file in files:
                data = pd.read_table(r'{}\{}'.format(path, file), delimiter='|', header=None,
                                     names=['col_1', 'col_2'],
                                     encoding='windows-1252')
                self.log.write_log('SentimentAnalysis', '{} file loaded'.format(file))

                data['col_1'] = data['col_1'].str.replace(' ', '')
                words = pd.concat([words, data], ignore_index=True)

            self.log.write_log('SentimentAnalysis', 'Dataframe of all stop words is created')
            words.drop(columns='col_2', inplace=True)
            stop_words_list = words['col_1'].tolist()
            self.log.write_log('SentimentAnalysis', 'Stop Words list created and returned')
            return stop_words_list
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def positive_words_list(self, positive_word_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "positive words list"')
            self.positive_path = positive_word_path
            self.log.write_log('SentimentAnalysis', 'positive word path {}'.format(self.positive_path))

            # positive_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\MasterDictionary\positive-words.txt'
            positive = pd.read_table(self.positive_path, delimiter='|', header=None, names=['col_1', 'col_2'],
                                     encoding='windows-1252')
            self.log.write_log('SentimentAnalysis', "Positive file read complete")
            positive.drop(columns='col_2', inplace=True)
            positive_words = positive['col_1'].tolist()
            self.log.write_log('SentimentAnalysis', "Positive word list created and returned")
            return positive_words
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def negative_words_list(self, negative_word_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "negative words list"')
            self.negative_path = negative_word_path
            self.log.write_log('SentimentAnalysis', 'negative word path {}'.format(self.negative_path))

            # negative_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\MasterDictionary\negative-words.txt'

            negative = pd.read_table(self.negative_path, delimiter='|', header=None, names=['col_1', 'col_2'],
                                     encoding='windows-1252')
            self.log.write_log('SentimentAnalysis', "Negative file read complete")
            negative.drop(columns='col_2', inplace=True)
            negative_words = negative['col_1'].tolist()
            self.log.write_log('SentimentAnalysis', "Negative word list created and returned")
            return negative_words
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def manual_tokenize(self, file_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "manual tokenize"')
            l = []
            path = file_path
            self.log.write_log('SentimentAnalysis', 'file path entered: {}'.format(file_path))
            try:
                with open(path, encoding='utf-8') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        l.append(line.replace('\n', '').replace(' \n', '').replace('”', '').replace('.', '').replace(',', '').replace('“','').replace('?', '').replace('!', '').split(' '))
                self.log.write_log('SentimentAnalysis', 'encoding = utf-8')
            except:
                with open(path, encoding='windows-1252') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        l.append(line.replace('\n', '').replace(' \n', '').replace('”', '').replace('.', '').replace(',', '').replace('“','').replace('?', '').replace('!', '').split(' '))
                self.log.write_log('SentimentAnalysis', 'encoding = windows-1252')

            text = []
            for i in l:
                for j in i:
                    if j != '':
                        text.append(j)
            self.log.write_log('SentimentAnalysis', 'Text file tokenized and returned as list')
            return text

        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def score_cal(self, tokenised_list, positive_word_list, negative_word_list):
        """

        :param tokenised_list:
        :param positive_word_list:
        :param negative_word_list:
        :return: positive score, negative score, polarity_score,subjectivity_score
        """
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "score cal"')
            pos_score = 0
            neg_score = 0
            for wrd in tokenised_list:
                if wrd in positive_word_list:
                    pos_score = pos_score + 1
                    #print(wrd, '\t pos')

                if wrd in negative_word_list:
                    neg_score = neg_score + 1
                    # print(wrd, '\t neg')

            polarity_score = (pos_score - neg_score) / ((pos_score + neg_score) + .000001)
            subjectivity_score = (pos_score + neg_score) / ((pos_score + neg_score) + .000001)
            self.log.write_log('SentimentAnalysis', "Positive score{}".format(pos_score))
            self.log.write_log('SentimentAnalysis', "Negative score{}".format(neg_score))
            self.log.write_log('SentimentAnalysis', "Polarity score{}".format(polarity_score))
            self.log.write_log('SentimentAnalysis', "Subjective score{}".format(subjectivity_score))

            return pos_score, neg_score, polarity_score, subjectivity_score
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def readability_scores(self, file_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "readability scores"')
            self.log.write_log('SentimentAnalysis', 'Path entered {}'.format(file_path))
            words_list = self.manual_tokenize(file_path)
            self.log.write_log('SentimentAnalysis', 'Word list created')
            tot_words = len(words_list)
            self.log.write_log('SentimentAnalysis', 'total word count {}'.format(tot_words))

            # As we know that the sentence can be terminated by either ".", "?","!"
            sentence = 0
            try:
                with open(file_path, encoding='utf-8') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        if '.' in line:
                            sentence = sentence + line.count('.')
                        if '?' in line:
                            sentence = sentence + line.count('?')
                        if '!' in line:
                            sentence = sentence + line.count('!')
                self.log.write_log('SentimentAnalysis', 'encoding = utf-8')

            except:
                with open(file_path, encoding='windows-1252') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        if '.' in line:
                            sentence = sentence + line.count('.')
                        if '?' in line:
                            sentence = sentence + line.count('?')
                        if '!' in line:
                            sentence = sentence + line.count('!')
                self.log.write_log('SentimentAnalysis', 'encoding = windows-1252')

            self.log.write_log('SentimentAnalysis', 'File successfully open')
            average_sentence_length = tot_words / sentence

            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            self.log.write_log('SentimentAnalysis', 'list of vowels created')

            complex_words = []
            for word in words_list:
                cnt = 0
                for letter in word:
                    if letter in vowels:
                        cnt = cnt + 1
                        if cnt > 1:
                            complex_words.append(word)
                            break
            self.log.write_log('SentimentAnalysis', 'Complex words list created')
            complex_words_percent = len(complex_words) / tot_words
            fog_index = .4*(complex_words_percent + average_sentence_length)
            self.log.write_log('SentimentAnalysis', 'average sentence length: {}'.format(average_sentence_length))
            self.log.write_log('SentimentAnalysis', 'complex_word_percent : {}'.format(complex_words_percent))
            self.log.write_log('SentimentAnalysis', 'fog_index: {}'.format(fog_index))

            return int(round(average_sentence_length,0)),len(complex_words) ,complex_words_percent, fog_index

        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def avg_words_sentence(self,text_file_path):
        try:
            self.log.write_log('SentimentAnalysis', 'Inside the method "avg words sentence"')
            self.log.write_log('SentimentAnalysis', 'Path entered {}'.format(text_file_path))
            sentence = 0
            words = 0
            try:
                with open(text_file_path, encoding='utf-8') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        if '.' in line:
                            sentence = sentence + line.count('.')
                        if '?' in line:
                            sentence = sentence + line.count('?')
                        if '!' in line:
                            sentence = sentence + line.count('!')
                        words = words + len(line.replace('“', '').replace('”', '').replace('’', '').strip())
                self.log.write_log('SentimentAnalysis', 'encoding = utf-8')

            except:
                with open(text_file_path, encoding='windows-1252') as fp:
                    lines = fp.readlines()
                    for line in lines:
                        if '.' in line:
                            sentence = sentence + line.count('.')
                        if '?' in line:
                            sentence = sentence + line.count('?')
                        if '!' in line:
                            sentence = sentence + line.count('!')
                        words = words + len(line.replace('“', '').replace('”', '').replace('’', '').strip())
                self.log.write_log('SentimentAnalysis', 'encoding = windows-1252')


            self.log.write_log('SentimentAnalysis', 'File read by the python')

            avg_word_sentece = int(round((words/sentence), 0))
            self.log.write_log('SentimentAnalysis', 'avg_word_sentence: {}'.format(avg_word_sentece))
            return avg_word_sentece
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def word_count(self, path_of_file):
        try:
            self.log.write_log('SentimentAnalysis', "Inside the method word_count")
            self.log.write_log('SentimentAnalysis', "Path entered: {}".format(path_of_file))
            words = self.manual_tokenize(path_of_file)
            self.log.write_log('SentimentAnalysis', "{} file read ".format(path_of_file))

            stop_words_nltk = set(stopwords.words('english'))
            self.log.write_log('SentimentAnalysis', "Stop word imported from NLTK package")
            text_without_stop_words = []
            for word in words:
                if word not in stop_words_nltk:
                    text_without_stop_words.append(word)
            word_cnt = len(text_without_stop_words)
            self.log.write_log('SentimentAnalysis', 'word count without stop words: {}'.format(word_cnt))
            return word_cnt
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def syllable_per_words(self, tokenised_list):
        try:
            self.log.write_log('SentimentAnalysis', "inside the method syllable per words")
            syllable = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'ed', 'es', 'ing', 'er']
            self.log.write_log('SentimentAnalysis', "Syllable defined {}".format(syllable))
            syllable_count = 0
            for wrd in tokenised_list:
                if wrd[-2:] in syllable:
                    wrd = wrd[:-2]
                if wrd[-3:] in syllable:
                    wrd = wrd[:-3]
                for letter in wrd:
                    if letter in syllable:
                        syllable_count = syllable_count + 1
            self.log.write_log('SentimentAnalysis', "Syllable count is {}".format(syllable_count))
            syllable_per_word = int(round(syllable_count/len(tokenised_list),0))
            self.log.write_log('SentimentAnalysis', "syllable per word: {}".format(syllable_per_word))
            return syllable_per_word
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def personal_pronoun_count(self, tokenised_list):
        try:
            self.log.write_log('SentimentAnalysis', "inside the method personal_pronoun_count")
            personal_pronoun_list = ["I", "we", "We", "my", "My", "ours", "our", "Ours", "Our", "us", 'Us']
            self.log.write_log('SentimentAnalysis', "personal_pronoun_list : {}".format(personal_pronoun_list))
            count_personal_pronoun = 0
            for wrd in tokenised_list:
                if wrd in personal_pronoun_list:
                    count_personal_pronoun = count_personal_pronoun + 1
            self.log.write_log('SentimentAnalysis', "personal_pronoun_count is {}".format(count_personal_pronoun))

            return count_personal_pronoun
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()

    def avg_word_length(self, tokenise_list):
        try:
            total_letter = 0
            total_word = 0
            for wrd in tokenise_list:
                total_letter = len(wrd) + total_letter
                total_word = total_word + 1
            avg_word_len =  int(round(total_letter / total_word, 0))
            return avg_word_len
        except:
            self.log.write_log('SentimentAnalysis', traceback.format_exc(), 'error')
            return traceback.format_exc()



