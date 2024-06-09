# API Klasifikasi Burung

Repositori ini berisi aplikasi web berbasis FastAPI untuk mengklasifikasikan spesies burung menggunakan model `dennisjooo/Birds-Classifier-EfficientNetB2`. Aplikasi ini menerima gambar sebagai input dan mengembalikan prediksi spesies burung.

## Model: dennisjooo/Birds-Classifier-EfficientNetB2

Model yang digunakan dalam proyek ini adalah `dennisjooo/Birds-Classifier-EfficientNetB2`, yaitu model EfficientNetB2 yang telah dilatih ulang untuk klasifikasi spesies burung. Model ini disimpan dalam format ONNX (Open Neural Network Exchange), yang memungkinkan interoperabilitas antara berbagai framework pembelajaran mendalam. EfficientNetB2 dikenal karena keseimbangan antara akurasi dan efisiensi, menjadikannya cocok untuk aplikasi waktu nyata.

## Dataset

Model ini dilatih pada dataset yang komprehensif yang berisi gambar berbagai spesies burung. Dataset ini mencakup gambar berkualitas tinggi yang dikategorikan ke dalam berbagai spesies untuk memastikan prediksi yang akurat.

### Jenis Burung

Beberapa spesies burung yang termasuk dalam dataset adalah:
- American Robin
- Bald Eagle
- Blue Jay
- Cardinal
- Chickadee
- Common Starling
- Downy Woodpecker
- House Sparrow
- Northern Flicker
- Red-winged Blackbird

## Format Input

API ini mengharapkan file gambar sebagai input. Gambar harus dalam salah satu format umum seperti JPEG, PNG, dll.

### Contoh Input

- Gambar JPEG
- Gambar PNG

## Dokumentasi API

### Endpoint Prediksi

**URL**: `https://bird-classification-mentor.1hv42jn51v17.us-east.codeengine.appdomain.cloud/predict`

**Metode**: `POST`

**Deskripsi**: Endpoint ini menerima file gambar dan mengembalikan spesies burung yang diprediksi.

#### Permintaan

- **Content-Type**: `multipart/form-data`
- **Parameter**:
  - `file`: File gambar yang akan diklasifikasikan.

#### Contoh Permintaan

```bash
curl -X POST -F "file=@D:\\images\\african firefinch.jpeg" https://bird-classification-mentor.1hv42jn51v17.us-east.codeengine.appdomain.cloud/predict
```

#### respon
> **Content-Type**: application/json

> **Parameters**:
prediction: The predicted bird species (as an integer label).

```json
{
    "prediction": [
        {
            "score": 1.0,
            "label": "BUSH TURKEY"
        },
        {
            "score": 0.3448189852414141,
            "label": "BAND TAILED GUAN"
        },
        {
            "score": 0.301270216622478,
            "label": "BANANAQUIT"
        },
        {
            "score": 0.15236842455759125,
            "label": "WILD TURKEY"
        },
        {
            "score": 0.0,
            "label": "BLACK SWAN"
        }
    ]
}
```