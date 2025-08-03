from datetime import date
from time import localtime
from django.utils import timezone
import json
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
import requests
from django.core.mail import send_mail
# from passlib.hash import pbkdf2_sha256
from demographic.models import Kebele, Nation, Region, Woreda, Zone
from notification.models import NotifiableUsers, Notification, SystemNotification
from superAdmin.ProfileUpdateForm import UserProfileUpdateForm
from superAdmin.forms import GroupForm
from superAdmin.models import *
from app .models import CustomUser as User
from superAdmin .models import Role
from django.core import mail


from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.db import connection
from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Permission
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.models import Group
# from staffprofile.forms import ProfileImage
import array

from django.http import HttpResponse
from .utils import generate_id_card_pdf
def generate_id_card(request, id_card_id):
    id_card = User.objects.get(id=id_card_id)
    pdf_file = generate_id_card_pdf(id_card)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="id_card_{id_card_id}.pdf"'
    return response
# from docx import Document

@login_required(login_url="/")
@permission_required("CustomUser.view_customuser",raise_exception=True)
def user_details(request):
    id = request.POST.get('id')
    user = User.objects.filter(id = id).filter(soft_delete = 0)
    # user = User.objects.select_related('user_roles').filter(id = id)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    return render(request, 'superAdmin/UserManagement/users/user_details.html',context)
@login_required(login_url="/")
@permission_required("CustomUser.add_role",raise_exception=True)
def create_role(request):
    return render(request, 'superAdmin/UserManagement/role/fields.html')
@login_required(login_url="/")
@permission_required("CustomUser.add_customuser",raise_exception=True)
def create_user(request):
    role = Role.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'role': role,
    }
    return render(request, 'superAdmin/UserManagement/users/create_user.html', context)
@login_required(login_url="/")
@permission_required("CustomUser.add_customuser",raise_exception=True)
def loadUserCell(request):
    party =request.POST.get('party')
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, 'superAdmin/UserManagement/users/usercell.html', context)
@login_required(login_url="administrator")
@permission_required("CustomUser.add_customuser",raise_exception=True)
def save_user_and_return(request):
   if request.method =="POST":
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    passwords =  make_password(password)
    user_roles = request.POST.get("user_roles")
    is_staff = request.POST.get("is_staff")
    is_active = request.POST.get("is_active")
    Is_superUser = request.POST.get("Is_superUser")
    users =User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_staff = is_staff,
        is_active = is_active,
        is_superuser = Is_superUser,
        user_roles_id= user_roles,
        username= email,
        password= passwords
    )
    users.save()    
    user = User.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    return render(request, 'superAdmin/UserManagement/users/index.html',context)

@login_required(login_url="/")
@permission_required("CustomUser.change_customuser",raise_exception=True)
def updateuser(request):
   if request.method =="POST":
    id =request.POST.get("id")
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("email")
    password = request.POST.get("password")
    passwords =  make_password(password)
    user_roles = request.POST.get("user_roles")
    is_staff = request.POST.get("is_staff")
    is_active = request.POST.get("is_active")
    Is_superuser = request.POST.get("Is_superuser")
    user_update = User.objects.get(id = id)
    user_update.first_name = first_name
    user_update.last_name = last_name
    user_update.email = email
    user_update.user_roles_id= user_roles
    user_update.username= username
    user_update.password= passwords
    user_update.is_staff = is_staff
    user_update.is_active = is_active
    user_update.is_superuser = Is_superuser
    user_update.save()
    user = User.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    return render(request, 'superAdmin/UserManagement/users/index.html',context)
@login_required(login_url="/")
@permission_required("CustomUser.add_role",raise_exception=True)
def save_role(request):
   if request.method =="POST":
    name =request.POST.get("role_name")
    roles =request.POST.get("role_description")
    role =Role(
       role_name = name,
       description = roles,
    )
    role.save()
    return render(request, 'superAdmin/UserManagement/role/fields.html')
@login_required(login_url="/")
def role_edit(request):
   if request.method =="POST":
    id =request.POST.get("id")
    role = Role.objects.filter(id = id)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'role': role
    }
    return render(request, 'superAdmin/UserManagement/role/edit.html',context)
