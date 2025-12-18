import databloom
import numpy as np

print("🌸 Test de la bibliothèque DataBloom...")

# --- 1. Test du Line Chart (Matplotlib) ---
print("1. Génération du Line Chart...")
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.1, 50) + 2

databloom.styled_line(
    x=x, 
    y=y, 
    title="DataBloom Line: Évolution du Signal",
    xlabel="Temps (s)",
    ylabel="Amplitude"
)

# --- 2. Test du Bar Chart (Seaborn) ---
print("2. Génération du Bar Chart...")
categories = ['Marketing', 'R&D', 'Sales', 'HR', 'IT']
values = [45, 80, 65, 30, 90]

databloom.styled_bar(
    categories=categories,
    values=values,
    title="DataBloom Bar: Budget par Département",
    xlabel="Département",
    ylabel="Budget (k€)"
)

# --- 3. Test du Scatter Plot (Seaborn avec catégories) ---
print("3. Génération du Scatter Plot...")
# Génération de données aléatoires
n = 50
x_scatter = np.random.rand(n) * 100
y_scatter = x_scatter * 0.5 + np.random.rand(n) * 20
# Assignation aléatoire de catégories pour tester la palette de couleurs
cats = np.random.choice(['Groupe A', 'Groupe B', 'Groupe C'], n)

databloom.styled_scatter(
    x=x_scatter,
    y=y_scatter,
    category=cats,
    title="DataBloom Scatter: Analyse de Corrélation",
    xlabel="Investissement",
    ylabel="Retour (ROI)"
)

# --- 4. Test du Bubble Chart (Matplotlib) ---
print("4. Génération du Bubble Chart...")
x_bub = [10, 20, 30, 40, 50]
y_bub = [25, 40, 35, 60, 45]
sizes = [30, 150, 80, 200, 100]  # Tailles variées pour l'effet "Bulle"

databloom.styled_bubble(
    x=x_bub,
    y=y_bub,
    sizes=sizes,
    title="DataBloom Bubble: Parts de Marché",
    xlabel="Année",
    ylabel="Volume"
)

# --- 5. Test du Stacked Chart (Altair) ---
print("5. Génération du Stacked Chart (Altair)...")
print("   -> Ce graphique doit s'ouvrir dans votre navigateur.")

# Données structurées en dictionnaire
data_empilee = {
    "Smartphone": [120, 135, 150, 170],
    "Laptop":     [80, 90, 85, 95],
    "Tablette":   [40, 35, 30, 25],
    "Montre":     [10, 25, 40, 60],
    "Autre":      [5, 5, 10, 15]
}
annees = ['2022', '2023', '2024', '2025']

databloom.styled_stacked(
    categories=annees,
    data_dict=data_empilee,
    title="DataBloom Stacked: Ventes par Catégorie",
    xlabel="Année",
    ylabel="Unités vendues"
)

print("✅ Tous les tests sont terminés !")