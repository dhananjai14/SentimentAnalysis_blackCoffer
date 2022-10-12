import DataExtraction
from SentimentAnalysis import sentiment as st
import pandas as pd


target_path = r"C:\Users\preet\Desktop\DS\Project\Blackcoffer\Files"
excel_path = r"C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\Input.xlsx"
web_driver = r'C:\Users\preet\Desktop\DS\Project\Youtube\chromedriver.exe'
ouput_file_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\OutputDataStructure.csv'

data = DataExtraction.DataExtract(excel_path, target_path)
data.data_load(web_driver)

sentiment = st()

stop_word_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\StopWords'
stop_word_list = sentiment.stop_words_list(stop_word_path)

positive_word_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\MasterDictionary\positive-words.txt'
positive_word_list = sentiment.positive_words_list(positive_word_path)

negative_word_path = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\20211030 Test Assignment\MasterDictionary\negative-words.txt'
negative_word_list = sentiment.negative_words_list(negative_word_path)

data = pd.read_excel(excel_path, engine='openpyxl')


out = pd.DataFrame(columns = ['URL_ID', 'URL' ,   'POSITIVE SCORE', 'NEGATIVE SCORE','POLARITY SCORE' ,
                              'SUBJECTIVITY SCORE','AVG SENTENCE LENGTH','PERCENTAGE OF COMPLEX WORDS'	,'FOG INDEX',
                              'AVG NUMBER OF WORDS PER SENTENCE',	'COMPLEX WORD COUNT',	'WORD COUNT',
                              'SYLLABLE PER WORD',	'PERSONAL PRONOUNS',	'AVG WORD LENGTH'])


for i in range(len(data)):
    url_id, url = data.iloc[i, :][0], data.iloc[i, :][1]
    file = r"{}/{}.txt".format(target_path, url_id)

    text_file_path = file
    tokenize_text = sentiment.manual_tokenize(text_file_path)

    pos_score, neg_score, polarity_score, subjectivity_score = sentiment.score_cal(tokenize_text, positive_word_list,
                                                                                   negative_word_list)

    average_sentence_length, complex_words, complex_words_percent, fog_index = sentiment.readability_scores(
        text_file_path)

    average_number_of_words_per_sentence = sentiment.avg_words_sentence(text_file_path)

    word_cnt = sentiment.word_count(text_file_path)

    syllable_per_word = sentiment.syllable_per_words(tokenize_text)

    count_personal_pronoun = sentiment.personal_pronoun_count(tokenize_text)

    avg_word_len = sentiment.avg_word_length(tokenize_text)

    dct = {"URL_ID": url_id,
           "URL": url,
           "POSITIVE SCORE": pos_score,
           "NEGATIVE SCORE": neg_score,
           "POLARITY SCORE": polarity_score,
           "SUBJECTIVITY SCORE": subjectivity_score,
           "AVG SENTENCE LENGTH": average_sentence_length,
           "PERCENTAGE OF COMPLEX WORDS": complex_words_percent,
           "FOG INDEX": fog_index,
           "AVG NUMBER OF WORDS PER SENTENCE": average_sentence_length,
           "COMPLEX WORD COUNT": complex_words,
           "WORD COUNT": word_cnt,
           "SYLLABLE PER WORD": syllable_per_word,
           "PERSONAL PRONOUNS": count_personal_pronoun,
           "AVG WORD LENGTH": avg_word_len}
    into1 = pd.DataFrame(dct, index = [0])
    out = pd.concat([out,into1], ignore_index=True)

out.to_csv(r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\OutputDataStructure.csv', index = False )
