from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import  datetime
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import base64


####header for skintone detection


###end header



####constants

mediapath = "D:\\my_main_project\\final\\GlowStyle\\GlowStyle\\media\\"



####end constants


# Create your views here.
from myapp.models import *


def login(request):
    return render(request, "admin/login.html")

def log_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var1 = Login.objects.get(username=username, password=password)
        request.session['lid']=var1.id
        if var1.type=='admin':
            return redirect('/myapp/home/')
        elif var1.type=='user':
            return redirect('/myapp/uhome/')
        else:
            return HttpResponse('''<script>alert("Not found");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location="/myapp/login/"</script>''')


def home(request):
    return render(request,"admin/home.html")

def add_category(request):
    return render(request, "admin/add category.html")



def addcat_post(request):
    name=request.POST['textfield']
    var=Category()
    var.catname=name
    var.save()
    return HttpResponse('''<script>alert("Successful");window.location="/myapp/add_category/"</script>''')


def change_password(request):
    return render(request, "admin/change password.html")

def changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword==confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert("Password mismatch");window.location="/myapp/change_password/"</script>''')
    else :
        return HttpResponse('''<script>alert("Invalid password");window.location="/myapp/change_password/"</script>''')

def edit_category(request,cid):
    res=Category.objects.get(id=cid)
    return render(request,"admin/edit category.html",{'data':res})

def edit_post(request):
    cid=request.POST['cid']
    catname = request.POST['textfield']
    res=Category.objects.filter(id=cid).update(catname=catname)
    return HttpResponse('''<script>alert("Successful");window.location="/myapp/VIEW_CATEGORY/"</script>''')

def delete_category(request,cid):
    res=Category.objects.filter(id=cid).delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/myapp/VIEW_CATEGORY/"</script>''')


def RESPONSE(request):
    return render(request,"admin/RESPONSE.html")

def resp_post(request):
    response = request.POST['textarea']
    return HttpResponse("ok")


def VIEW_CATEGORY(request):
    res=Category.objects.all()
    return render(request,"admin/VIEW CATEGORY.html",{'data':res})

def viewcat_post(request):
    search = request.POST['textfield']
    res = Category.objects.filter(catname__icontains=search)
    return render(request, "admin/VIEW CATEGORY.html", {'data': res})


def VIEW_SUGGESTION(request):
    res=Suggestion.objects.all()
    return render(request,"admin/VIEW SUGGESTION.html",{'data':res})

def viewsug(request):
    fromd = request.POST['textfield']
    tod = request.POST['textfield2']
    res = Suggestion.objects.filter(date__range=[fromd,tod])
    return render(request, "admin/VIEW SUGGESTION.html", {'data': res})


def viewuser(request):
    res=User.objects.all()
    return render(request,"admin/viewuser.html",{'data':res})

def viewuser_post(request):
    text = request.POST['textfield']
    res = User.objects.filter(name__icontains=text)
    return render(request, "admin/viewuser.html", {'data': res})

def send_reply(request,id):

    request.session['cid']=id
    return render(request,"admin/send_reply.html")

def send_repy_post(request):

    res = Suggestion.objects.get(id=request.session['cid'])

    res.response = request.POST['reply']
    res.status = "replied"

    res.save()
    return VIEW_SUGGESTION(request)

def Adddress(request):
    data=Category.objects.all()
    return render(request,"admin/ADD DRESS.html",{'dt':data})

def adddress_POST(request):
    pname=request.POST['textfield4']
    photo=request.FILES['fileField']
    description=request.POST['textarea']
    category=request.POST['select']
    skintone=request.POST['checkbox']
    gender=request.POST['select2']
    skinType = request.POST['select3']
    occassions=request.POST.getlist('occassions')
    oc=""
    for i in occassions:
        if oc!="":
            oc+=","+i
        else:
            oc=i
    from datetime import datetime
    date="dress/"+datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)

    dobj=SkinProducts()
    dobj.pname=pname
    dobj.photo=path
    dobj.description=description
    dobj.CATEGORY_id=category
    dobj.skintone=skintone
    dobj.skinType=skinType
    dobj.occasions=oc
    dobj.gender=gender
    dobj.save()
    return HttpResponse('''<script>alert("Successfully added");window.location="/myapp/home/"</script>''')

def deletedress(request,id):
    data=SkinProducts.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/myapp/viewdress/"</script>''')


