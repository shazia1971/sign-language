
## Installation

### Prerequisites
- Python 3.11 
- Flask
- TensorFlow
- Other dependencies listed in `requirements.txt`

### Setup
1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/sign-language-project.git
    cd sign-language-project
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the pre-trained model**:
    Place the `sign_language_model.keras` file in the `model/` directory.

## Usage
1. **Run the Flask application**:
    ```sh
    python app.py
    ```

2. **Open the application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Start Camera**:
    Start the camera and perform a sign language gesture to get the prediction.

## Training the Model
The CNN model was trained using the [Sign Language MNIST dataset](https://www.kaggle.com/datasets/datamunge/sign-language-mnist). The training process involved:
- **Data Preprocessing**: Normalizing images and augmenting the dataset.
- **Model Architecture**: Building a CNN with multiple convolutional and dense layers.
- **Training**: Using TensorFlow to train the model.

You can retrain the model using the `train_model.py` script located in the `model/` directory. The training script and dataset preprocessing script can be found in the `model/` directory.

## Results
The model achieves an accuracy of 98% on the test set. Below are some example results:

| Gesture | Prediction |
|---------|------------|
| ![A](path/to/sample_a.png) | A |
| ![B](path/to/sample_b.png) | B |

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.



## Acknowledgments
- [Sign Language MNIST dataset](https://www.kaggle.com/datasets/datamunge/sign-language-mnist)
- [Any other resources or inspirations you used]
