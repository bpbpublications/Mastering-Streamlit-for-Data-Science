from surprise import Dataset, Reader, SVD
from surprise.model_selection import GridSearchCV
import joblib
import pandas as pd

df = pd.read_csv('../data/products_sales.csv')
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['User ID', 'Product', 'Rating']], reader)
param_grid = {
    'n_epochs': [5, 10, 20],  # Number of iteration of the SGD procedure
    'lr_all': [0.002, 0.005, 0.01],  # Learning rate for all parameters
    'reg_all': [0.02, 0.1, 0.4]  # Regularization term for all parameters
}

gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
gs.fit(data)

print(gs.best_params['rmse'])

algo = SVD(n_epochs=gs.best_params['rmse']['n_epochs'], lr_all=gs.best_params['rmse']['lr_all'], reg_all=gs.best_params['rmse']['reg_all'])
trainset = data.build_full_trainset()
algo.fit(trainset)

joblib_file = "recommender_model.joblib"
joblib.dump(algo, joblib_file)