def editdress(request,id):

    d=SkinProducts.objects.get(id=id)
    data = Category.objects.all()
    request.session['did']=id
    return render(request,"admin/EDIT DRESS.html",{'data': d,'dd':data})

def editdress_POST(request):
    dname = request.POST['textfield4']

    description = request.POST['textarea']
    category = request.POST['select']
    skintone = request.POST['checkbox']
    gender = request.POST['select2']
    bodytype = request.POST['select3']
    occassions = request.POST.getlist('occassions')
    oc = ""
    for i in occassions:
        if oc != "":
            oc += "," + i
        else:
            oc = i
    from datetime import datetime


    dobj = SkinProducts.objects.get(id=request.session['did'])
    dobj.dname = dname
    if 'fileField' in request.FILES:

        photo = request.FILES['fileField']
        if photo:
            date = "dress/" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)
            dobj.photo = path
    dobj.description = description
    dobj.CATEGORY_id = category
    dobj.skintone = skintone
    dobj.bodytype = bodytype
    dobj.occasions = oc
    dobj.gender = gender
    dobj.save()
    return viewdress(request)


def viewdress(request):
    data=SkinProducts.objects.all()
    cat=Category.objects.all()
    return render(request,"admin/VIEW DRESS.html",{'dt':data,'cat':cat})

def viewdress_POST(request):
    c=request.POST["select"]
    data = SkinProducts.objects.filter(CATEGORY_id=c)
    cat = Category.objects.all()
    return render(request, "admin/VIEW DRESS.html", {'dt': data, 'cat': cat})


def searchdress(request):
    return render(request,"admin/VIEW DRESS.html")

def searchdress_POST(request):
    return HttpResponse("ok")




def user_post(request):

    name=request.POST['name']
    password=request.POST['password']

    image=request.POST['image']
    gender=request.POST['gender']
    phone=request.POST['phone']
    email=request.POST['email']

    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    with open(mediapath + filename, mode='wb') as h:
        h.write(base64.b64decode(image))


    uobj=User()
    uobj.name=name
    uobj.phone=phone
    uobj.email=email
    uobj.photo="/media/"+ filename
    uobj.gender=gender

    lobj=Login()
    lobj.username= email
    lobj.password=password
    lobj.type="user"
    lobj.save()

    uobj.LOGIN= lobj
    uobj.save()


    return JsonResponse({'status':'ok'})

def login2(request):
    uname=request.POST['uname']
    psw=request.POST['psw']

    lobjs= Login.objects.filter(username=uname,password=psw)
    if lobjs.exists():

        lobjs=lobjs[0]

        return JsonResponse({'status':'ok', 'lid': lobjs.id})
    return JsonResponse({'status':'no'})


def  user_changepassword(request):

    lid= request.POST["lid"]
    newpassword= request.POST["newpassword"]



    lobj=Login.objects.get(id=lid)
    lobj.password= newpassword
    lobj.save()
    return JsonResponse({'status': 'ok'})



def user_skintonedetection(request):
    from . import face_detect
    from . import kMeansImgPy
    import cv2
    from . import allotSkinTone

    img= request.POST["img"]
    mediapath="C:\\22-23\\trendtrove\\media\\"

    filename= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"

    with open(mediapath+ filename, mode='wb') as h:
        h.write(base64.b64decode(img))


    imgpath = mediapath+ filename
    image = cv2.imread(imgpath)

    # Detect face and extract
    face_extracted = face_detect.detect_face(image)
    # Pass extracted face to kMeans and get Max color list
    colorsList = kMeansImgPy.kMeansImage(face_extracted)

    print("Main File : ")
    print("Red Component : " + str(colorsList[0]))
    print("Green Component : " + str(colorsList[1]))
    print("Blue Component : " + str(colorsList[2]))

    # Allot the actual skinTone to a certain shade
    allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)
    print("alloted skin tone : ")
    print(allotedSkinToneVal)

    tones = [
        "tone1",
        "tone2",
        "tone3",
        "tone4",
        "tone5",
    ]
    colors = [
        [59, 34, 25],  # tone1
        [161, 110, 75],  # tone2
        [212, 170, 120],  # tone3
        [230, 188, 152],  # tone4
        [255, 231, 209]  # tone5
    ]
    mindex = colors.index(allotedSkinToneVal)
    print(tones[mindex])



    return JsonResponse({'status':'ok', 'tone': tones[mindex]})


