
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('',views.login),
    path('login/',views.login),
    path('login_post/',views.log_post),
    path('add_category/',views.add_category),
    path('add_category_post/',views.addcat_post),
    path('change_password/',views.change_password),
    path('change_password_post/', views.changepas_post),
    path('edit_category/<cid>',views.edit_category),
    path('delete_category/<cid>',views.delete_category),
    path('edit_category_post/',views.edit_post),
    path('RESPONSE/',views.RESPONSE),
    path('response_post/',views.resp_post),
    path('VIEW_CATEGORY/',views.VIEW_CATEGORY),
    path('VIEW_CATEGORY_post/',views.viewcat_post),

    path('viewuser/',views.viewuser),
    path('viewuser_post/',views.viewuser_post),
    path('home/',views.home),
    path('Adddress/',views.Adddress),path('VIEW_SUGGESTION/',views.VIEW_SUGGESTION),
    path('VIEW_SUGGESTION_post/',views.viewsug),
    path("send_reply/<id>",views.send_reply),
    path("send_repy_post/",views.send_repy_post),
    path('adddress_POST/',views.adddress_POST),
    path('editdress/<id>',views.editdress),
    path('editdress_POST/',views.editdress_POST),
    path('viewdress/',views.viewdress),
    path('viewdress_POST/',views.viewdress_POST),
    path('deletedress/<id>',views.deletedress),
    path('searchdress/',views.searchdress),
    path('serachdress_POST/',views.searchdress_POST),
    path('adminindex/',views.adminindex),






    path('user_post/',views.user_post),
    path('login2/',views.login2),
    path('user_changepassword/',views.user_changepassword),
    path('user_skintonedetection/',views.user_skintonedetection),
    path('userget_reccomendatins/',views.userget_reccomendatins),
    path('userviewprofile/',views.userviewprofile),
    path('user_edit_post/',views.user_edit_post),
    path('user_add_dress_get/',views.user_add_dress_get),
    path('user_add_dress/',views.user_add_dress),
    path('user_view_dress/',views.user_view_dress),
    path('user_delete_dress/',views.user_delete_dress),
    path('user_send_suggestion/',views.user_send_suggestion),
    path('user_dress_combinations/',views.user_dress_combinations),
    path('user_view_dress_adminadded/',views.user_view_dress_adminadded),
    path('user_view_dress_adminadded_search/',views.user_view_dress_adminadded_search),

    path("usignup/",views.usignup),
    path('verify_email/', views.verify_email, name='verify_email'),
    path("user_signup/",views.user_signup),
    path("uhome/",views.uhome),
    path("uprofile/",views.uprofile),
    path("profile_update/",views.profile_update),
    path("profile_update_post/",views.profile_update_post),
    path('change_password_u/', views.change_passwordu),
    path('change_password_post_u/', views.changepas_postu),
    path('VIEW_SUGGESTION_u/',views.VIEW_SUGGESTION_u),
    path('VIEW_SUGGESTION_post_u/',views.viewsug_u),
    path("skintone/",views.skintone),
    path("skintone_post/",views.skintone_post),
    path('viewdress_u/', views.viewdress_u),
    path('viewdress_POST_u/', views.viewdress_POST_u),
    path("skintones/",views.skintones),
    path("skintone_posts/",views.skintone_posts),

    path('delete_drs/<id>',views.delete_drs),

    



]
