""" from https://github.com/keithito/tacotron """
from text import cleaners
from text.symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
"""
一个字典，用于音素字符到id的映射
key是音素字符；
value是id，为整数；
"""
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
"""
一个字典,用于id到音素字符的映射
key是id，为整数
value是音素字符
"""
_id_to_symbol = {i: s for i, s in enumerate(symbols)}


def text_to_sequence(text, cleaner_names):
    '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
      Args:
        text: string to convert to a sequence
        cleaner_names: names of the cleaner functions to run the text through
      Returns:
        List of integers corresponding to the symbols in the text
    '''
    sequence = []

    clean_text = _clean_text(text, cleaner_names)
    for symbol in clean_text:
        symbol_id = _symbol_to_id[symbol]
        sequence += [symbol_id]
    return sequence


def cleaned_text_to_sequence(cleaned_text):
    '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
      Args:
        text: string to convert to a sequence
      Returns:
        List of integers corresponding to the symbols in the text
    '''
    """
    函数功能：将音素文本字符串转变到id
    cleaned_text: 为待转变的音素字符串
    return: 音素相对应的id列表
    """
    sequence = [_symbol_to_id[symbol] for symbol in cleaned_text]
    return sequence


def sequence_to_text(sequence):
    '''Converts a sequence of IDs back to a string'''
    result = ''
    for symbol_id in sequence:
        s = _id_to_symbol[symbol_id]
        result += s
    return result


def _clean_text(text, cleaner_names):
    for name in cleaner_names:
        cleaner = getattr(cleaners, name)
        if not cleaner:
            raise Exception('Unknown cleaner: %s' % name)
        text = cleaner(text)
    return text
