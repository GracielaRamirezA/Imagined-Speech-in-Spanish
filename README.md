
# Imagined Speech in Spanish: EEG Dataset Acquisition Protocol and Baseline Classification Results.

**Manuscript ID:** IEEE LATAM Submission ID: 10609  
**Authors:**
Luis-Raul Sigala-Gonzalez<sup>a</sup>, Graciela Ramirez-Alonso<sup>a</sup>, Juan A. Ramirez-Quintana<sup>b</sup>, Fernando Martinez-Reyes<sup>a</sup>, David R. Lopez-Flores<sup>b</sup>  

<sup>a</sup> Universidad Autónoma de Chihuahua, Facultad de Ingeniería, Chihuahua, México  
<sup>b</sup> Tecnológico Nacional de México/Instituto Tecnológico de Chihuahua, Chihuahua, México

## Graphical Abstract
<img src='GraphicalAbstract.png' width='1000'>

## Codes

This repository contains the Python scripts, Jupyter notebooks, GUI files, and audio stimuli used for EEG data acquisition, signal processing, baseline classification, ablation experiments, channel importance analysis, and statistical analysis presented in the manuscript.

| File / Folder | Purpose | Description |
|---|---|---|
| **Dataset** | EEG dataset | Contains the raw and processed EEG recordings used in the study. Due to its size, the dataset is hosted externally on Google Drive. **[Download dataset] https://drive.google.com/drive/folders/1EhBOtrhZm8Pm5RhiFVje-4-kN4U0ywpR?usp=sharing** |
| `Audios/` | Experimental stimuli | Contains the audio stimuli used by the graphical user interface (GUI) during the EEG acquisition protocol. |
| `PantallaInicial.ui` | GUI | Defines the initial graphical user interface used by the EEG acquisition application. |
| `PantallaSujeto.ui` | GUI | Defines the graphical interface presented to participants during the EEG acquisition protocol. |
| `experimentoV2.py` | EEG acquisition | Controls EEG signal acquisition, communication with the OpenBCI hardware, experimental recording sessions, and storage of raw EEG recordings. |
| `Processing_and_Segmentation.py` | Preprocessing and segmentation | Performs EEG preprocessing, filtering, segmentation, and data organization for subsequent classification tasks. |
| `transformer_hi.py` | Baseline classification | Performs training, validation, and testing of the Transformer-based baseline model using the processed EEG dataset. |
| `Ablationstudy.py` | Ablation study | Performs ablation experiments to evaluate the contribution of different components to classification performance. |
| `EEG_importance.ipynb` | Channel importance analysis | Performs channel-wise ablation by systematically removing individual EEG channels and measuring the resulting variation in classification accuracy to estimate channel importance. |
| `EEG_Wilcoxon.ipynb` | Statistical analysis | Performs statistical comparisons of the experimental results using the Wilcoxon signed-rank test. |
| `SPEARMAN_EEG.ipynb` | Statistical analysis | Performs Spearman correlation analysis on the EEG experimental results. |

### General Workflow

The recommended workflow is:

1. **EEG Acquisition:** Run `experimentoV2.py` to conduct the experimental protocol and acquire the raw EEG signals using the OpenBCI hardware.
2. 
3. **Preprocessing and Segmentation:** Download the raw EEG dataset from the Google Drive link provided in the table above and place the `.npz` files in the same directory as `Processing_and_Segmentation.py`. Then, run `Processing_and_Segmentation.py` to preprocess, filter, segment, and organize the EEG recordings for subsequent classification.

4. **Baseline Classification:** Run `transformer_hi.py` to train, validate, and test the Transformer-based baseline model using the processed EEG dataset.

5. **Ablation Study:** Run `Ablationstudy.py` to perform the ablation experiments reported in the manuscript.

6. **Channel Importance Analysis:** Run `EEG_importance.py` to perform the channel-wise ablation analysis and estimate the contribution of individual EEG channels to classification performance.

7. **Statistical Analysis:** Use `EEG_Wilcoxon.ipynb` and `SPEARMAN_EEG.ipynb` to perform the statistical analyses reported in the manuscript.

> **Note:** The required dataset files must be located in the same directory as the corresponding script before execution.

### Transformer-Based Baseline

The Transformer implementation used as the baseline classifier is based on the following work:

> I. Gallo and S. Corchs, "Thinking is Like Processing a Sequence of Spatial and Temporal Words," in *2024 International Joint Conference on Neural Networks (IJCNN)*, IEEE, 2024.


## Citation
If you use this code, please cite:

Sigala-Gonzalez, L.R., Ramirez-Alonso, G., Ramirez-Quintana, J.A., Martinez-Reyes, F., Lopez-Flores, D.R. (2026). 
Imagined Speech in Spanish: EEG Dataset Acquisition Protocol and Baseline Classification Results.  IEEE Latin America Transactions, ID: 10609.
## License

This repository is intended for academic and research purposes only.

## Dataset 
The dataset was developed with the participation of the following team members:

Student Participants:

**MI. Luis Raúl Sigala González**, UACH Faculty of Engineering.
**Alan Hernández Galván**, UACH Faculty of Medicine and Biomedical Sciences.

Principal Investigators:

**Dr. Graciela María de Jesús Ramírez Alonso**, UACH Faculty of Engineering.  
**Dr. Javier Camarillo Cisneros**, UACH Faculty of Medicine and Biomedical Sciences.  
**Dr. Abimael Guzmán Pando**, UACH Faculty of Medicine and Biomedical Sciences.  
**Dr. Juan Alberto Ramírez Quintana**, Instituto Tecnológico de Chihuahua, Tecnológico Nacional de México.  
**Dr. David Ricardo López Flores**, Instituto Tecnológico de Chihuahua, Tecnológico Nacional de México.  
