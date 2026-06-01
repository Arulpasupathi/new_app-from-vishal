# Car Price Prediction ML Pipeline

A complete machine learning pipeline for predicting car prices using the Cars24 dataset.

## Project Structure

```
├── 01_eda.ipynb                    # Exploratory Data Analysis
├── 02_model_testing.py             # Algorithm testing & hyperparameter tuning
├── 03_train_final_model.py         # Final model training on full dataset
├── requirements.txt                # Python dependencies
├── artifacts/                      # Trained models and artifacts
│   ├── car_price_model_latest.pkl  # Latest trained model
│   ├── model_summary.json          # Model metadata
│   ├── feature_info.json           # Feature information
│   └── feature_importance.csv      # Feature importance scores
├── .vscode/settings.json           # VS Code settings
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run EDA

Open `01_eda.ipynb` in Jupyter and run all cells to explore the dataset.

### 3. Test Models

```bash
python 02_model_testing.py
```

This script will:
- Load and preprocess the data
- Test multiple algorithms (Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting, SVR)
- Perform hyperparameter tuning on the best model
- Display performance metrics and feature importance

### 4. Train Final Model

```bash
python 03_train_final_model.py
```

This script will:
- Train the finalized model on the entire dataset
- Save the model in the `artifacts/` directory
- Generate metadata files (feature info, model summary, feature importance)

## Models Tested

1. **Linear Regression** - Baseline model
2. **Ridge Regression** - L2 regularization
3. **Lasso Regression** - L1 regularization
4. **Random Forest** - Ensemble tree-based
5. **Gradient Boosting** - Sequential ensemble (BEST)
6. **Support Vector Regression** - Non-linear regression

## Best Model

**Gradient Boosting Regressor** - Selected based on test performance

### Hyperparameters:
- n_estimators: 200
- learning_rate: 0.1
- max_depth: 5
- min_samples_split: 5

## Dataset

- **File**: `cars24-car-price-cleaned-new.csv`
- **Target**: `selling_price` (in Lakhs)
- **Features**: 17 features including km_driven, mileage, engine, max_power, age, make, model, and fuel/transmission types

## VS Code Configuration

The `.vscode/settings.json` includes:
- Auto-save disabled to prevent silent overwrites
- Git auto-refresh enabled
- Python formatting and linting configured
- Conflict-aware settings for merge operations

## Git Workflow

```bash
# Check status
git status

# Add changes
git add <files>

# Commit
git commit -m "Your message"

# View history
git log
```

## Next Steps

1. Deploy the trained model
2. Create a prediction API
3. Monitor model performance in production
4. Retrain periodically with new data

---

Created: June 1, 2026