@login_required(login_url="/")
@permission_required("CustomUser.change_role",raise_exception=True)
def update_role(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("role_name")
    roles_description =request.POST.get("role_description")
    role = Role.objects.get(id = id)
    role.role_name=name
    role.description =roles_description
    role.save()
    return render(request, 'superAdmin/UserManagement/role/edit.html')


@login_required(login_url="/")
@permission_required("CustomUser.delete_role",raise_exception=True)
def delete_role(request):
    id = request.POST.get('id')
    roles = Role.objects.get(id = id)
    roles.soft_delete =1
    roles.save()
    role = Role.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'role': role
    }
    return render(request, 'superAdmin/UserManagement/role/index.html',context)

@login_required(login_url="/")
@permission_required("CustomUser.view_role",raise_exception=True)
def role_index(request):
    role = Role.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'role': role
    }
    return render(request, 'superAdmin/UserManagement/role/index.html',context)
   
@login_required(login_url="/")
@permission_required("CustomUser.view_customuser",raise_exception=True)
def users(request):
    user = User.objects.filter(soft_delete = 0).select_related('user_roles')
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    return render(request, 'superAdmin/UserManagement/users/index.html',context)
def view_permission(request):
    id = request.POST.get('id')
    user = User.objects.select_related('user_roles').filter(id = id).filter(soft_delete = 0)
    cursor = connection.cursor()
    cursor.execute(f"select auth_permission.id as ids, name, codename,users_user_permissions.id from auth_permission join users_user_permissions on users_user_permissions.permission_id = auth_permission.id where users_user_permissions.customuser_id = '{id}'")
    result =cursor.fetchall()
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'permission': result,
        'user':user
    }
    return render(request, 'superAdmin/UserManagement/users/viewpermission.html',context)
@login_required(login_url="/")
def delete_permission(request):
    id = request.POST.get('id')
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM users_user_permissions WHERE id = '{id}'")
    html = "<div class=col-md-12 id=revoke> <button id=RevokePermission class= 'btn btn-info btn-sm revoke'> Update</button></div><br>"
    data = {'html': html}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def load_permission(request):
    id = request.POST.get('id')
    user = User.objects.select_related('user_roles').filter(id = id).filter(soft_delete = 0)
    cursor = connection.cursor()
    cursor.execute(f"select permission_id from users_user_permissions where customuser_id = '{id}'")
    perm_id =cursor.fetchall()
    a = array.array('i', [])
    for i in perm_id:
       pr =i[0]
       a.insert(1,pr)
   
    cursor = connection.cursor()
    cursor.execute(f"select auth_permission.id as ids from auth_permission join users_user_permissions on users_user_permissions.permission_id = auth_permission.id where users_user_permissions.customuser_id != '{id}'")
    permission = Permission.objects.exclude(id__in=a[0:])
    context = {
        'permission': permission,
        'user':user
    }
    return render(request, 'superAdmin/UserManagement/users/permission.html',context)
def permit(request):
    permissions = request.POST.get('id')
    user_id = request.POST.get('user_id')
    cursor = connection.cursor()
    # cursor.execute(f"insert into users_user_permissions values('{user_id}','{permissions}')")
    cursor.execute(f"INSERT INTO `users_user_permissions`(`customuser_id`, `permission_id`) values('{user_id}','{permissions}')")
    html = "<div class=col-md-12 id=revoke> <button id=addPermission class= 'btn btn-info btn-sm revoke'> Update</button></div><br>"
    data = {'html': html}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    # return HttpResponse(({'html':"Sucessfully added"}), 'application/json')
@login_required(login_url="/")
def active_users(request):
    user = User.objects.filter(is_active = 1).filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    # return render(request, 'superAdmin/UserManagement/users/create_user.html',context)
    return render(request, 'superAdmin/UserManagement/users/active_user_index.html',context)

@login_required(login_url="/")
def user_edit_view(request):
    id = request.POST.get('id')
    user = User.objects.select_related('user_roles').filter(id = id)
    role = Role.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user,
        'role': role
    }
    return render(request, 'superAdmin/UserManagement/users/user_edit_view.html',context)

@login_required(login_url="/")
@permission_required("RequestItem.add_requestitem",raise_exception=True)
def Delete(request):
    id = request.POST.get('id')
    users = User.objects.get(id = id)
    users.soft_delete =1
    users.save()
    user = User.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'user': user
    }
    return render(request, 'superAdmin/UserManagement/users/index.html',context)

# User Groups 
@login_required(login_url="/")
def group_index(request):
    group = Group.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'group': group
    }
    return render(request, 'superAdmin/UserManagement/group/index.html',context)
