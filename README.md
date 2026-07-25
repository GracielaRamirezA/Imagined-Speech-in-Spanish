
# Imagined Speech in Spanish: EEG Dataset Acquisition Protocol and Baseline Classification Results.

**Manuscript ID:** IEEE LATAM Submission ID: 10609  
**Authors:**
Luis-Raul Sigala-Gonzalez<sup>a</sup>, Graciela Ramirez-Alonso<sup>a</sup>, Juan A. Ramirez-Quintana<sup>b</sup>, Fernando Martinez-Reyes<sup>a</sup>, David R. Lopez-Flores<sup>b</sup>  

<sup>a</sup> Universidad Autónoma de Chihuahua, Facultad de Ingeniería, Chihuahua, México  
<sup>b</sup> Tecnológico Nacional de México/Instituto Tecnológico de Chihuahua, Chihuahua, México

Please complete the following form to request access to the EEG dataset.

The information collected will be used only to evaluate the request and keep a record of dataset use for academic and research purposes. 
https://docs.google.com/forms/d/e/1FAIpQLSecO2j5EIbDxt-x4ZiMzjlltxislXRgFiHGTrfkpTgH6ZPNGQ/viewform?usp=header 

## Graphical Abstract
<img src='GraphicalAbstract.png' width='1000'>

## Codes

This repository contains the Python scripts, Jupyter notebooks, GUI files, and audio stimuli used for EEG data acquisition, signal processing, baseline classification, ablation experiments, and statistical analysis presented in the manuscript.

| File / Folder | Purpose | Description |
|---|---|---|
| `Audios/` | Experimental stimuli | Contains the audio stimuli used by the graphical user interface (GUI) during the EEG acquisition protocol. |
| `experimentoV2.py` | EEG acquisition | Implements the experimental procedure used for EEG data acquisition and stimulus presentation. |
| `PantallaInicial.ui` | GUI | Qt Designer file defining the initial interface of the EEG acquisition application. |
| `PantallaSujeto.ui` | GUI | Qt Designer file defining the interface presented to the participant during the experimental protocol. |
| `Processing_and_Segmentation.py` | Signal processing | Performs EEG signal preprocessing and segmentation for subsequent analysis and classification. |
| `transformer_hi.py` | Baseline classification | Implements the transformer-based baseline model used for imagined-speech EEG classification. |
| `Ablationstudy.py` | Ablation study | Performs the ablation experiments used to evaluate the contribution of the different components of the classification pipeline. |
| `EEG_Wilcoxon.ipynb` | Statistical analysis | Performs statistical comparisons using the Wilcoxon signed-rank test. |
| `SPEARMAN_EEG.ipynb` | Statistical analysis | Performs Spearman correlation analysis on the EEG experimental results. |
| `signal_quality_review.py` | Signal quality | Evaluates and reviews the quality of the acquired EEG signals. |

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
