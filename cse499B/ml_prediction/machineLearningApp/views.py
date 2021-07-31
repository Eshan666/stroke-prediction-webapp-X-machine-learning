from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
import joblib
from django.contrib.auth import authenticate, login,logout
from machineLearningApp.models import *


# Create your views here.

def home(request):
    if request.method == "POST":
        context = {}

        age = int(request.POST.get('age'))
        hypertension = int(request.POST.get('hypertension'))
            
        heart_disease = int(request.POST.get('heart_disease'))
        glucose = int(request.POST.get('glucose'))
          
        bmi = int(request.POST.get('bmi'))
        gender = int(request.POST.get('gender'))
            
        married = int(request.POST.get('married'))
        workType = int(request.POST.get('workType'))
        residence = int(request.POST.get('residence'))
        smoking = request.POST.get('smoking')


        model = joblib.load('trained_model.joblib')
        pipeline = joblib.load('pipeline')  

        prep_data = pipeline.transform([[age,hypertension,heart_disease,glucose,bmi,gender,married,workType,residence,smoking]])
        result = model.predict(prep_data)[0]

        dataset = Dataset(patient=request.user,
         age = age,
         hypertension = hypertension,
         heartDisease = heart_disease,
         glucose = glucose,
         bmi = bmi,
         gender = gender,
         married = married,
         workType = workType,
         Residence = residence,
         smoking = smoking,
         result = result
         )

        dataset.save()

        context = {
            "result" : result
        }

        return render(request,'machineLearningApp/home.html',context)

    return render(request,'machineLearningApp/home.html')


def signInPage(request):
    
    if request.method == "POST":
        
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =  authenticate(request, username=username, password=password)
            

            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('home')
            else:
                messages.info(request,"username or password is incorrect")
   

    return render(request,'machineLearningApp/signIn.html')



def signUpPage(request):
    form =  CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form }
    return render(request,'machineLearningApp/signup.html',context)