
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

# Nettoyage plus robuste
df = df.dropna(subset=['prix_moyen', 'rating', 'nb_notes'])
df = df[df['prix_moyen'] > 0]

# Features / Target
X = df[['rating', 'nb_notes', 'pop_totale', 'zone_paris', 'arrondissement', 'main_category']]
y = np.log1p(df['prix_moyen'])  # transformation log pour mieux prédire les prix

# Colonnes
num_features = ['rating', 'nb_notes', 'pop_totale']
cat_features = ['zone_paris', 'arrondissement', 'main_category']

# Préprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', min_frequency=10), cat_features)
    ]
)

# Modèle plus performant que RandomForest pour ce type de données
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
y_pred_log = grid.predict(X_test)
y_pred = np.expm1(y_pred_log)
y_test_real = np.expm1(y_test)

# Métriques
rmse = np.sqrt(mean_squared_error(y_test_real, y_pred))
r2 = r2_score(y_test_real, y_pred)

print(" PRÉDICTION DU PRIX (MODÈLE AMÉLIORÉ)")
print("Meilleurs paramètres :", grid.best_params_)
print("RMSE :", rmse)
print("R²   :", r2)

# Visualisation
plt.figure(figsize=(7,7))
plt.scatter(y_test_real, y_pred, alpha=0.6)
plt.plot([y_test_real.min(), y_test_real.max()], 
         [y_test_real.min(), y_test_real.max()], 'r--')
plt.xlabel("Prix réel")
plt.ylabel("Prix prédit")
plt.title("Comparaison Prix réel vs Prix prédit (modèle amélioré)")
plt.show()
