# Titanic-Dashboard
# 🚢 Titanic Survival Analysis Dashboard

An interactive data visualization dashboard analyzing Titanic passenger survival patterns using Python, Dash, and Plotly.

![Dashboard Preview](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Dash](https://img.shields.io/badge/Dash-2.14.2-purple)

## 🎯 Live Demo

**[View Live Dashboard →](YOUR_RENDER_URL_HERE)**

## 📊 Features

- **11+ Interactive Visualizations**
  - Pie charts, bar charts, histograms
  - Box plots, scatter plots, heatmaps
  - Correlation matrices
  
- **Real-time Filtering**
  - Filter by passenger class (1st, 2nd, 3rd)
  - Filter by gender (male, female)
  - All charts update instantly
  
- **Statistical Analysis**
  - Survival rates by demographics
  - Age and fare distributions
  - Multi-dimensional correlations
  
- **Professional UI**
  - Responsive design
  - Clean, modern interface
  - Mobile-friendly

## 🔍 Key Insights

Based on the analysis of 418 passengers:

1. **Gender = Survival**: 100% female survival vs 0% male (in this dataset)
2. **Class Matters**: 1st class had 46.7% survival vs 33.0% for 3rd class
3. **Family Size Impact**: Small families (2-4) had 52.4% survival (highest)
4. **Children Protected**: 48.0% survival for children vs 37.5% for adults
5. **Wealth = Safety**: High fare passengers had 1.7× better survival odds

## 💻 Technologies Used

- **Python 3.8+**
- **Dash 2.14.2** - Web framework
- **Plotly 5.18.0** - Interactive visualizations
- **Pandas 2.1.4** - Data manipulation
- **Gunicorn 21.2.0** - Production server

## 🚀 Quick Start

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/abdosami1225/titanic-dashboard.git
cd titanic-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the dashboard**
```bash
python app.py
```

4. **Open browser**
```
http://127.0.0.1:8050/
```

## 📁 Project Structure

```
titanic-dashboard/
│
├── app.py                    # Main dashboard application
├── Titanic.csv               # Dataset
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
└── README.md                 # This file
```

## 🌐 Deployment

This dashboard is deployed on Render (free tier).

### Deploy Your Own

1. Fork this repository
2. Sign up at [render.com](https://render.com)
3. Connect your GitHub account
4. Create new Web Service
5. Select this repository
6. Deploy!

## 📊 Dataset Information

- **Source**: Titanic passenger manifest
- **Size**: 418 passengers
- **Features**: 12 variables including Age, Class, Fare, Survival status
- **Time Period**: April 15, 1912

## 🎨 Visualizations

1. **Overall Survival Rate** (Pie Chart)
2. **Survival by Gender** (Bar Chart)
3. **Survival by Class** (Bar Chart)
4. **Age Distribution** (Histogram)
5. **Fare Distribution** (Histogram)
6. **Age vs Fare** (Scatter Plot)
7. **Survival Rate Heatmap** (Gender × Class)
8. **Family Size Analysis** (Bar Chart)
9. **Correlation Matrix** (Heatmap)

## 🔧 Configuration

To modify the dashboard:

1. Edit `app.py` for layout changes
2. Modify callback functions for interactivity
3. Update color schemes in the color_discrete_map
4. Add new visualizations in the layout section

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Abdelrahman Samy**
- Portfolio: https://abdelrahman-samy-portfol-apbsehk.gamma.site/
- LinkedIn: www.linkedin.com/in/abdelrahman-samy-423773251
- Upwork: [upwork.com/freelancers/~yourprofile](https://upwork.com/freelancers/~yourprofile)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show Your Support

Give a ⭐ if this project helped you!

## 📧 Contact

Questions? Reach out at your.email@example.com

---

**Built with ❤️ using Python, Dash, and Plotly**
