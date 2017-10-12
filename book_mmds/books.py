re_empty_line = re.compile(r'^\s*$')
re_remove_chars = re.compile("[\r\n•]+")
re_chapter_title = re.compile("^[A-ZÁÉÍÓÚÃÕ\. ]+\s*$")

def clean_line(line):
    
    return re_remove_chars.sub("", line)

def is_good_line_casmurro(line):
    
    return re_empty_line.match(line) is None and\
           re_chapter_title.match(line) is None
    
def is_good_line_clarice(line):
    
    return re_empty_line.match(line) is None
    
def clean_and_filter_casmurro(lines):
    
    return [line for line in [clean_line(line) for line in lines] if \
            is_good_line_casmurro(line)]

def clean_and_filter_clarice(lines):
    
    return [line for line in [clean_line(line) for line in lines] if \
            is_good_line_clarice(line)]

sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")

with codecs.open('dom_casmurro.txt', 'r', 'utf-8') as f:
    
    dom_casmurro = sent_tokenizer.tokenize(' '.join(clean_and_filter_casmurro(f.readlines())))
    
with codecs.open('perto_do_coracao_selvagem.txt', 'r', 'utf-8') as f:
    
    perto_coracao = sent_tokenizer.tokenize(' '.join(clean_and_filter_clarice(f.readlines())))
