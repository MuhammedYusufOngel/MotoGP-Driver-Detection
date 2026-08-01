# MotoGP Driver Detection

This project is an advanced computer vision system designed to automatically detect and identify MotoGP drivers from video feeds. Leveraging the YOLOv8 object detection architecture, the system is capable of performing inference on pre-recorded race footage as well as real-time video streams.

## About the Project

The primary objective of this project is to create a reliable and high-performance object detection model tailored for the fast-paced environment of MotoGP racing. Accurately tracking and identifying drivers during a race can be challenging due to high speeds and motion blur. This project addresses the need for automated race analysis by providing a complete pipeline—from dataset generation and preprocessing to model training and real-time inference—allowing for continuous tracking of drivers via a virtual camera setup or video files.

## Features

* **Automated Dataset Generation (`divide_frame.py`)**: Extracts individual frames from race videos based on the video's frames-per-second (FPS), facilitating the creation of custom datasets.
* **Dataset Cleaning (`clear.py`)**: Automatically scans the dataset directory to identify and remove unlabeled images (images without a corresponding `.json` label file), ensuring dataset integrity before training.
* **Dataset Label Analysis (`label_count.py`)**: Parses JSON label files to count and display the frequency of each driver label, which helps in balancing the dataset.
* **Model Training (`train.py`)**: Fine-tunes a pre-trained YOLOv8 model on the custom MotoGP dataset, applying various data augmentation techniques to improve robustness.
* **Pre-recorded Video Inference (`run.py`)**: Processes existing MP4 video files through the trained model and saves the annotated outputs.
* **Real-time Live Inference (`obs_catch_video.py`)**: Connects to an OBS Virtual Camera stream to perform live object detection, rendering the annotated frames in a dedicated OpenCV window.

## Technologies Used

* **Python** — The core programming language used for scripting the entire pipeline.
* **Ultralytics YOLOv8** — The deep learning framework utilized for training the object detection model and performing inference.
* **OpenCV (cv2)** — Used for video capture, frame extraction, image processing, and real-time visualization.
* **JSON** — Used as the format for storing and parsing dataset bounding box labels.
* **OBS Studio (Virtual Camera)** — Utilized as the source for the live video feed during real-time inference.

## Project Structure

```text
Project/
├── clear.py                  # Script to remove unlabeled images from the dataset
├── divide_frame.py           # Script to extract frames from video files
├── label_count.py            # Utility to count the distribution of labels in the JSON files
├── obs_catch_video.py        # Real-time inference script using OBS Virtual Camera
├── run.py                    # Script to perform inference on pre-recorded video files
├── train.py                  # Model training script with YOLOv8 configurations
├── yolov8n.pt                # Base YOLOv8 Nano model weights used for transfer learning
├── dataset_final.zip         # The finalized dataset used for training
├── dataset_2026_mugello.zip  # Extracted frame dataset from the Mugello race
├── train/                    # Directory containing the YOLO training outputs and custom model weights
└── runs/                     # Directory for storing YOLOv8 inference outputs
```

## Technical Details

The project utilizes the **YOLOv8 Nano (yolov8n.pt)** model architecture due to its balance between detection accuracy and inference speed, which is critical for processing fast-moving subjects like MotoGP bikes in real-time. 

**Data Augmentation & Training:**
In `train.py`, the model is trained over 50 epochs on a custom dataset (`dataset_final/YOLODataset/dataset.yaml`). To enhance the model's ability to generalize and handle the dynamic conditions of a racetrack, several data augmentation hyperparameters are explicitly defined:
* `degrees=10.0` and `scale=0.5`: Applies rotation and scaling to simulate different camera angles and distances.
* `hsv_h=0.015, hsv_s=0.7, hsv_v=0.4`: Modifies the image's hue, saturation, and value to mimic varying lighting and weather conditions.
* `perspective=0.001`: Simulates 3D perspective changes.
* `fliplr=0.5` and `mosaic=0.5`: Flips images horizontally and combines multiple images into a single mosaic, improving the model's ability to detect objects in complex, occluded scenes.

**Inference Pipeline:**
The system supports two modes of inference:
1. **Static Video Analysis (`run.py`)**: Loads the best weights (`best.pt`) from the training output and processes high-resolution video using a high confidence threshold (`conf=0.8`) to minimize false positives.
2. **Dynamic Live Analysis (`obs_catch_video.py`)**: Uses `cv2.VideoCapture(1)` to hook into a virtual camera feed. The frames are continuously passed to the YOLO model with `stream=True` to optimize memory usage during continuous execution.

**Dataset Management:**
Labels are managed in JSON format. The project ensures data quality programmatically: `label_count.py` checks class distribution via the 'shapes' array, and `clear.py` maintains parity between images and annotation files by deleting orphan images.

## Setup and Execution

1. **Environment Setup**
   Ensure Python is installed on your system. Install the required dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```

2. **Preparing the Dataset**
   * Extract video frames using `python divide_frame.py`.
   * Label the extracted frames (using an external labeling tool) and save the labels as JSON files in the same directory.
   * Clean the dataset of any unlabeled images by running `python clear.py`.
   * Check your label distribution with `python label_count.py`.
   * Format your dataset according to the YOLO format.

3. **Training the Model**
   Run the training script to generate your custom weights:
   ```bash
   python train.py
   ```
   The best weights will be saved to `./train/weights/best.pt`.

4. **Running Inference**
   * For pre-recorded video: Place your video in the `videos` folder and execute `python run.py`.
   * For live camera feed: Ensure your OBS Virtual Camera is running and execute `python obs_catch_video.py`.

## Usage

Once the environment is set up and the model is trained, the user can utilize the scripts depending on their specific needs. To create a new dataset from a race, the user modifies the video path in `divide_frame.py` and runs it. After manual labeling, `clear.py` and `label_count.py` can be used to validate the data. Finally, the user can either feed a race replay into `run.py` to obtain an annotated video file or use `obs_catch_video.py` alongside OBS Studio to perform real-time tracking on a live broadcast.

## Project Visuals or Demo

[![Project Demonstration Video](./gifs/motogp_driver_detection.gif)](https://youtu.be/mHgMHMhNGAE)

## Development Process

During the development process of this project, AI-supported tools were utilized for code suggestions, error analysis, technical research, and accelerating the development process. The project architecture, feature determination, integrations, testing, and final technical decisions were evaluated and implemented by the developer.

## Future Improvements

* Integration of a deep SORT or ByteTrack algorithm to assign persistent IDs to drivers across consecutive frames.
* Automatic calculation of speed and trajectory estimation based on bounding box movement over time.
* Exporting detection data (coordinates and timestamps) to a CSV format for further statistical analysis.
* Creating a graphical user interface (GUI) to easily select video sources and adjust confidence thresholds without modifying the source code.

## Developer

* **Developer:** Muhammed Yusuf Öngel
* **GitHub:** [https://github.com/MuhammedYusufOngel](https://github.com/MuhammedYusufOngel)
* **LinkedIn:** [https://www.linkedin.com/in/muhammed-yusuf-öngel-56a399302/](https://www.linkedin.com/in/muhammed-yusuf-öngel-56a399302/)
* **Portfolio:** [https://muhammedyusufongel.github.io](https://muhammedyusufongel.github.io)
