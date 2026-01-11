## Overview

NeuralCrypt is a state-of-the-art cryptanalysis platform combining deep neural sequence modeling with classical cryptographic heuristics.

It automates:

- Cipher classification  
- Hybrid neural + rule-based plaintext recovery  

Designed for robustness, scalability, and interpretability, NeuralCrypt deciphers complex ciphers efficiently.

## Key Features

### Probabilistic Dataset Augmentation
- Simulates encryption schemes with variable key lengths, cipher parameters, and noise models  
- Generates large-scale labeled corpora for robust training  

### Neural Cipher Classification
- Convolutional + BiLSTM networks capture sequential dependencies in ciphertext embeddings  
- Discriminates substitution, transposition, and polyalphabetic ciphers  

### Sequence-to-Sequence Decryption
- Encoder-decoder with attention approximates ciphertext to plaintext mappings  
- Optimized with cross-entropy, teacher forcing, and scheduled sampling  

### Optimized Training & Inference
- CPU-efficient batch loaders, memory management, and vectorized tensor operations  
- Implemented with PyTorch and NumPy  

### Evaluation Metrics
- Decryption accuracy  
- Normalized edit distance  
- BLEU scores  
- Confusion matrices  

## Architecture

      Ciphertext Input
              │
              ▼
     +-----------------+
     | Cipher Embedding |
     +-----------------+
              │
              ▼
    +--------------------------+
    | Convolutional Layers     |
    +--------------------------+
              │
              ▼
     +-----------------+
     | BiLSTM Encoder  |
     +-----------------+
              │
              ▼
      +----------------------+
      | Cipher Classification|
      +----------------------+
              │
              ▼
      +-----------------------------+
      | Encoder-Decoder w/Attention|
      +-----------------------------+
              │
              ▼
      +-----------------------------+
      | Predicted Plaintext Output |
      +-----------------------------+
              │
              ▼
       +-------------------------------------+
       |Hybrid Neural + Rule-Based Inference|
       +-------------------------------------+


## Attention Visualization

The attention mechanism shows which parts of the ciphertext the model focuses on when predicting plaintext. Example:

Ciphertext: LXFOP VEFRNHR
Predicted: ATTACK AT DAWN

Mapping Attention Weights (0-9 scale):
```
L -> A ████████ 8
X -> T ██████ 6
F -> T ███████ 7
O -> A ████████ 8
P -> C ██████ 6
V -> K ██████ 6
E ->   ███ 3
F -> A █████ 5
R -> T ███████ 7
N -> D ██████ 6
H -> A █████ 5
R -> W ███████ 7
```

This gives insight into how the model assigns importance to each ciphertext character during decryption.  

## Screenshots

<p align="center">
  <img src="/images/neurl2.png" width="450"/>
  <img src="/images/neurl.png" width="450"/>
</p>

## Sample Runs
-----------------------------------------------------------------------
| Cipher Type     | Ciphertext       | Predicted Plaintext | Accuracy |
|-----------------|-----------------|----------------------|----------|
| Substitution    | QEB NRFZH YOLTK | THE QUICK BROWN      | 92%      |
| Transposition   | TEH RCIUK BOWNF | THE QUICK BROWN      | 88%      |
| Polyalphabetic  | LXFOP VEFRNHR   | ATTACK AT DAWN       | 90%      |
-----------------------------------------------------------------------


## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/NeuralCrypt.git
cd NeuralCrypt

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Train cipher classifier
```
python train_classifier.py --dataset ./data
```

#### Train decryption model
```
python train_decryptor.py --dataset ./data
```

#### Hybrid decryption on ciphertext
```
python decrypt.py --input "QEB NRFZH YOLTK" --cipher_type "substitution"
```

## Evaluation

- Decryption accuracy – percentage of correctly recovered characters
- Normalized edit distance – character-level error metric
- BLEU score – sequence similarity measure
- Confusion matrices – insight into misclassifications

## Optional Enhancements

- Attention heatmaps for model interpretability
- Benchmark tables for accuracy vs key length or noise levels
- Interactive Jupyter notebooks for hands-on analysis
