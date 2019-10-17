from django.shortcuts import render
from .models import Demo
# Create your views here.
from django.shortcuts import render , reverse
from django.http import JsonResponse , HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Demo,Country
from .serializers import SampleSerializer

msg=''
num_verified=False
ctry_matched = ''
@api_view(['GET'])
def fetch_all(request):
    if request.method=='GET':
       d = Country.objects.all()
       data={}
       for k in d:
           data[str(k.country_name)] = {"ALPHA-1-CODE": k.country_alpha_1_code , "NUM-CODE":k.country_num_code,}
       return Response(data)
@api_view(['POST'])
def fetch_items(request):
   
   global num_verified,ctry_matched,msg
   
   if request.method=='POST':
      data_received = {'num':request.data.get('NUM'),'num_pre':request.data.get('NUM_PRE'),}
      exists = search(str(data_received['num']),int(data_received['num_pre']))
      if exists:
         exist_obj = Country.objects.get(country_name=ctry_matched)
         response_data = {'EXISTS':True, 'VERIFIED':num_verified, 'CTRY':exist_obj.country_name,'PREFIX':exist_obj.phone_prefix,'ALPHA_1':exist_obj.country_alpha_1_code,'ALPHA_2':exist_obj.country_alpha_2_code,'NUM_CODE':exist_obj.country_num_code,'msg':msg,}
               
      else:
         response_data = {'EXISTS':False, 'VERIFIED':False, 'msg':msg,}

   else:
      response_data = {'ERROR':'Invalid Request Method , Expected a POST request',}

   return Response(response_data)
def checkNum(x):
    try:
        int_x=int(x)
    except ValueError:
        return False
    return True

def search(num,pre):
    global num_verified,ctry_matched , msg
    ctry_matched=''
    all_obj = Country.objects.all()
    obj_found =[]
    verified_len=0
    data_rec_ph_len=len(num)
    #check for prefix
    for ctry in all_obj:
        if pre==int(ctry.phone_prefix):
            obj_found.append(ctry)
    if obj_found!=[]:
        #check for lengths
        for obj in obj_found:
            ph_ = obj.phone_length.split()
            if ph_[0][0]=='(':
                
                if ph_[0][0:5]==num[0:5]:
                    data_rec_ph_len-=5
                    obj_found = [obj]
                    break   
        for pre in obj_found:
            ph_len=[]
            ph_ = pre.phone_length.split()
                
            if 'to' in ph_:
                ind=ph_.index('to') 
                min_=int(ph_[ind-1])
                max_=int(ph_[ind+1])
                while min_<=max_:
                    ph_len.append(min_)
                    min_+=1
            elif ',' in ph_:
                a=ph_.index(',')-1
                b=ph_.index(',')+1
                ph_len=[a,b]
            else:
                ph_len=ph_
            allowed_lengths=[]
            for k in ph_len:
                if checkNum(k):
                    allowed_lengths.append(int(k))
                    if int(k)==data_rec_ph_len:
                        temp=int(k)
                        ctry_matched = pre.country_name
                        obj_found=[]
                        break
        if ctry_matched!='':
            if len(ph_len)>2:
                if allowed_lengths[-1]>temp:
                    msg='This is not a general mobile number , but it could be a landline number'
                    num_verified=False
                    return True
                else:
                    msg="Number verified successfully"
            msg="Number verified successfully"
            num_verified = True
            return True
        else:
            msg='The phone length doesn\'t match with the related prefix'
            num_verified=False
            return False
    else:
        msg='The provided prefix or phone number does not match with the record of more than 240 codes.'
        return False
   
def Home(request):
    return render(request , 'home.html')