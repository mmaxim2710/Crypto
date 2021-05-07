import re
import random


def compare_texts(first_text, second_text):
    count = 0

    for i in range(len(first_text)):
        if first_text[i] == second_text[i]:
            count += 1

    return count / len(first_text)


def generate_random_alphabet_text(size):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = ''
    for i in range(size):
        text += alphabet[random.randint(0, len(alphabet) - 1)]
    return text


def generate_random_words_text(size, filename):
    fd = open(filename, 'r')
    words = fd.read().casefold().replace('\n', ' ').split(' ')
    text = ''
    for i in range(size):
        text += words[random.randint(0, len(words) - 1)]
    return text


if __name__ == '__main__':
    fd1 = open('text1.txt', 'r')
    fd2 = open('text2.txt', 'r')

    pattern = re.compile('[.,:"-]')
    text1 = fd1.read().casefold().replace('\n', ' ').replace(' ', '')
    text2 = fd2.read().casefold().replace('\n', ' ').replace(' ', '')
    text1 = pattern.sub('', text1)
    text2 = pattern.sub('', text2)

    print('1. Два осмысленных текста:')
    print('Size of text1 =', len(text1))
    print('Size of text2 =', len(text2))
    print('Процент совпадения букв:', compare_texts(text1, text2))

    random_text1 = generate_random_alphabet_text(len(text1))

    print('\n2. Осмысленный текст и текст из случайных букв:')
    print('Size of text1 =', len(text1))
    print('Size of text2 =', len(random_text1))
    print('Процент совпадения букв:', compare_texts(text1, random_text1))

    random_words_text1 = generate_random_words_text(len(text1) // 5, 'words.txt')

    print('\n3. Осмысленный текст и текст из случайных слов:')
    print('Size of text1 =', len(text1))
    print('Size of text2 =', len(random_words_text1))
    print('Процент совпадения букв:', compare_texts(text1, random_words_text1))

    random_text2 = generate_random_alphabet_text(len(text1))

    print('\n4. Два текста из случайных букв:')
    print('Size of text1 =', len(text1))
    print('Size of text2 =', len(random_text2))
    print('Процент совпадения букв:', compare_texts(random_text1, random_text2))

    random_words_text2 = generate_random_words_text(len(text1) // 5, 'words.txt')

    print('\n5. Два текста из случайных слов:')
    print('Size of text1 =', len(text1))
    print('Size of text2 =', len(random_words_text1))
    print('Процент совпадения букв:', compare_texts(random_words_text1, random_words_text2))
