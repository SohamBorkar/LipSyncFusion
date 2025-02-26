# LipSyncFusion

LipSyncFusion is an end-to-end lip-sync solution that combines the power of the open-source [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) model with ElevenLabs Text-to-Speech (TTS). This project synchronizes a frontal face image with audio generated from a custom script (using the "Anika – Customer Care Agent" voice at a speech speed of 0.92) to produce a high-quality, realistic lip-synced video. Developed as part of an internship assignment, LipSyncFusion emphasizes robust model implementation, clear project structure, and excellent output quality.

## Features

- **Realistic Lip Sync:** Utilizes Wav2Lip to generate accurate and natural lip movements.
- **Custom Audio Generation:** Integrates with ElevenLabs TTS to create audio with specific voice and speed parameters.
- **Organized Structure:** Separates core model code, custom scripts, input data, and outputs for clarity and ease of maintenance.

## Prerequisites

- **Python:** 3.6 or higher
- **ffmpeg:** Required for video processing ([Install ffmpeg](https://ffmpeg.org/download.html))
  ```bash
  sudo apt-get install ffmpeg
  ```
- **Optional:** NVIDIA GPU with CUDA for accelerated inference (the project will run on CPU if no GPU is available)

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/SohamBorkar/LipSyncFusion.git
cd LipSyncFusion
```

### 2. Set Up the Virtual Environment

Create a virtual environment in the main project folder and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using the provided requirements file:
```bash
pip install -r requirements.txt
```
Alternatively, instructions for using a docker image are provided [here](https://github.com/Rudrabha/Wav2Lip/issues/175#issuecomment-864222024). Have a look at this comment and comment on the gist if you encounter any issues.

### 4. Download the Pretrained Model

Download the pretrained Wav2Lip checkpoint (e.g., `wav2lip_gan.pth`) as per the instructions in the [Wav2Lip repository](https://github.com/Rudrabha/Wav2Lip) and place it in the `Wav2Lip/checkpoints/` folder.

### 5. Face Detection Pretrained Model

The face detection pre-trained model should be downloaded to `face_detection/detection/sfd/s3fd.pth`. 
[Alternative link](https://drive.google.com/file/d/1pjG8fB8p6fFGAePqBpG-LKjp0hT-KQFj/view?usp=sharing) if the above does not work.

## Project Structure

```
LipSyncFusion/
├── Wav2Lip/                # Cloned Wav2Lip repository with core model code
│   ├── checkpoints/        # Contains pretrained model checkpoint(s)
│   ├── inference.py        # Inference script for generating lip-synced video
│   └── ... (other Wav2Lip files)
├── data/                   # Input files and generated assets
│   ├── Cleaned_Model_Image.png  # Input frontal face image
│   └── Lip_Synk_Audio.mp3         # Audio file generated via ElevenLabs TTS
├── outputs/                # Final generated lip-synced video
│   └── result_video.mp4    # Output video file
├── src/                    # Custom scripts for project integration
│   ├── generate_audio.py   # Script to generate audio using ElevenLabs TTS
│   └── run_wav2lip.py      # (Optional) Script to automate the inference process
├── venv/                   # Virtual environment folder (excluded from version control)
├── README.md               # This file
└── requirements.txt        # Combined requirements file (if applicable)
```

## Usage

### Step 1: Generate Audio with ElevenLabs TTS

1. Open the file `src/generate_audio.py` and set your ElevenLabs API key and the voice ID for "Anika – Customer Care Agent."
2. Run the script to generate the audio:
   ```bash
   python src/generate_audio.py
   ```
   This will generate an audio file (e.g., `Lip_Synk_Audio.mp3`) in the `data/` folder.

### Step 2: Generate the Lip-Synced Video

Run the Wav2Lip inference script using the generated audio and input image:
```bash
python Wav2Lip/inference.py --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth --face data/Cleaned_Model_Image.png --audio data/Lip_Synk_Audio.mp3
```
After the process completes, the output video (`result_video.mp4`) will be saved in the `outputs/` folder.

## Results

The generated results are stored in the `/outputs` folder. You can download them and view the results. Please check all outputs in the /outputs folder to see the final generated videos.

## Troubleshooting

- **File Not Found:** Verify that the paths provided to the `--face` and `--audio` arguments are correct. Adjust the paths if needed (use relative or absolute paths).
- **CUDA Warning:** If you do not have an NVIDIA GPU, the script will fall back to CPU. This warning is expected and can be ignored if you’re running on CPU.
- **Dependency Issues:** Ensure that all dependencies are correctly installed. If you encounter build errors, try installing the `wheel` package (`pip install wheel`) and verify the versions in `requirements.txt`.

## Acknowledgements

- [Wav2Lip](https://github.com/Rudrabha/Wav2Lip)
- [ElevenLabs TTS](https://elevenlabs.io/)
- Internship Assignment for Lip Sync Model Implementation

## Contact

For questions or issues, please open an issue in the repository or contact sohamborkar14@gmail.com.

