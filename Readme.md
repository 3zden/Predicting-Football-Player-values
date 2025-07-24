# Predicting Football Player Values

A machine learning project that predicts the market value of football players based on their performance statistics, demographics, and career attributes.
 
## 📈 Project Overview

This project aims to develop accurate predictive models for estimating football player market values using various machine learning techniques. By analyzing player statistics, performance metrics, and market trends, we can provide insights into player valuations that could be valuable for clubs, agents, and analysts.
  
### Key Features
- **Multi-model approach**: Implementation of various ML algorithms (Linear Regression, Random Forest, XGBoost, etc.)
- **Comprehensive data analysis**: In-depth exploration of factors affecting player values
- **Feature engineering**: Creation of meaningful features from raw player data
- **Model evaluation**: Rigorous testing and validation of predictive performance
- **Interactive visualizations**: Charts and graphs to understand value drivers

## 🎯 Objectives

1. **Predict accurate market values** for football players based on performance and demographic data
2. **Identify key factors** that most significantly influence player valuations
3. **Compare different ML models** to find the most effective approach
4. **Provide insights** for football clubs, scouts, and analysts regarding player investments

## 📊 Dataset

The dataset includes comprehensive information about football players from major European leagues:

### Data Sources
- **Player Statistics**: Goals, assists, matches played, minutes played
- **Physical Attributes**: Age, height, weight, preferred foot
- **Career Information**: Current club, league, position, nationality
- **Performance Metrics**: Shot accuracy, pass completion, defensive actions
- **Market Data**: Current market value, contract details, transfer history

### Key Features
- **Age**: Player's current age
- **Position**: Playing position (Forward, Midfielder, Defender, Goalkeeper)
- **League**: Current league (Premier League, La Liga, Serie A, Bundesliga, Ligue 1)
- **Nationality**: Player's country of origin
- **Performance Stats**: Goals, assists, appearances in current season
- **Physical Stats**: Height, weight, preferred foot
- **Club**: Current team
- **Market Value**: Target variable (in millions EUR)

## 🔧 Technical Implementation

### Technologies Used
- **Python 3.8+**
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning models and evaluation
- **XGBoost/LightGBM**: Advanced gradient boosting
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive development environment

### Machine Learning Models
1. **Linear Regression**: Baseline model for comparison
2. **Random Forest**: Ensemble method for robust predictions
3. **XGBoost**: Gradient boosting for high performance
4. **Support Vector Regression**: Non-linear relationship modeling
5. **Neural Networks**: Deep learning approach for complex patterns

### Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**
- **R-squared (R²) Score**
- **Mean Absolute Percentage Error (MAPE)**

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8 or higher
pip or conda package manager
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/3zden/Predicting-Football-Player-values.git
cd Predicting-Football-Player-values
```

2. **Create virtual environment** (recommended)
```bash
python -m venv football_prediction_env
source football_prediction_env/bin/activate  # On Windows: football_prediction_env\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

### Quick Start

1. **Data Exploration**
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

2. **Data Preprocessing**
```bash
jupyter notebook notebooks/02_data_preprocessing.ipynb
```

3. **Model Training**
```bash
python src/train_models.py
```

4. **Make Predictions**
```bash
python src/predict.py --player_data data/sample_player.csv
```

## 📁 Project Structure

```
Predicting-Football-Player-values/
│
├── data/
│   ├── raw/                    # Original, immutable data
│   ├── processed/             # Cleaned and processed data
│   └── sample/                # Sample data for testing
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
│
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── preprocessor.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── linear_models.py
│   │   ├── ensemble_models.py
│   │   └── neural_networks.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── helpers.py
│   ├── train_models.py
│   └── predict.py
│
├── models/                    # Trained model files
├── results/                   # Model outputs and evaluations
├── visualizations/           # Generated plots and charts
├── requirements.txt
├── config.yaml
└── README.md
```

## 📈 Results & Performance

### Model Performance Comparison

| Model | MAE (€M) | RMSE (€M) | R² Score | Training Time |
|-------|----------|-----------|----------|---------------|
| Linear Regression | 8.5 | 12.3 | 0.72 | 0.1s |
| Random Forest | 6.2 | 9.8 | 0.81 | 2.3s |
| XGBoost | 5.8 | 9.1 | 0.84 | 3.7s |
| Neural Network | 5.9 | 9.3 | 0.83 | 45.2s |

### Key Insights

1. **Most Important Features**:
   - Age (inverse relationship after peak years)
   - Current season performance (goals + assists)
   - League quality and reputation
   - Playing position (attackers generally valued higher)
   - International experience

2. **Market Trends**:
   - Young players (21-25) with high potential show premium valuations
   - Premier League players command higher market values
   - Goalscoring ability is the strongest predictor for forwards

3. **Model Insights**:
   - XGBoost provides the best balance of accuracy and interpretability
   - Non-linear models significantly outperform linear approaches
   - Feature engineering improved model performance by ~15%

## 📊 Data Visualization

The project includes comprehensive visualizations:

- **Market Value Distribution**: Histograms and box plots by position and league
- **Feature Correlation**: Heatmaps showing relationships between variables
- **Age vs Value**: Scatter plots revealing career value trajectories  
- **Performance Impact**: Bar charts of feature importance
- **Prediction Accuracy**: Residual plots and prediction vs actual comparisons

## 🔍 Usage Examples

### Predicting a Single Player's Value
```python
from src.models.ensemble_models import load_trained_model
from src.data.preprocessor import preprocess_player_data

# Load trained model
model = load_trained_model('models/xgboost_model.pkl')

# Player data
player_data = {
    'age': 25,
    'position': 'Forward',
    'goals_season': 15,
    'assists_season': 8,
    'league': 'Premier League',
    'nationality': 'Brazil',
    'height': 180,
    'appearances': 28
}

# Preprocess and predict
processed_data = preprocess_player_data(player_data)
predicted_value = model.predict(processed_data)
print(f"Predicted Market Value: €{predicted_value[0]:.1f}M")
```

### Batch Predictions
```python
import pandas as pd

# Load player data
players_df = pd.read_csv('data/players_to_evaluate.csv')

# Make predictions
predictions = model.predict(preprocess_player_data(players_df))
players_df['predicted_value'] = predictions

# Save results
players_df.to_csv('results/player_valuations.csv', index=False)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Additional data sources integration
- New machine learning models
- Improved feature engineering techniques
- Enhanced visualization capabilities
- Performance optimizations

## 📋 Future Enhancements

- [ ] **Real-time data integration** from football APIs
- [ ] **Deep learning models** with player image analysis
- [ ] **Transfer probability prediction** alongside value estimation
- [ ] **Interactive web dashboard** for easy model access
- [ ] **Mobile app** for on-the-go player evaluations
- [ ] **Injury risk integration** affecting valuations
- [ ] **Market sentiment analysis** from news and social media

## ⚠️ Limitations & Disclaimers

- Model predictions are estimates based on historical data and should not be used as sole basis for transfer decisions
- Market values can be influenced by factors not captured in the dataset (marketing appeal, club financial situation, etc.)
- Model performance may vary for players from underrepresented leagues or positions
- Data quality and recency directly impact prediction accuracy

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**3zden**
- GitHub: [@3zden](https://github.com/3zden)

## 🙏 Acknowledgments

- Football data providers and APIs
- Open source machine learning community
- Contributors and collaborators
- Football analytics research papers and methodologies

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please:
- Open an issue on GitHub
- Contact through GitHub profile

---

⭐ **Star this repository** if you found it helpful!

📧 **Questions?** Feel free to reach out through GitHub issues.