def create_group(request):
    # GroupForm
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            group = Group.objects.filter(soft_delete = 0)
            context = {
                'media_root': settings.MEDIA_ROOT,
                'media_url': settings.MEDIA_URL,
                'group': group
            }
            return render(request, 'superAdmin/UserManagement/group/index.html',context)
    else:
       form = GroupForm()
    return render(request, 'superAdmin/UserManagement/group/fields.html', {'form':form})
@login_required(login_url="/")
def delete_group(request):
    id = request.POST.get('id')
    roles = Group.objects.filter(id = id)
    roles.delete()
    group = Group.objects.filter(soft_delete = 0)
    context = {
        'group': group
    }
    return render(request, 'superAdmin/UserManagement/group/index.html',context)
@login_required(login_url="/") 
def update_profile(request, file_id):
    if request.method == 'POST' and request.FILES:
        file_obj = User.objects.get(id=file_id)
        new_file = request.FILES['new_file']
        file_obj.user_profile.save(new_file.name, new_file, save=True)
        return redirect('superAdmin:users')
    context = {
    'media_root': settings.MEDIA_ROOT,
    'media_url': settings.MEDIA_URL,
    }
    return render(request, 'superAdmin/UserManagement/users/update_file.html',context) 
@login_required(login_url="/")
def update_own_profile(request):
   if request.method =="POST":
    id =request.POST.get("id")
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    password = request.POST.get("password")
    passwords =  make_password(password)
    user_update = User.objects.get(id = id)
    user_update.first_name = first_name
    user_update.last_name = last_name
    user_update.email = email
    user_update.password= passwords
    user_update.save()
    context = {
    'media_root': settings.MEDIA_ROOT,
    'media_url': settings.MEDIA_URL,
    }
    return render(request, 'superAdmin/UserManagement/users/update_file.html',context) 
# Region Functions 
@login_required(login_url="/")
def region_index(request):
    region = Region.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'region': region
    }
    return render(request, 'superAdmin/Settings/region/index.html',context)
@login_required(login_url="/")
def create_region(request):
    return render(request, 'superAdmin/Settings/region/fields.html')
@login_required(login_url="/")
def save_region(request):
   if request.method =="POST":
    name =request.POST.get("region_name")
    description =request.POST.get("description")
    regions =Region(
       name = name,
       description = description,
    )
    regions.save()
    region = Region.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'region': region
    }
    return render(request, 'superAdmin/Settings/region/index.html',context)
@login_required(login_url="/")
def region_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    region = Region.objects.filter(id = id)
    context = {
    'region': region
    }
    return render(request, 'superAdmin/Settings/region/edit.html', context)
@login_required(login_url="/")
def update_region(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    region = Region.objects.get(id = id)
    region.name=name
    region.description =description
    region.save()
    return render(request, 'superAdmin/Settings/region/edit.html')
@login_required(login_url="/")
def delete_region(request):
    id = request.POST.get('id')
    region = Region.objects.get(id = id)
    region.soft_delete =1
    region.save()
    data = {'success': "መረጃዉ በተሳካ ሁኔታ ተሰርዟል"}
    return JsonResponse(data)

# Zone Functions  
@login_required(login_url="/")
def zone_index(request):
    zone = Zone.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'zone': zone
    }
    return render(request, 'superAdmin/Settings/zone/index.html',context)
@login_required(login_url="/")
def create_zone(request):
    return render(request, 'superAdmin/Settings/zone/fields.html')
@login_required(login_url="/")
def save_zone(request):
   if request.method =="POST":
    name =request.POST.get("zone_name")
    description =request.POST.get("zone_description")
    zone =Zone(
       name = name,
       description = description,
    )
    zone.save()
    return render(request, 'superAdmin/Settings/region/fields.html')
@login_required(login_url="/")
def zone_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    zone = Zone.objects.filter(id = id)
    context = {
    'zone': zone
    }
    return render(request, 'superAdmin/Settings/zone/edit.html', context)
@login_required(login_url="/")
def update_zone(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    zone = Zone.objects.get(id = id)
    zone.name=name
    zone.description =description
    zone.save()
    return render(request, 'superAdmin/Settings/zone/edit.html')
@login_required(login_url="/")
def delete_zone(request):
    id = request.POST.get('id')
    zone = Zone.objects.get(id = id)
    zone.soft_delete =1
    zone.save()
    data = {'success': "መረጃዉ በተሳካ ሁኔታ ተሰርዟል"}
    return JsonResponse(data)
# Nation Functions 
@login_required(login_url="/")
def nation_index(request):
    nation = Nation.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'nation': nation
    }
    return render(request, 'superAdmin/Settings/nation/index.html',context)
