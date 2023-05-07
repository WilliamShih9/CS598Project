# CS598 Project
This project is a reproduction of the results presented in the paper
* **Bai, T., Vucetic, S., Improving Medical Code Prediction from Clinical Text via Incorporating Online Knowledge Sources, The Web Conference (WWW'19), 2019.**

as well as an idea of implementing the most up to date Wikipedia articles.

## Links

- [Link to original GitHub repository](https://github.com/tiantiantu/KSI)
- [Link to original paper](https://dl.acm.org/doi/10.1145/3308558.3313485)

## Environment

I used the following Python environment for the implementation:
* Python 3.10.11
* torch==2.0.0+cu118
* numpy==1.22.4
* sklearn==1.2.2

I also used "rvest_1.0.2" with R to download the most recent Wikipedia articles from the internet. The file for this is "updatewikipedia.R". The Wikipedia articles are up to date as of May 1, 2023 with the "wikipedia_knowledge_new" file. This is about 4 years newer than the original Wikipedia file, which is "wikipedia_knowledge".

## How to Run

Before running the program, you need to apply for [MIMIC-III](https://mimic.physionet.org/gettingstarted/access/) dataset and put two files "NOTEEVENTS.csv.gz" and "DIAGNOSES_ICD.csv.gz" under the same folder of the project.

Once you get these two files, run preprocessing scripts "preprocessing0.py", "preprocessing1.py", "preprocessing2.py", and "preprocessing3.py" in order. Note that I originally implemented this on Google Colab so that so code might be modified in order to run it properly using the python files that were drived from the .ipynb files. The code to mount on Google Drive should be removed when running locally.

The .ipynb files can be found in the IPYNB folder and the .py files can be found in the PY folder. When running the code, move either all the PY files or all the IPYNB files in the same folder where "NOTEEVENTS.csv.gz", "DIAGNOSES_ICD.csv.gz", "IDList.npy", "wikipedia_knowledge", and "wikipedia_knowledge_new" is stored.

Splitting off from there, the new Wikipedia data can be implemented using "preprocessing2_new.ipy" and "preprocessing3_new.py" in order (since the "preprocessing0.py" and "preprocessing1.py" do not involve Wikipedia data at all yet).

After running three preprocessing files, you can run any of four models ("KSI_LSTM.py", "KSI_LSTMatt.py", "KSI_CNN.py", "KSI_CAML.py") to see how much improvement KSI framework brings to the specific model. Any of the four models using the new Wikipedia knowledge can be run using ("KSI_LSTM_new.py", "KSI_LSTMatt_new.py", "KSI_CNN_new.py", "KSI_CAML_new.py"). 

Finally, "Results.csv" is a copy paste from the performance numbers in the .ipynb files. "CreateTables.R" creates latex tables from the results in the "Results.csv" file.
