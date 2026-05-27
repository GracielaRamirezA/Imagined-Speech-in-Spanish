# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:57:02 2026

@author: sigal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import welch
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from itertools import combinations

# ======================================================
# TU FUNCION ORIGINAL
# ======================================================


def sel_exp(caso, data, labels):

    objeto = {
        'Multi': {'aceptar': 0, 'cancelar': 1, 'arriba': 2, 'abajo': 3,
                  'derecha': 4, 'izquierda': 5, 'hola': 6, 'ayuda': 7,
                  'gracias': 8, 'a': 9, 'e': 10, 'i': 11, 'o': 12, 'u': 13},
    }

    if caso == 'Multi':

        X = np.vstack(data["hi"])

        Y = np.repeat(np.arange(14), data["hi"].shape[1])

    else:
        raise ValueError("Solo Multi implementado en este ejemplo")

    return X, Y


# ======================================================
# METRICAS DE CALIDAD
# ======================================================

def compute_rms(X):

    return np.sqrt(np.mean(X**2))


def compute_variance(X):

    return np.var(X)


def compute_signal_power(X):

    return np.mean(X**2)


def compute_beta_power(X, fs=120):

    beta_powers = []

    for sample in X:

        for ch in sample:

            freqs, psd = welch(
                ch,
                fs=fs,
                nperseg=min(256, len(ch))
            )

            beta_mask = (freqs >= 13) & (freqs <= 30)

            beta_power = np.sum(psd[beta_mask])

            beta_powers.append(beta_power)

    return np.mean(beta_powers)


# ======================================================
# SEPARABILIDAD FISHER
# ======================================================

def fisher_score(class1, class2):

    mu1 = np.mean(class1)
    mu2 = np.mean(class2)

    var1 = np.var(class1)
    var2 = np.var(class2)

    score = ((mu1 - mu2) ** 2) / (var1 + var2 + 1e-8)

    return score


def compute_class_separability(X, Y):
    """
    Calcula separabilidad promedio entre clases
    """

    separability_scores = []

    classes = np.unique(Y)

    # Flatten:
    # (samples, channels, time)
    # -> (samples, features)

    X_flat = X.reshape(X.shape[0], -1)

    for c1, c2 in combinations(classes, 2):

        X1 = X_flat[Y == c1]
        X2 = X_flat[Y == c2]

        score = fisher_score(X1, X2)

        separability_scores.append(score)

    return np.mean(separability_scores)


# ======================================================
# ACCURACY POR SUJETO
# ======================================================

# EJEMPLO
# CAMBIA ESTOS VALORES

subject_accuracies = {
    1: 13.36633663,
    2: 12.57425756,
    3: 11.58415842,
    4: 13.46534672,
    5: 30.87301769,
    6: 14.85294085,
    7: 12.87128735,
    8: 11.48514833,
    9: 13.66336651,
    10:	11.88118801,
    11: 13.72727213,
    12:	15.34653454,
    13:	12.27722788,
    14: 13.8613863,
    15: 16.13861351,
    16: 15.34653454
}


# ======================================================
# ANALISIS COMPLETO
# ======================================================

results = []

subjects = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for subject_num in subjects:

    print(f"Procesando sujeto {subject_num}")

    # =====================
    # CARGAR NPZ
    # =====================

    data = np.load(
        f's-{subject_num}-prepros-ASU.npz',
        allow_pickle=True
    )

    labels = data['labels']

    X, Y = sel_exp("Multi", data, labels)

    # =====================
    # METRICAS
    # =====================

    rms = compute_rms(X)

    variance = compute_variance(X)

    power = compute_signal_power(X)

    beta_power = compute_beta_power(X)

    separability = compute_class_separability(X, Y)

    accuracy = subject_accuracies[subject_num]

    # =====================
    # GUARDAR
    # =====================

    results.append({
        "subject": subject_num,
        "accuracy": accuracy,
        "rms": rms,
        "variance": variance,
        "power": power,
        "beta_power": beta_power,
        "separability": separability
    })


# ======================================================
# DATAFRAME
# ======================================================

df = pd.DataFrame(results)

print(df)


# ======================================================
# CORRELACIONES
# ======================================================

metrics = [
    "rms",
    "variance",
    "power",
    "beta_power",
    "separability"
]

print("\n================ CORRELACIONES ================\n")

for metric in metrics:

    r, p = pearsonr(
        df[metric],
        df["accuracy"]
    )

    print(f"{metric}")
    print(f"Pearson r = {r:.4f}")
    print(f"p-value = {p:.4f}")
    print()


# ======================================================
# GRAFICAS
# ======================================================

for metric in metrics:

    plt.figure(figsize=(5, 4))

    plt.scatter(
        df[metric],
        df["accuracy"]
    )

    plt.xlabel(metric)
    plt.ylabel("Accuracy")

    plt.title(f"{metric} vs Accuracy")

    plt.grid(True)

    plt.show()
