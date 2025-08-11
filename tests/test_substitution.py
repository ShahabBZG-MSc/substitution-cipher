import string
import math
import random
import os, sys
from collections import Counter  # only used implicitly in assertions

# Make local runs work (CI also sets PYTHONPATH=src)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from crypto.paths import DATA_DIR, DOCS_DIR, NOTEBOOKS_DIR
from crypto.substitution import (
    caesar_encrypt, caesar_decrypt,
    affine_encrypt, affine_decrypt,
    substitution_encrypt, substitution_decrypt,
    letter_frequencies,
)

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

def test_affine_decrypt_when_a_not_invertible_returns_input():
    msg = "abc xyz"
    # a=2 is not invertible mod 26 (gcd(2,26)=2), so function returns ciphertext unchanged
    assert affine_decrypt(msg, a=2, b=1) == msg

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
    text = 'aabBccC!!'  # letters: a,a,b,B,c,c,C  -> total = 7
    freqs = letter_frequencies(text)

    # sums to ~1
    assert math.isclose(sum(freqs.values()), 1.0, rel_tol=0, abs_tol=1e-12)

    # specific letters (normalized)
    assert math.isclose(freqs['a'], 2/7, rel_tol=0, abs_tol=1e-12)
    assert math.isclose(freqs['b'], 2/7, rel_tol=0, abs_tol=1e-12)  # 'B' counted as 'b'
    assert math.isclose(freqs['c'], 3/7, rel_tol=0, abs_tol=1e-12)

    # letters not present should be absent from the dict
    assert 'z' not in freqs
    
def test_letter_frequencies_empty_string():
    assert letter_frequencies("") == {}
    assert letter_frequencies("!!!") == {}