def userget_reccomendatins(request):
    tone= request.POST['tone']
    lid= request.POST['lid']

    userobj= User.objects.get(LOGIN_id=lid) 


    print(userobj.gender,"gender")

    print(tone,"tone")


    dressobjs= SkinProducts.objects.filter(skintone=tone,gender=userobj.gender)

    ls=[]

    for i in dressobjs:
        ls.append({'id': i.id, 'dname':i.dname, 'photo':i.photo,'description':i.description, 'catname':i.CATEGORY.catname})


    print(ls)


    return JsonResponse({'status':'ok', 'data':ls})





def user_view_dress_adminadded(request):


    lid= request.POST["lid"]

 

    userobj = User.objects.get(LOGIN_id=lid)



    


    dressobjs= SkinProducts.objects.all()

    ls=[]

    for i in dressobjs:
        ls.append({'id': i.id, 'dname':i.dname, 'photo':i.photo,'description':i.description, 'catname':i.CATEGORY.catname})
    print(ls)
    return JsonResponse({'status':'ok', 'data':ls,  'name': userobj.name, 'photo':userobj.photo})


def user_view_dress_adminadded_search(request):


    lid= request.POST["lid"]

    search= request.POST["search"]

 

    userobj = User.objects.get(LOGIN_id=lid)



    


    dressobjs=SkinProducts.objects.filter(dname__icontains=search)

    ls=[]

    for i in dressobjs:
        ls.append({'id': i.id, 'dname':i.dname, 'photo':i.photo,'description':i.description, 'catname':i.CATEGORY.catname})
    print(ls)
    return JsonResponse({'status':'ok', 'data':ls,  'name': userobj.name, 'photo':userobj.photo})






def userviewprofile(request):
    lid= request.POST['lid']
    userobj = User.objects.get(LOGIN_id=lid)

    return JsonResponse({'status': 'ok', 'name': userobj.name, 'email': userobj.email, 'phone': userobj.phone, 'gender': userobj.gender, 'photo':userobj.photo})




def user_edit_post(request):

    lid=request.POST['lid']
    name=request.POST['name']


    image=request.POST['image']
    gender=request.POST['gender']
    phone=request.POST['phone']
    email=request.POST['email']





    uobj=User.objects.get(LOGIN_id=lid)
    uobj.name=name
    uobj.phone=phone
    uobj.email=email
    if len(image)>0:
        mediapath = "C:\\22-23\\trendtrove\\media\\"

        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        with open(mediapath + filename, mode='wb') as h:
            h.write(base64.b64decode(image))
        uobj.photo="/media/"+ filename
    uobj.save()


    return JsonResponse({'status':'ok'})





def user_delete_dress(request):
    mydressid= request.POST["mydressid"]

    Mydress.objects.filter(id=mydressid).delete()

    return JsonResponse({'status': 'ok'})



def user_send_suggestion(request):
    lid=request.POST["lid"]
    compaint= request.POST["complaint"]


    obj= Suggestion()
    obj.compaint=compaint
    obj.status="pending"
    obj.date= datetime.now()
    obj.response="pending"
    obj.USER= User.objects.get(LOGIN_id=lid)
    obj.save()

    return JsonResponse({'status': 'ok'})