@login_required(login_url="/")
def create_nation(request):
    return render(request, 'superAdmin/Settings/nation/fields.html')
@login_required(login_url="/")
def save_nation(request):
   if request.method =="POST":
    name =request.POST.get("nation_name")
    description =request.POST.get("nation_description")
    nation =Nation(
       name = name,
       description = description,
    )
    nation.save()
    return render(request, 'superAdmin/Settings/nation/fields.html')
@login_required(login_url="/")
def nation_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    nation = Nation.objects.filter(id = id)
    context = {
    'nation': nation
    }
    return render(request, 'superAdmin/Settings/nation/edit.html', context)   
@login_required(login_url="/")
def update_nation(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    nation = Nation.objects.get(id = id)
    nation.name=name
    nation.description =description
    nation.save()
    return render(request, 'superAdmin/Settings/nation/edit.html')
@login_required(login_url="/")
def delete_nation(request):
    id = request.POST.get('id')
    nation = Nation.objects.get(id = id)
    nation.soft_delete =1
    nation.save()
    data = {'success': "መረጃዉ በተሳካ ሁኔታ ተሰርዟል"}
    return JsonResponse(data)

# Kebele Functions 
@login_required(login_url="/")
def kebele_index(request):
    kebele = Kebele.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'kebele': kebele
    }
    return render(request, 'superAdmin/Settings/kebele/index.html',context)
@login_required(login_url="/")
def create_kebele(request):
    return render(request, 'superAdmin/Settings/kebele/fields.html')
@login_required(login_url="/")
def save_kebele(request):
   if request.method =="POST":
    name =request.POST.get("kebele_name")
    description =request.POST.get("kebele_description")
    kebele =Kebele(
       name = name,
       description = description,
    )
    kebele.save()
    return render(request, 'superAdmin/Settings/kebele/fields.html')
@login_required(login_url="/")
def kebele_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    kebele = Kebele.objects.filter(id = id)
    context = {
    'kebele': kebele
    }
    return render(request, 'superAdmin/Settings/kebele/edit.html', context)   
@login_required(login_url="/")
def update_kebele(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    kebele = Kebele.objects.get(id = id)
    kebele.name=name
    kebele.description =description
    kebele.save()
    return render(request, 'superAdmin/Settings/kebele/edit.html')
# Woreda Functions 
@login_required(login_url="/")
def delete_kebele(request):
    id = request.POST.get('id')
    kebele = Kebele.objects.get(id = id)
    kebele.soft_delete =1
    kebele.save()
    data = {'success': "መረጃዉ በተሳካ ሁኔታ ተሰርዟል"}
    return JsonResponse(data)
@login_required(login_url="/")
def woreda_index(request):
    woreda = Woreda.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'woreda': woreda
    }
    return render(request, 'superAdmin/Settings/woreda/index.html',context)
@login_required(login_url="/")
def create_woreda(request):
    return render(request, 'superAdmin/Settings/woreda/fields.html')
@login_required(login_url="/")
def save_woreda(request):
   if request.method =="POST":
    name =request.POST.get("woreda_name")
    description =request.POST.get("woreda_description")
    woreda =Woreda(
       name = name,
       description = description,
    )
    woreda.save()
    return render(request, 'superAdmin/Settings/woreda/fields.html')
@login_required(login_url="/")
def woreda_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    woreda = Woreda.objects.filter(id = id)
    context = {
    'woreda': woreda
    }
    return render(request, 'superAdmin/Settings/woreda/edit.html', context)   
@login_required(login_url="/")
def update_woreda(request):
   if request.method =="POST":
    id =request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    woreda = Woreda.objects.get(id = id)
    woreda.name=name
    woreda.description =description
    woreda.save()
    return render(request, 'superAdmin/Settings/woreda/edit.html')
@login_required(login_url="/")
def delete_woreda(request):
    id = request.POST.get('id')
    woreda = Woreda.objects.get(id = id)
    woreda.soft_delete =1
    woreda.save()
    data = {'success': "መረጃዉ በተሳካ ሁኔታ ተሰርዟል"}
    return JsonResponse(data)
@login_required(login_url="/")
def email_index(request):
    email = Notification.objects.filter(soft_delete = 0)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'email': email
    }
    return render(request, 'superAdmin/Notification/notification/index.html',context)
