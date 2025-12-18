import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION DU STYLE ET DES COULEURS ---

# Votre palette exacte
PASTEL_THEME = [
    '#C4A1CE',  # Violet
    '#FFC4D6',  # Rose Pâle
    '#FF96B4',  # Rose Vif
    '#B6E1FA',  # Bleu Ciel
    '#92C9FA'   # Bleu Azur
]

# Configuration globale de Seaborn
sns.set_theme(style="whitegrid")
sns.set_palette(sns.color_palette(PASTEL_THEME))

# Configuration pour Matplotlib
BG_COLOR = '#FFFFFF'
TEXT_COLOR = '#5D6D7E'
GRID_COLOR = '#EAECEE'

def _apply_matplotlib_theme(ax, title, xlabel, ylabel):
    """Applique le style 'clean' aux graphiques Matplotlib et Seaborn"""
    ax.set_title(title, fontsize=16, fontweight='bold', color=TEXT_COLOR, pad=20)
    ax.set_xlabel(xlabel, fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel(ylabel, fontsize=11, color=TEXT_COLOR)
    ax.set_facecolor(BG_COLOR)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COLOR)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(color=GRID_COLOR, linestyle='-', linewidth=1, alpha=0.6)

# --- 2. LES FONCTIONS (Mélange des bibliothèques) ---

def styled_line(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
    """
    Backend: MATPLOTLIB
    Pourquoi : Contrôle total sur les lignes et le remplissage.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Ligne Bleu Azur (index 4)
    ax.plot(x, y, color=PASTEL_THEME[4], linewidth=4, marker='o', 
            markerfacecolor='white', markeredgewidth=2, zorder=3)
    
    # Remplissage Bleu Ciel (index 3)
    ax.fill_between(x, y, color=PASTEL_THEME[3], alpha=0.3, zorder=2)
    
    _apply_matplotlib_theme(ax, title, xlabel, ylabel)
    plt.show()

def styled_bubble(x, y, sizes, title="Bubble Chart", xlabel="X", ylabel="Y"):
    """
    Backend: MATPLOTLIB + NUMPY
    Pourquoi : Matplotlib gère mieux les tailles de bulles personnalisées (sizes) que Seaborn.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Normalisation des tailles avec Numpy pour l'affichage
    scaled_sizes = np.array(sizes) * 10 
    
    # Bulles Rose Pâle (index 1) contour Rose Vif (index 2)
    ax.scatter(x, y, s=scaled_sizes, color=PASTEL_THEME[1], 
               edgecolors=PASTEL_THEME[2], linewidth=2, alpha=0.8, zorder=3)
    
    _apply_matplotlib_theme(ax, title, xlabel, ylabel)
    plt.show()

def styled_bar(categories, values, title="Bar Chart", xlabel="Category", ylabel="Value"):
    """
    Backend: SEABORN
    Pourquoi : Seaborn rend les graphiques catégoriels très simples.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Création d'un DataFrame temporaire (Seaborn adore Pandas)
    data = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Barplot avec la couleur Rose Vif (index 2)
    sns.barplot(data=data, x='Category', y='Value', ax=ax, 
                color=PASTEL_THEME[2], saturation=0.9, zorder=3)
    
    _apply_matplotlib_theme(ax, title, xlabel, ylabel)
    plt.show()

def styled_scatter(x, y, category=None, title="Scatter Plot", xlabel="X", ylabel="Y"):
    """
    Backend: SEABORN
    Pourquoi : Facile de colorer les points par catégorie automatiquement.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Si pas de catégorie, on utilise une couleur unique (Violet - index 0)
    if category is None:
        sns.scatterplot(x=x, y=y, ax=ax, s=150, color=PASTEL_THEME[0], 
                        edgecolor='white', linewidth=1.5, zorder=3)
    else:
        # Sinon, Seaborn utilise la palette PASTEL_THEME automatiquement
        sns.scatterplot(x=x, y=y, hue=category, ax=ax, s=150, 
                        palette=PASTEL_THEME, edgecolor='white', linewidth=1.5, zorder=3)
        ax.legend(frameon=False)

    _apply_matplotlib_theme(ax, title, xlabel, ylabel)
    plt.show()

def styled_stacked(categories, data_dict, title="Stacked Bar (Interactive)"):
    """
    Backend: ALTAIR
    Pourquoi : Altair excelle dans les graphiques empilés et interactifs.
    Note : Ouvre le graphique dans le navigateur par défaut.
    """
    # 1. Transformation des données pour Altair (Format Long)
    df_list = []
    for cat_label, values in data_dict.items():
        for i, val in enumerate(values):
            df_list.append({
                'Category': categories[i],
                'Group': cat_label,
                'Value': val
            })
    df = pd.DataFrame(df_list)

    # 2. Création du Chart Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Category', title='Catégorie', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Value', title='Valeur Totale'),
        color=alt.Color('Group', scale=alt.Scale(range=PASTEL_THEME), title="Légende"),
        tooltip=['Category', 'Group', 'Value'] # Bonus : Info-bulle au survol !
    ).properties(
        title=title,
        width=500,
        height=400,
        background='white'
    ).configure_title(
        fontSize=16, color=TEXT_COLOR, anchor='start'
    ).configure_axis(
        labelColor=TEXT_COLOR, titleColor=TEXT_COLOR, gridColor=GRID_COLOR
    ).configure_view(
        strokeWidth=0 # Retire la bordure du cadre
    )

    # Affichage (Altair ouvre souvent une page web ou un viewer jupyter)
    chart.show()
    # Si chart.show() ne marche pas dans votre terminal, utilisez :
    # chart.save('chart_stacked.html')
    # print("Graphique sauvegardé sous chart_stacked.html")