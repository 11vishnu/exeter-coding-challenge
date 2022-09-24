#the program for example search for the word 'abide' exactly and replace it but does not replace 'abides' or 'ABIDE'
import string
import csv
import shutil

file_to_search=r't8.shakespeare.txt'  #file-original copy
translated_file=r't8.shakespeare.transl.txt' #copy of the file to search,replace


with open('french_dictionary.csv','r+') as f:  #converting the dictionary.csv file into python dictionary
    french_dict = dict(filter(None, csv.reader(f))) 
with open('find_words.txt','r') as fw:       #converting the find_words.txt into list
    words_find=fw.read().splitlines()


def main():
    shutil.copy(file_to_search,translated_file) #making a copy of file
    text_to_search()              #function to get the search word and coomplete the process
    

def text_to_search():       #loops over the list of words and calls the translate function to search and replace it
    for word in words_find:          
        temp_word=word
        e,f,c=translate_file(temp_word)
        if c>0:
            frequency(e,f,c)       #to write a frequency.csv file


def eng_fren_dict(eng_word): #checks the dictionary and returns the  replace word
    for key in french_dict:
        if key==eng_word:
            value=french_dict[key]
            return value


def frequency(e,f,c): #writes a csv file with English word,french word and no. of times word is replaced.
    frequency_list=[]
    frequency_tuple=(e,f,c)
    frequency_list.extend(frequency_tuple) 
    with open('frequency.csv', 'a',newline="") as frequency_csv:
        csvfile = csv.writer(frequency_csv,delimiter=',')
        csvfile.writerow(frequency_list)
        
def translate_file(temp_word): #gets a search word and looks for the replace word in "eng_fren_dict" function and replaces it.
    count=0
    replace_word= eng_fren_dict(temp_word)
    with  open(translated_file,'r+') as tf:
        list_of_lines=tf.readlines()
        tf.seek(0)
        for line in list_of_lines:
            if temp_word in line:
                l=list(line.split())
                l = [''.join(c for c in s if c not in string.punctuation) for s in l]  #remove punctuation
                if temp_word in l:
                    line=line.replace(temp_word, replace_word)
                    count+=1
            tf.write(line) 

    return temp_word,replace_word,count  

if __name__ == '__main__':
    main()   

