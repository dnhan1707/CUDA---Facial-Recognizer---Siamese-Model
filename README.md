# DeepFace Recognition with TensorFlow & GPU Acceleration 🚀

A real-time facial recognition system built with TensorFlow and OpenCV, optimized to leverage NVIDIA GPU acceleration through CUDA and cuDNN. This project demonstrates the performance gains and practical implementation of deep learning on edge devices with GPU support.

## 🔍 Project Overview

This project uses a triplet loss-based deep learning model to learn facial embeddings and identify individuals with high accuracy. Designed to be GPU-efficient and scalable, it showcases the power of NVIDIA's CUDA platform when integrated with TensorFlow.

### ✅ Key Features

- ✅ End-to-end face recognition pipeline using deep CNNs  
- ✅ Real-time image collection and preprocessing using OpenCV  
- ✅ TensorFlow GPU configuration with CUDA/cuDNN  
- ✅ Triplet loss function for better face embedding separation  
- ✅ Modular, reproducible code ready for experimentation

## ⚙️ Tech Stack

- **TensorFlow 2.x**
- **OpenCV**
- **CUDA Toolkit (11.2+)**
- **cuDNN**
- **Python 3.9+**
- **NVIDIA RTX 3050 (or compatible GPU)**

---

## 🚀 GPU Optimization

This project verifies and configures GPU usage explicitly:
- Checks for GPU availability via `tf.config.list_physical_devices('GPU')`
- Enables memory growth to avoid CUDA OOM errors
- Falls back gracefully to CPU if no GPU is found

> ✅ **Performance boost:** Training time reduced from **9 hours to 3 hours** on an NVIDIA RTX 3050

---

## 🖼️ Dataset

Uses the **LFW (Labeled Faces in the Wild)** dataset for face classification and verification. You can replace it with any personal dataset by placing images into:

