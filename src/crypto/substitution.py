"""
Substitution/Classic ciphers utilities.

Notes:
- Functions are import-safe (no I/O at import time).
- Substitution mapping is expected over lowercase letters a–z.
- substitution_* functions preserve the original case of letters.
"""

from __future__ import annotations

import string
from collections import Counter
from .paths import DATA_DIR  # package-relative import


# ---------------------------
# Caesar cipher (lowercase-only transform; others preserved)
# ---------------------------

def caesar_encrypt(plaintext: str, shift: int = 0) -> str:
    alphabet = string.ascii_lowercase
    out = []
    for ch in plaintext:
        if ch in alphabet:
            idx = (alphabet.index(ch) + shift) % 26
            out.append(alphabet[idx])
        else:
            # leave uppercase / punctuation / spaces unchanged
            out.append(ch)
    return "".join(out)


def caesar_decrypt(ciphertext: str, shift: int = 0) -> str:
    alphabet = string.ascii_lowercase
    out = []
    for ch in ciphertext:
        if ch in alphabet:
            idx = (alphabet.index(ch) - shift) % 26
            out.append(alphabet[idx])
        else:
            out.append(ch)
    return "".join(out)


# ---------------------------
# Simple substitution (case-preserving)
# mapping: dict over lowercase letters, e.g. {'a':'q', 'b':'w', ...}
# ---------------------------

def substitution_encrypt(plaintext: str, mapping: dict[str, str]) -> str:
    out = []
    for ch in plaintext:
        if ch.isalpha() and ch.lower() in mapping:
            enc = mapping[ch.lower()]
            out.append(enc.upper() if ch.isupper() else enc)
        else:
            out.append(ch)
    return "".join(out)


def substitution_decrypt(ciphertext: str, mapping: dict[str, str]) -> str:
    inv = {v: k for k, v in mapping.items()}
    out = []
    for ch in ciphertext:
        lo = ch.lower()
        if ch.isalpha() and lo in inv:
            dec = inv[lo]
            out.append(dec.upper() if ch.isupper() else dec)
        else:
            out.append(ch)
    return "".join(out)


# ---------------------------
# Affine cipher (lowercase-only transform; others preserved)
# E(x) = (a*x + b) mod 26,  D(y) = a_inv * (y - b) mod 26
# ---------------------------

def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    alphabet = string.ascii_lowercase
    out = []
    for ch in plaintext:
        if ch in alphabet:
            x = ord(ch) - ord("a")
            y = (a * x + b) % 26
            out.append(chr(y + ord("a")))
        else:
            out.append(ch)
    return "".join(out)


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    # find modular inverse of a mod 26
    a_inv = None
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    if a_inv is None:
        # not invertible; return text unchanged (or raise)
        return ciphertext

    alphabet = string.ascii_lowercase
    out = []
    for ch in ciphertext:
        if ch in alphabet:
            y = ord(ch) - ord("a")
            x = (a_inv * (y - b)) % 26
            out.append(chr(x + ord("a")))
        else:
            out.append(ch)
    return "".join(out)


# ---------------------------
# Frequency utilities expected by tests
# ---------------------------

def letter_frequencies(text: str) -> dict[str, float]:
    """
    Return normalized frequencies of a–z in the given text (case-insensitive).
    Only includes letters that appear at least once, sorted by letter.
    """
    text = text.lower()
    filtered = [ch for ch in text if ch in string.ascii_lowercase]
    n = len(filtered)
    if n == 0:
        return {}
    counts = Counter(filtered)
    return {char: count / n for char, count in sorted(counts.items())}

# ---------------------------
# Demo / notebook-derived code (guarded)
# ---------------------------

if __name__ == "__main__":  # pragma: no cover
    # Example demo usage that won’t run during import/CI.
    # Safe to remove or expand locally as you wish.

    # Caesar quick check
    pt = "hello!"
    ct = caesar_encrypt(pt, shift=4)
    print(f"Caesar enc: {pt} -> {ct}")
    print(f"Caesar dec: {ct} -> {caesar_decrypt(ct, shift=4)}")

    # Substitution quick check
    demo_map = {"h": "a", "e": "p", "l": "w", "o": "q"}
    pt2 = "hello!"
    ct2 = substitution_encrypt(pt2, demo_map)
    print(f"Subst enc: {pt2} -> {ct2}")
    print(f"Subst dec: {ct2} -> {substitution_decrypt(ct2, demo_map)}")

    # Affine quick check
    pt3 = "hello world!"
    a, b = 3, 1
    ct3 = affine_encrypt(pt3, a, b)
    print(f"Affine enc: {pt3} -> {ct3}")
    print(f"Affine dec: {ct3} -> {affine_decrypt(ct3, a, b)}")

    # Optional: reading data files if they exist
    try:
        caesar_path = DATA_DIR / "ciphertext_caesar.txt"
        if caesar_path.exists():
            with open(caesar_path, "r", encoding="utf-8") as f:
                sample = f.read().strip().lower()
            print("First 5 Caesar decrypt candidates:")
            for s in range(5):
                print(s, "->", caesar_decrypt(sample, s)[:80])
    except Exception as e:
        print("Demo data step skipped:", e)