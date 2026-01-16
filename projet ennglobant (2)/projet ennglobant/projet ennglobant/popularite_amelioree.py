
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor

# =========================
# Chargement des données
# =========================
df = pd.read_csv('projet ennglobant/restaurants_paris_sql_ready.csv')

# Variable cible : popularité (log du nombre de notes)
df = df.dropna(subset=['prix_moyen', 'rating', 'nb_notes', 'pop_totale', 'arrondissement', 'zone_paris'])
df = df[df['nb_notes'] >= 0]
df['log_reviews'] = np.log1p(df['nb_notes'])

# Features / Target
X = df[['prix_moyen', 'rating', 'pop_totale', 'arrondissement', 'zone_paris']]
y = df['log_reviews']

# Colonnes
num_features = ['prix_moyen', 'rating', 'pop_totale']
cat_features = ['arrondissement', 'zone_paris']

# Préprocessing amélioré
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', min_frequency=10), cat_features)
    ]
)

# Modèle plus performant
gbr = GradientBoostingRegressor(random_state=42)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', gbr)
])

# Hyperparamètres
param_grid = {
    'model__n_estimators': [200, 400],
    'model__learning_rate': [0.05, 0.1],
    'model__max_depth': [3, 5]
}

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# GridSearch
grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='r2',
    n_jobs=-1
)

grid.fit(X_train, y_train)

# Prédictions
y_pred = grid.predict(X_test)

# Métriques
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("📊 PRÉDICTION DE LA POPULARITÉ (MODÈLE AMÉLIORÉ)")
print("Meilleurs paramètres :", grid.best_params_)
print("RMSE :", rmse)
print("R²   :", r2)

# Visualisation
plt.figure(figsize=(7,7))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Log(Nb Notes) réel")
plt.ylabel("Log(Nb Notes) prédit")
plt.title("Comparaison Log(Nb Notes) réel vs prédit (modèle amélioré)")
plt.show()
