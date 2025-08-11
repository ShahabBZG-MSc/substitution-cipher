# src/crypto/__init__.py
"""
Crypto package for Applied Data Security — Substitution Cipher project.
"""

from .substitution import (
    caesar_encrypt,
    caesar_decrypt,
    affine_encrypt,
    affine_decrypt,
    substitution_encrypt,
    substitution_decrypt,
    letter_frequencies,   # normalized now
)

__all__ = [
    "caesar_encrypt",
    "caesar_decrypt",
    "affine_encrypt",
    "affine_decrypt",
    "substitution_encrypt",
    "substitution_decrypt",
    "letter_frequencies",
]