def user_dress_combinations(request):
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers
    from tensorflow.keras.applications import ResNet50
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

    # Load a pre-trained CNN model (ResNet-50)
    base_model = ResNet50(weights='imagenet', include_top=False)

    # Define a custom head for similarity computation
    inputs = keras.Input(shape=(224, 224, 3))
    x = base_model(inputs)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(512, activation='relu')(x)
    outputs = layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1))(x)  # L2 normalization
    model = keras.Model(inputs, outputs)

    # Load and preprocess dress images (replace these paths with your dataset)


    lid= request.session["lid"]

    topdress= Mydress.objects.filter(USER__LOGIN_id= lid,dresstype='top')
    botdress= Mydress.objects.filter(USER__LOGIN_id= lid,dresstype='bottom')


    if not  ( len(topdress) >0 and len(botdress)>0):

        return JsonResponse({'status':'insuffcicientdresscount'})


    top_dress_image_paths = []

    bottom_dress_image_paths = []

    for i in topdress:
        top_dress_image_paths.append(mediapath + i.dressphoto.replace("/media/",""))


    for i in botdress:
        bottom_dress_image_paths.append(mediapath + i.dressphoto.replace("/media/",""))

        # Function to load and preprocess an image
    def load_and_preprocess_image(image_path):
        img = image.load_img(image_path, target_size=(224, 224))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        return img

    # Extract features for all top and bottom dresses
    top_dress_features = []
    bottom_dress_features = []

    for top_image_path in top_dress_image_paths:
        top_dress_img = load_and_preprocess_image(top_image_path)
        top_dress_features.append(model.predict(np.expand_dims(top_dress_img, axis=0)))

    for bottom_image_path in bottom_dress_image_paths:
        bottom_dress_img = load_and_preprocess_image(bottom_image_path)
        bottom_dress_features.append(model.predict(np.expand_dims(bottom_dress_img, axis=0)))

    # Calculate cosine similarity between all pairs of top and bottom dresses
    similarities = np.dot(np.vstack(top_dress_features), np.vstack(bottom_dress_features).T)

    # Display the similarity matrix
    print("Similarity Matrix:")
    print(similarities)

    # You can set a threshold to determine if the dresses match or not
    threshold = 0.6  # Adjust this threshold as needed


    ls=[]

    # Find and display matching combinations
    for i, top_similarities in enumerate(similarities):
        matching_bottom_indices = np.where(top_similarities >= threshold)[0]
        if matching_bottom_indices.any():


            # print(f"Top Dress {i + 1} matches with Bottom Dress(es): {matching_bottom_indices + 1}")

            # print(i,matching_bottom_indices[0], type(i), type(matching_bottom_indices[0]))
            ls.append({'top':topdress[i].dressphoto ,'bottom':botdress[int(matching_bottom_indices[0])].dressphoto   })
        else:
            print(f"No matching Bottom Dress found for Top Dress {i + 1}")



    return render(request,"user/vd.html",{'status':'ok', 'data':ls})




def adminindex(request):
    return render(request,"admin/index.html")

def usignup(request):

    return render(request, "user/user_register.html")

# def user_signup(request):

#     full=request.POST["fullname"]
#     phone=request.POST["phone"]
#     gender=request.POST["gender"]
#     email=request.POST["email"]
#     password=request.POST["password"]
#     img=request.FILES["photo"]
#     from datetime import datetime
#     date = "user/"+datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
#     fs = FileSystemStorage()
#     fs.save(date, img)
#     path = fs.url(date)
#     l=Login()
#     l.username=email
#     l.password=password
#     l.type="user"


#     subject = 'welcome to GFG world'
#     message = f'Hi , thank you for registering in geeksforgeeks.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email, ]
#     send_mail( subject, message, email_from, recipient_list )


#     l.save()

    

    
    
#     u=User()
#     u.name=full
#     u.photo=path
#     u.phone=phone
#     u.gender=gender
#     u.email=email
#     u.LOGIN_id=l.id
#     u.save()
#     return  HttpResponse('''<script>alert("Success");window.location="/myapp/login/"</script>''')


def user_signup(request):
    if request.method == 'POST':
        full = request.POST["fullname"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        password = request.POST["password"]
        img = request.FILES["photo"]

        if not phone.isdigit() or len(phone) != 10:
            return HttpResponse('''<script>alert("Invalid phone number");window.location="/myapp/usignup/"</script>''')

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse('''<script>alert("Invalid email address");window.location="/myapp/usignup/"</script>''')

        # Validate password
        if len(password) < 8:
            return HttpResponse('''<script>alert("Password must be at least 8 characters long");window.location="/myapp/usignup/"</script>''')


        if User.objects.filter(email=email).exists():
            return HttpResponse('''<script>alert("Email already exist");window.location="/myapp/usignup/"</script>''')


        # Generate OTP
        otp = ''.join(random.choices('0123456789', k=6))  # 6-digit OTP

        # Save OTP to the session
        request.session['otp'] = otp

        # Send OTP to the user's email
        subject = 'OTP Verification for Registration'
        message = f'Your OTP for registration is: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

        # Continue with your existing code for saving user details
        date = "user/"+datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, img)
        path = fs.url(date)
        l = Login()
        l.username = email
        l.password = password
        l.type = "user"
        l.save()

        u = User()
        u.name = full
        u.photo = path
        u.phone = phone
        u.gender = gender
        u.email = email
        u.LOGIN_id = l.id
        u.save()
        return render(request, 'user/verify_email.html')

#     

    return HttpResponse("Method Not Allowed")


