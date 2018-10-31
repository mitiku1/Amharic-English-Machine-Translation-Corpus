import argparse
import json
from preprocess import get_all_sentences


def main():
    all_sentences = get_all_sentences("dataset")
    english_sentences = list(all_sentences.keys())
    amharic_sentences = [all_sentences[sentence] for sentence in english_sentences]
    new_json_file_dict = [{"english":eng_sent,"amharic":amh_sent} for (eng_sent, amh_sent) in zip(english_sentences, amharic_sentences) ]
    with open('dataset.json', 'w') as outfile:
        json.dump(new_json_file_dict, outfile)
if __name__ == '__main__':
    main()