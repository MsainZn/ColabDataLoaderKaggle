# -*- coding: utf-8 -*-
"""Competition-Loader

Automatically generated by Colaboratory.


"""

!pip install kaggle

!mkdir -p ~/.kaggle

from google.colab import files
files.upload()

!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle competitions download -c commonlit-evaluate-student-summaries

