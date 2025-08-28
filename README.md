# xai
This repository implements Explainable AI (XAI) methods as described in XAI survey papers..



# Interpretable Sentiment Analysis with LIME

This notebook provides a hands-on walkthrough of **LIME (Local Interpretable Model-Agnostic Explanations)** applied to a sentiment classification model built using two examples - first, a basic one, using sklearn, and a more complex one, using a BERT LIME Hugging Face's transformer pipeline. It is designed for educational and research purposes, especially in the context of Explainable AI (XAI).

## Objective

To demonstrate how perturbation-based methods like LIME can help interpret black-box NLP models by showing which parts of the input text most influence model predictions.

## Contents

- Load a pre-trained sentiment analysis pipeline (`nlptown/bert-base-multilingual-uncased-sentiment`)
- Define a wrapper function compatible with LIME
- Use `lime_text.LimeTextExplainer` to generate explanations
- Visualize which words contribute most positively/negatively to sentiment prediction

## Requirements

Make sure the following packages are installed:

```bash
pip install lime transformers torch numpy scikit-learn

```




