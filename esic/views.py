from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils import timezone
from . models import Hospital
from django.db.models import Sum
from django.db.models import F

from .forms import UserLoginForm,HospitalForm,changepasswordForm


def homepage(request):
    total_beds=Hospital.objects.aggregate(Sum('total_beds'))['total_beds__sum']
    occupied_beds=Hospital.objects.aggregate(Sum('beds_occupied'))['beds_occupied__sum']
    if(total_beds==None and occupied_beds==None):
        return render(request,'esic/beds.html',{'total_beds':0,'vacant_beds':0,'occupied_beds':0})
    else:
        vacant_beds=total_beds-occupied_beds
        full_record=Hospital.objects.all()
    return render(request,'esic/beds.html',{'total_beds':total_beds,'vacant_beds':vacant_beds,'occupied_beds':occupied_beds,'full_record':full_record})

def homepage2(request):
    total_ventilators=Hospital.objects.aggregate(Sum('total_ventilators'))['total_ventilators__sum']
    occupied_ventilators=Hospital.objects.aggregate(Sum('ventilators_occupied'))['ventilators_occupied__sum']
    if(total_ventilators==None and occupied_ventilators==None):
        return render(request,'esic/ventilators.html',{'total_ventilators':0,'vacant_ventilators':0,'occupied_ventilators':0})
    else:
        vacant_ventilators=total_ventilators-occupied_ventilators
        full_record=Hospital.objects.all()
    return render(request,'esic/ventilators.html',{'total_ventilators':total_ventilators,'vacant_ventilators':vacant_ventilators,'occupied_ventilators':occupied_ventilators,'full_record':full_record})


def homepage3(request):
    total_iw=Hospital.objects.aggregate(Sum('total_iw'))['total_iw__sum']
    occupied_iw=Hospital.objects.aggregate(Sum('iw_occupied'))['iw_occupied__sum']
    if(total_iw==None and occupied_iw==None):
        return render(request,'esic/iw.html',{'total_iw':0,'vacant_iw':0,'occupied_iw':0})
    else:
        vacant_iw=total_iw-occupied_iw
        full_record=Hospital.objects.all()
    return render(request,'esic/iw.html',{'total_iw':total_iw,'vacant_iw':vacant_iw,'occupied_iw':occupied_iw,'full_record':full_record})

def adminbeds(request):
    if request.session.get('user_session',None):
        currentuser=request.session['user_session']
        record=Hospital.objects.filter(email=currentuser) 
        return render(request,'esic/admin_beds.html',{'record':record})
    else:
        return HttpResponseRedirect(reverse('login'))

def adminventilators(request):
    if request.session.get('user_session',None):
        currentuser=request.session['user_session']
        record=Hospital.objects.filter(email=currentuser) 
        return render(request,'esic/admin_ventilators.html',{'record':record})
    else:
        return HttpResponseRedirect(reverse('login'))

def adminiw(request):
    if request.session.get('user_session',None):
        currentuser=request.session['user_session']
        record=Hospital.objects.filter(email=currentuser) 
        return render(request,'esic/admin_iw.html',{'record':record})
    else:
        return HttpResponseRedirect(reverse('login'))

