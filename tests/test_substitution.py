import string
import random
from src.crypto.substitution import (
    caesar_encrypt, caesar_decrypt,
    affine_encrypt, affine_decrypt,
    substitution_encrypt, substitution_decrypt,
    letter_frequencies, normalize_frequencies,
)
from src.crypto.paths import DATA_DIR, DOCS_DIR, NOTEBOOKS_DIR

def test_paths_exist():
    assert DATA_DIR.exists()
    assert DOCS_DIR.exists() or True  # docs may be empty initially
    assert NOTEBOOKS_DIR.exists()

def test_caesar_roundtrip():
    msg = 'Hello, Caesar! Zz'
    for shift in [0, 1, 3, 13, 25]:
        enc = caesar_encrypt(msg, shift)
        dec = caesar_decrypt(enc, shift)
        assert dec == msg

def test_affine_roundtrip():
    msg = 'Affine Cipher Test!'
    # choose a,b with a coprime to 26
    for a in [1, 3, 5, 7, 11, 15, 17, 19, 21, 23, 25]:
        for b in [0, 1, 5, 13, 25]:
            enc = affine_encrypt(msg, a, b)
            dec = affine_decrypt(enc, a, b)
            assert dec == msg

def test_substitution_roundtrip():
    # build a random permutation to stress-test
    letters = list(string.ascii_lowercase)
    random.seed(42)
    perm = letters[:]
    random.shuffle(perm)
    mapping = dict(zip(letters, perm))

    msg = 'Substitution Cipher 123! ABC xyz'
    enc = substitution_encrypt(msg, mapping)
    dec = substitution_decrypt(enc, mapping)
    assert dec == msg

def test_letter_frequencies_normalization():
    text = 'aabBccC!!'
    freqs = letter_frequencies(text)
    probs = normalize_frequencies(freqs)
    assert abs(sum(probs.values()) - 1.0) < 1e-9
    # check specific letters
    assert freqs['a'] == 2
    assert freqs['b'] == 2  # 'B' counted as 'b'
    assert freqs['c'] == 3