# System Notification 
@login_required(login_url="/")
def view_notification(request):
    notifications = SystemNotification.objects.filter(read =0).filter(recipient = request.user.id)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'notifications': notifications
    }
    return render(request, 'superAdmin/Notification/notification/notificationTable.html',context)
@login_required(login_url="/")
def superAdmindetail_notification(request):
    id =request.POST.get("id")
    notification = SystemNotification.objects.filter(id =id)
    context = {
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'notification': notification
    }
    notifup = SystemNotification.objects.get(id =id)
    notifup.read =1
    notifup.save()
    return render(request, 'superAdmin/Notification/notification/notificationDetail.html',context)
@login_required(login_url="/")
def create_email(request):
    return render(request, 'superAdmin/Notification/notification/fields.html')

@login_required(login_url="/")
def save_email(request):
   if request.method =="POST":
    holder =request.POST.get("holder")
    email =request.POST.get("email")
    email =Notification(
       holder = holder,
       email = email,
    )
    email.save()
    return render(request, 'superAdmin/Notification/notification/fields.html')

@login_required(login_url="/")
def email_edit(request):
 if request.method =="POST":
    id =request.POST.get("id")
    email = Notification.objects.filter(id = id)
    context = {
    'email': email
    }
    return render(request, 'superAdmin/Notification/notification/edit.html',context)  
@login_required(login_url="/")
def update_email(request):
   if request.method =="POST":
    id =request.POST.get("id")
    holder =request.POST.get("holder")
    emails =request.POST.get("email")
    emailv = Notification.objects.get(id = id)  
    emailv.holder = holder
    emailv.email = emails
    emailv.save()
    return redirect('superAdmin:email_index')
@login_required(login_url="/")
@permission_required("Notification.delete_notification",raise_exception=True)
def delete_email(request):
    id = request.POST.get('id')
    email = Notification.objects.filter(id = id)
    email.delete()
    return redirect('superAdmin:email_index')
@login_required(login_url="/")
def report(request):
   return render(request, 'cellAdmin/MemberData/report/index.html')
@login_required(login_url="/")
def not_user(request):
    not_users =NotifiableUsers.objects.all()
    users =[0]
    for i in not_users:
        users.append(i.user_id)  
    notif_user =User.objects.filter(id__in =users)   
    context ={
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'notif_user':notif_user
    }
    return render(request, 'superAdmin/Notification/notification/users.html', context)
@login_required(login_url="/")
def create_not_user(request):
    users =User.objects.all()
    context ={
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
        'users':users
    }
    return render(request, 'superAdmin/Notification/notification/user_field.html', context)
@login_required(login_url="/")
def save_not_user(request):
   if request.method =="POST":
    user =request.POST.get("user")
    notifiable =NotifiableUsers(
       user_id = user
    )
    notifiable.save()
    return redirect('superAdmin:not_user')
@login_required(login_url="/")
@permission_required("notification.delete_notifiableusers",raise_exception=True)
def delete_not_user(request):
    id = request.POST.get('id')
    not_user = NotifiableUsers.objects.filter(user_id = id)
    not_user.delete()
    return redirect('superAdmin:not_user')

@login_required(login_url="/") 
def notif_test(request):  
    reciver =NotifiableUsers.objects.filter(soft_delete = 0)
    for i in reciver:
        notification = SystemNotification(
        recipient = i.user_id,
        message = "Some one shifted from partial to whole membership",
        read = 0 
        )
        notification.save()
    # Send Email 
    broadcast_email = Notification.objects.all()
    for i in broadcast_email:
        send_mail(
            "Dear "+ i.holder,
            'This is sample email broadcasting test',
            'nurekemal100@gmail.com',
            [i.email],
            fail_silently=False,
        )
    return HttpResponse("Notification Test successful!", status=200)  # 200 OK
@login_required(login_url="/")
@permission_required("registrar.change_membership",raise_exception=True)
def update_ownProfile(request, id):
    member = get_object_or_404(User, id =request.user.id)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance= member)
        if form.is_valid():
            form.save()
            return redirect('superAdmin:users')  # Redirect after saving
    else:
        form = UserProfileUpdateForm(instance=member)
        context = {
            'form': form,
            'member': member,
            'media_root': settings.MEDIA_ROOT,
            'media_url': settings.MEDIA_URL,
        }
    return render(request, 'superAdmin/pages/frontend/profileUpdate.html',context)
