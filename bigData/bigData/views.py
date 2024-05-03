from django.shortcuts import render
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def home(request):
    return render(request, 'home.html')

def prediction(request):
    return render(request, 'prediction.html')

def result(request):
    return render(request, "prediction.html")