# Substitution Cipher — Applied Data Security Project

[![CI](https://github.com/ShahabBZG-MSc/substitution-cipher/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ShahabBZG-MSc/substitution-cipher/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Implementation of **classic cryptographic ciphers** — Caesar, Affine, and Substitution — with **frequency analysis** for cryptanalysis.  
Developed as part of the *Applied Data Security* MSc coursework at the University of Bologna.

---

## 📜 Features
- **Caesar Cipher** encryption & decryption
- **Affine Cipher** encryption & decryption
- **Monoalphabetic Substitution Cipher** (case-preserving)
- **Letter frequency analysis** and normalization
- **Frequency-based cryptanalysis** for simple substitution ciphers
- **Automated testing** with Pytest and GitHub Actions CI
- **100% code coverage** verified in CI

---

## 📂 Repository Structure
```
substitution-cipher/
├── src/
│   └── crypto/
│       ├── paths.py                # Directory paths helper
│       ├── substitution.py         # Cipher implementations + analysis
│       └── __init__.py
├── tests/
│   └── test_substitution.py        # Pytest test suite
├── notebooks/
│   ├── substitution_ciphers.ipynb  # Demo and analysis notebook
├── data/
│   ├── ciphertext_caesar.txt
│   ├── ciphertext_simple.txt
│   └── wikipedia_cybersecurity.txt
├── requirements.txt
├── .coveragerc
├── .github/workflows/ci.yml        # GitHub Actions CI workflow
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ShahabBZG-MSc/substitution-cipher.git
cd substitution-cipher
```

### 2. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run tests
```bash
pytest --cov=src --cov-report=term-missing
```

### 4. Execute the notebook
Open `notebooks/substitution_ciphers.ipynb` in Jupyter Lab or VS Code, or run:
```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/substitution_ciphers.ipynb
```

---

## 📌 Example Usage
```python
from crypto.substitution import caesar_encrypt, caesar_decrypt

msg = "hello world"
shift = 3
enc = caesar_encrypt(msg, shift)
dec = caesar_decrypt(enc, shift)

print("Encrypted:", enc)  # khoor zruog
print("Decrypted:", dec)  # hello world
```

---

## 🧪 Methods
- **Implementation:** Python 3.11, object-free functional style
- **Testing:** Pytest with 100% coverage
- **CI/CD:** GitHub Actions for automated tests and notebook execution
- **Data Analysis:** Jupyter Notebook for frequency analysis visualisation
- **Reproducibility:** `.coveragerc` to ensure coverage metrics are consistent across environments

---

## 📊 Results
- All cipher functions verified against known plaintext/ciphertext pairs
- Frequency analysis successfully identifies likely substitutions for simple substitution ciphers
- CI workflow executes tests and notebook on every push/PR to `main`

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

*Maintained by [Shahab Bozorgzadeh](https://github.com/Shahubzg) – MSc in Electronics for intelligent systems*