def bed_added(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_beds=F("total_beds") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(beds_vacant=F("beds_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminbeds'))

def bed_removed(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_beds=F("total_beds") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(beds_vacant=F("beds_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminbeds'))

def ventilator_added(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_ventilators=F("total_ventilators") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(ventilators_vacant=F("ventilators_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminventilators'))

def ventilator_removed(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_ventilators=F("total_ventilators") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(ventilators_vacant=F("ventilators_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminventilators'))

def iw_added(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_iw=F("total_iw") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(iw_vacant=F("iw_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminiw'))

def iw_removed(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(total_iw=F("total_iw") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(iw_vacant=F("iw_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminiw'))

def bed_occupied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(beds_occupied=F("beds_occupied") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(beds_vacant=F("beds_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminbeds'))

def bed_emptied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(beds_occupied=F("beds_occupied") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(beds_vacant=F("beds_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminbeds'))

def ventilator_occupied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(ventilators_occupied=F("ventilators_occupied") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(ventilators_vacant=F("ventilators_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminventilators'))

def ventilator_emptied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(ventilators_occupied=F("ventilators_occupied") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(ventilators_vacant=F("ventilators_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminventilators'))

def iw_occupied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(iw_occupied=F("iw_occupied") + 1)
    record2=Hospital.objects.filter(email=currentuser).update(iw_vacant=F("iw_vacant") - 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminiw'))

def iw_emptied(request):
    currentuser=request.session['user_session']
    record=Hospital.objects.filter(email=currentuser).update(iw_occupied=F("iw_occupied") - 1)
    record2=Hospital.objects.filter(email=currentuser).update(iw_vacant=F("iw_vacant") + 1)
    record3=Hospital.objects.filter(email=currentuser).update(last_updated=timezone.now())
    return HttpResponseRedirect(reverse('adminiw'))

def login(request):
    if request.session.get('user_session',None):
        return HttpResponseRedirect(reverse('adminbeds'))

    else:
        if request.method=='POST':
            form=UserLoginForm(request.POST)
            if form.is_valid():
                input_email=form.cleaned_data['email']
                passwd=form.cleaned_data['password']
                in_HOD=Hospital.objects.filter(email=input_email,password=passwd)
                if in_HOD.exists():
                    request.session['user_session']=input_email
                    return HttpResponseRedirect(reverse('adminbeds'))
            
                else:
                    no_account="Invalid email or Password"
                    return render(request,'esic/login.html',{'form':form,'no_account':no_account})
            else:
                field_error="Invalid Fields"
                return render(request,'esic/login.html',{'form':form,'field_error':field_error})

        else:
            form=UserLoginForm()
        return render(request,'esic/login.html',{'form':form})



def signup(request):
    if request.session.get('user_session',None):
        return HttpResponseRedirect(reverse('adminbeds'))
    else:
        if request.method=='POST':
            form=HospitalForm(request.POST)
            if form.is_valid():
                input_email=form.cleaned_data['email']
                passwd=form.cleaned_data['password']
                in_HOD=Hospital.objects.filter(email=input_email,password=passwd)
                if in_HOD.exists():    
                    no_account="Account Already Exists"
                    return render(request,'esic/signup.html',{'form':form,'no_account':no_account})
                else:
                    request.session['user_session']=input_email
                    hn=form.cleaned_data['hospital_name']
                    address=form.cleaned_data['Address']
                    gl=form.cleaned_data['GLink']
                    cn=form.cleaned_data['contact_number']
                    htype=form.cleaned_data['h_type']
                    bo=form.cleaned_data['total_beds']-form.cleaned_data['beds_vacant']
                    bv=form.cleaned_data['beds_vacant']
                    tb=form.cleaned_data['total_beds']
                    vo=form.cleaned_data['total_ventilators']-form.cleaned_data['ventilators_vacant']
                    vv=form.cleaned_data['ventilators_vacant']
                    tv=form.cleaned_data['total_ventilators']
                    io=form.cleaned_data['total_iw']-form.cleaned_data['iw_vacant']
                    iv=form.cleaned_data['iw_vacant']
                    ti=form.cleaned_data['total_iw']
                    record=Hospital(email=input_email,hospital_name=hn,Address=address,GLink=gl,contact_number=cn,h_type=htype,iw_occupied=io,iw_vacant=iv,total_iw=ti,beds_occupied=bo,beds_vacant=bv,total_beds=tb,ventilators_occupied=vo,ventilators_vacant=vv,total_ventilators=tv,last_updated=timezone.now(),password=passwd)
                    record.save()
                    return HttpResponseRedirect(reverse('adminbeds'))
            else:
                field_error="Invalid Fields"
                return render(request,'esic/signup.html',{'form':form,'field_error':field_error})

        else:
            form=HospitalForm()
        return render(request,'esic/signup.html',{'form':form})

def changepassword(request):
    if request.session.get('user_session',None):
        if request.method=='POST':
            form=changepasswordForm(request.POST)
            if form.is_valid():
                currentuser=request.session['user_session']
                current_password=form.cleaned_data['cp']
                new_password=form.cleaned_data['np']
                confirm_new_password=form.cleaned_data['cnp']
                record=Hospital.objects.filter(email=currentuser,password=current_password)
                if (record.exists() and (new_password==confirm_new_password)):
                    nrecord=Hospital.objects.filter(email=currentuser).update(password=new_password)
                    return HttpResponseRedirect(reverse('adminiw'))
                elif(record.exists()):
                    cerror="new Password and Confirmation password are not matching"
                    return render(request,'esic/change_password.html',{'form':form,'cerror':cerror})
                else:
                    perror="Wrong Password"
                    return render(request,'esic/change_password.html',{'form':form,'perror':perror})

            else:
                field_error="Invalid Fields"
                return render(request,'esic/change_password.html',{'form':form,'field_error':field_error})
        else:
            form=changepasswordForm()
        return render(request,'esic/change_password.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('homepage'))


    



def logout(request):
    try:
        del request.session['user_session']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))