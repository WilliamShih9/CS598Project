# -*- coding: utf-8 -*-
"""ParameterCount.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lq6Ynp7CJMUVQXhMqY1QHyZCs62p4E8Z
"""

from google.colab import drive

drive.mount('/content/gdrive')

import os
print(os.getcwd())
os.chdir("/content/gdrive/My Drive/Colab Notebooks")
print(os.getcwd())

import torch

def parameters_list(model_name):
  model = torch.load(model_name)
  tensor_list = list(model.items())
  total_sum = 0
  total_sum_KSI = 0
  for layer_tensor_name, tensor in tensor_list:
      if "vattention" not in layer_tensor_name and "layer2" not in layer_tensor_name and "embedding." not in layer_tensor_name:
        total_sum = torch.numel(tensor) + total_sum
      total_sum_KSI = torch.numel(tensor) + total_sum_KSI
      print('Layer {}: {} elements, {} shape'.format(layer_tensor_name, torch.numel(tensor), tensor.size()))
  print('Number of parameters without KSI for', model_name, total_sum)
  print('Number of parameters with KSI for', model_name, total_sum_KSI)

parameters_list("CAML_model")

parameters_list("CNN_model")

parameters_list("LSTM_model")

parameters_list("LSTMattn_model")