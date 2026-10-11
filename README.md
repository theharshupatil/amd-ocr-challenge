# AMD OCR Challenge

Robust OCR inference for AMD AI Challenge — Mini-Challenge 2.

## Objective

Transcribe text accurately from license plates and road signs under
challenging conditions such as blur, glare, noise, low light, and perspective
distortion.

## Strategy

1. Build a reproducible local benchmark.
2. Evaluate pretrained OCR and vision-language models.
3. Optimize preprocessing, inference, and postprocessing.
4. Measure exact-match accuracy, latency, and GPU memory.
5. Package the final system using the mandated ROCm Docker base.

## Structure

- `app/` — final inference application
- `samples/images/` — public sample images
- `samples/labels.json` — expected sample transcriptions
- `experiments/` — experiment notes and comparisons
- `models/` — optional model weights
- `scripts/` — development utilities
- `tests/` — automated tests
- `benchmark.py` — local exact-match benchmark
- `Dockerfile` — submission container

## Competition Interface

Input:
`python3 /app/app.py --input-image /path/to/image.png`

Output:
`/app/output/<input_filename>_output.json`

Supported formats: PNG, JPEG, TIFF.

Required base image:
`rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0`

The ten public examples are development samples, not the hidden evaluation set.

## Status

Initial project scaffold. OCR inference and sample extraction are pending.
