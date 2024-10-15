# DDoS Protection Model

Welcome to the **AI DDoS Protection System**! This project leverages machine learning to identify and mitigate potential DDoS attacks using various algorithms. The application features a user-friendly interface to input network parameters and predict the likelihood of a DDoS attack.

## Live Demo

You can see the live version of the application at [this URL](https://ddos.up.railway.app/).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time prediction of DDoS attacks.
- User-friendly interface for inputting network parameters.
- Visual representation of model performance metrics.

## Installation

To get started, clone this repository and install the required packages:

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
pip install -r requirements.txt
```

### Requirements

Make sure you have the following Python packages installed:

- Flask
- scikit-learn
- joblib
- flask_socketio
- pandas
- numpy
- eventlet

You can create a `requirements.txt` file with the following content:

```plaintext
Flask
scikit-learn
joblib
flask_socketio
pandas
numpy
eventlet
```

## Usage

Run the application using Gunicorn:

```bash
gunicorn -k gevent -w 1 app:app
```

Open your web browser and navigate to `http://localhost:5000` to access the app. 

### Input Parameters

You can input the following network parameters to predict the likelihood of a DDoS attack:

- **Flow Duration**
- **Source IP**
- **Source Port**
- **Destination IP**
- **Destination Port**
- **Total Forward Packets**
- **Initial Backward Window Bytes**
- **Protocol**

## Model Performance

### Gaussian Naive Bayes

- Training-set accuracy score: **81.90%**
- Model accuracy score: **81.87%**

### Random Forest Classifier

- Cross-validation accuracy scores for each fold: **[1.0, 1.0, 0.99999844, 0.99999844, 1.0]**
- Mean cross-validation accuracy: **99.9999%**
- Standard deviation: **7.66e-07**

The models were trained using various machine learning techniques to ensure high accuracy in DDoS detection.

## Dataset

The project uses a DDoS dataset sourced from Kaggle. You can download it using the following command:

```python
import kagglehub

path = kagglehub.dataset_download("devendra416/ddos-datasets")
print("Path to dataset files:", path)
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance. Thank you for checking out this.
```