def verify_email(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp', '')
        saved_otp = request.session.get('otp', '')

        if user_otp == saved_otp:
            # OTP is correct, proceed with user registration
            del request.session['otp']  # Delete OTP from session
            return HttpResponse('''<script>alert("Email verified. Registration successful.");window.location="/myapp/login/"</script>''')
        else:
            # Incorrect OTP, prompt user to try again
            return HttpResponse('''<script>alert("Incorrect OTP. Please try again.");window.location="/myapp/user/verify_email/"</script>''')

    return render(request, 'user/verify_email.html')  # Create a template for OTP verification form

def uhome(request):
    data=SkinProducts.objects.all()
    cat=Category.objects.all()
    return render(request,"user/home.html",{'dt':data,'cat':cat})
    

def uprofile(request):
    u=User.objects.get(LOGIN_id=request.session["lid"])
    return render(request,"user/userprofile.html",{'data':u})


def profile_update(request):
    u=User.objects.get(LOGIN_id=request.session["lid"])
    return render(request,"user/user_updateprofile.html",{'data':u})

def profile_update_post(request):
    u=User.objects.get(LOGIN_id=request.session["lid"])
    full = request.POST["fullname"]
    phone = request.POST["phone"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    u.name=full
    u.phone=phone
    u.gender=gender
    u.email=email
    if 'photo' in request.FILES:
        img = request.FILES["photo"]
        if img:
            from datetime import datetime
            date = "user/" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, img)
            path = fs.url(date)
            u.photo=path
    u.save()
    return uprofile(request)




def change_passwordu(request):
    return render(request, "user/change password.html")

def changepas_postu(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword==confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert("Password mismatch");window.location="/myapp/change_password/"</script>''')
    else :
        return HttpResponse('''<script>alert("Invalid password");window.location="/myapp/change_password/"</script>''')


def VIEW_SUGGESTION_u(request):
    res=Suggestion.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/VIEW SUGGESTION.html",{'data':res})

def viewsug_u(request):

    res = Suggestion()
    res.compaint=request.POST['complaint']
    res.response="pending"
    res.status="pending"
    res.USER=User.objects.get(LOGIN_id=request.session["lid"])
    res.date=datetime.now().date()
    res.save()
    return VIEW_SUGGESTION_u(request)


def skintone(request):

    return render(request,"user/skintone_identify.html")


def skintone_post(request):
    gender=request.POST['select2']
    body=request.POST['select3']
    occassion=request.POST['occassions']
    from . import face_detect
    from . import kMeansImgPy
    import cv2
    from . import allotSkinTone

    img = request.FILES["fileField"]
    from datetime import datetime
    date = "Checking/" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, img)
    path = fs.url(date)

    imgpath = r"D:\my_main_project\final\GlowStyle\GlowStyle\media\Checking\\" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    image = cv2.imread(imgpath)

    # Detect face and extract
    face_extracted = face_detect.detect_face(image)
    # Pass extracted face to kMeans and get Max color list
    colorsList = kMeansImgPy.kMeansImage(face_extracted)

    print("Main File : ")
    print("Red Component : " + str(colorsList[0]))
    print("Green Component : " + str(colorsList[1]))
    print("Blue Component : " + str(colorsList[2]))

    # Allot the actual skinTone to a certain shade
    allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)
    print("alloted skin tone : ")
    print(allotedSkinToneVal)

    tones = [
        "tone1",
        "tone2",
        "tone3",
        "tone4",
        "tone5",
    ]
    colors = [
        [59, 34, 25],  # tone1
        [161, 110, 75],  # tone2
        [212, 170, 120],  # tone3
        [230, 188, 152],  # tone4
        [255, 231, 209]  # tone5
    ]
    mindex = colors.index(allotedSkinToneVal)
    print(tones[mindex])
    d=SkinProducts.objects.filter(skintone=tones[mindex],gender=gender)
    ld=[]
    for i in d:
        if i.skinType == "ALL":
            d=str(i.occasions).split(",")
            print(d,occassion)
            if occassion in d:

                ld.append({"id":i.id,"photo":i.photo,"pname":i.pname,"description":i.description,"category":i.CATEGORY.catname,"skintone":i.skintone,"bodytype":i.skinType,'gender':i.gender})
        elif i.skinType == body:
            d = str(i.occasions).split(",")
            if occassion in d:
                ld.append({"id": i.id, "photo": i.photo, "pname": i.pname, "description": i.description,
                       "category": i.CATEGORY.catname, "skintone": i.skintone, "bodytype": i.skinType,'gender': i.gender})
        else:
            pass
    print(ld)
    return render(request, "user/skintone_identify.html",{"dresses":ld})


def skintones(request):
    import cv2
    return render(request,"user/p.html")


def skintone_posts(request):
    import cv2
    camera = cv2.VideoCapture(0)
    if 'b' in request.POST:
        ret, frame = camera.read()
        # frame_with_faces, faces = detect_faces(frame)
        # if frame:
        import datetime
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = now + ".jpg"
        cv2.imwrite("D:\\my_main_project\\final\\GlowStyle\\GlowStyle\\media\\Checking\\" + filename, frame)
        request.session['fname']=filename
        
        return render(request,"user/p.html",{"img":"/static/check/"+filename})

    else:
        gender=request.POST['select2']
        body=request.POST['select3']
        occassion=request.POST['occassions']
        from . import face_detect
        from . import kMeansImgPy
        import cv2
        from . import allotSkinTone

        from datetime import datetime
        date = "Checking/" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"


        imgpath = "D:\\my_main_project\\final\\GlowStyle\\GlowStyle\\media\\Checking\\" + request.session['fname']
        image = cv2.imread(imgpath)

        # Detect face and extract
        face_extracted = face_detect.detect_face(image)
        # Pass extracted face to kMeans and get Max color list
        colorsList = kMeansImgPy.kMeansImage(face_extracted)

        print("Main File : ")
        print("Red Component : " + str(colorsList[0]))
        print("Green Component : " + str(colorsList[1]))
        print("Blue Component : " + str(colorsList[2]))

        # Allot the actual skinTone to a certain shade
        allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)
        print("alloted skin tone : ")
        print(allotedSkinToneVal)

        tones = [
            "tone1",
            "tone2",
            "tone3",
            "tone4",
            "tone5",
        ]
        colors = [
            [59, 34, 25],  # tone1
            [161, 110, 75],  # tone2
            [212, 170, 120],  # tone3
            [230, 188, 152],  # tone4
            [255, 231, 209]  # tone5
        ]
        mindex = colors.index(allotedSkinToneVal)
        print(tones[mindex])
        d=SkinProducts.objects.filter(skintone=tones[mindex],gender=gender)
        ld=[]
        for i in d:
            if i.skinType == "ALL":
                d=str(i.occasions).split(",")
                if occassion in d:

                    ld.append({"id":i.id,"photo":i.photo,"pname":i.pname,"description":i.description,"category":i.CATEGORY.catname,"skintone":i.skintone,"bodytype":i.skinType,'gender':i.gender})
            elif i.skinType == body:
                d = str(i.occasions).split(",")
                if occassion in d:
                    ld.append({"id": i.id, "photo": i.photo, "pname": i.pname, "description": i.description,
                           "category": i.CATEGORY.catname, "skintone": i.skintone, "bodytype": i.skinType,'gender': i.gender})
            else:
                pass
        return render(request, "user/p.html",{"dresses":ld})

def viewdress_u(request):
    data=SkinProducts.objects.all()
    cat=Category.objects.all()
    return render(request,"user/VIEW DRESS.html",{'dt':data,'cat':cat})

def viewdress_POST_u(request):
    c=request.POST["select"]
    data = SkinProducts.objects.filter(CATEGORY_id=c)
    cat = Category.objects.all()
    return render(request, "user/home.html", {'dt': data, 'cat': cat})


def user_add_dress_get(request):
    return render(request,"user/add_mydress.html")

def user_add_dress(request):

    dressphoto=request.FILES['fileField']
    dresstype=request.POST['select']



    from datetime import datetime
    date = "mydress/" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, dressphoto)
    path = fs.url(date)
    mobj=Mydress()
    mobj.USER= User.objects.get(LOGIN_id=request.session['lid'])
    mobj.dresstype= dresstype
    mobj.dressphoto=path
    mobj.save()

    return HttpResponse('''<script>alert('Added');window.location='/myapp/user_add_dress_get/'</script>''')



def user_view_dress(request):
    lid= request.session["lid"]

    dressobjs=Mydress.objects.filter(USER__LOGIN_id=lid)

    ls = []

    for i in dressobjs:
        ls.append({'id': i.id, 'dressphoto': i.dressphoto, 'dresstype': i.dresstype})

    return render(request, "user/view_dress_my.html",{"data":ls})
def delete_drs(request,id):
    Mydress.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted');window.location='/myapp/user_view_dress/'</script>''')



