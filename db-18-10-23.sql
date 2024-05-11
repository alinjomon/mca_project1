/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 10.4.28-MariaDB : Database - sadh
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sadh` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `sadh`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add dress',7,'add_dress'),
(26,'Can change dress',7,'change_dress'),
(27,'Can delete dress',7,'delete_dress'),
(28,'Can view dress',7,'view_dress'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add user',9,'add_user'),
(34,'Can change user',9,'change_user'),
(35,'Can delete user',9,'delete_user'),
(36,'Can view user',9,'view_user'),
(37,'Can add suggestion',10,'add_suggestion'),
(38,'Can change suggestion',10,'change_suggestion'),
(39,'Can delete suggestion',10,'delete_suggestion'),
(40,'Can view suggestion',10,'view_suggestion'),
(41,'Can add category',11,'add_category'),
(42,'Can change category',11,'change_category'),
(43,'Can delete category',11,'delete_category'),
(44,'Can view category',11,'view_category'),
(45,'Can add mydress',12,'add_mydress'),
(46,'Can change mydress',12,'change_mydress'),
(47,'Can delete mydress',12,'delete_mydress'),
(48,'Can view mydress',12,'view_mydress');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(11,'myapp','category'),
(7,'myapp','dress'),
(8,'myapp','login'),
(12,'myapp','mydress'),
(10,'myapp','suggestion'),
(9,'myapp','user'),
(6,'sessions','session');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-13 10:33:07.071967'),
(2,'auth','0001_initial','2023-10-13 10:33:07.639004'),
(3,'admin','0001_initial','2023-10-13 10:33:07.733574'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-13 10:33:07.749282'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-13 10:33:07.749282'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-13 10:33:07.811938'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-13 10:33:07.858935'),
(8,'auth','0003_alter_user_email_max_length','2023-10-13 10:33:07.874647'),
(9,'auth','0004_alter_user_username_opts','2023-10-13 10:33:07.890280'),
(10,'auth','0005_alter_user_last_login_null','2023-10-13 10:33:07.921689'),
(11,'auth','0006_require_contenttypes_0002','2023-10-13 10:33:07.921689'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-13 10:33:07.937510'),
(13,'auth','0008_alter_user_username_max_length','2023-10-13 10:33:07.953377'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-13 10:33:07.984629'),
(15,'auth','0010_alter_group_name_max_length','2023-10-13 10:33:08.000255'),
(16,'auth','0011_update_proxy_permissions','2023-10-13 10:33:08.000255'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-13 10:33:08.031738'),
(18,'myapp','0001_initial','2023-10-13 10:33:08.173228'),
(19,'sessions','0001_initial','2023-10-13 10:33:08.204606'),
(20,'myapp','0002_category','2023-10-13 10:39:43.403334'),
(21,'myapp','0003_rename_dresscolour_dress_description_and_more','2023-10-18 11:07:57.683950'),
(22,'myapp','0004_dress_gender','2023-10-18 11:30:47.388960');

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('fapuktls1qtre0i6qvo0c2e1jgqfz8ex','eyJsaWQiOjF9:1qt4q7:tqQNsEiMk87OJtTBOXXmcWio2ulTpGxN6sqrL_uGPlo','2023-11-01 11:35:51.940756');

/*Data for the table `myapp_category` */

insert  into `myapp_category`(`id`,`catname`) values 
(2,'pant'),
(3,'pant'),
(4,'shirt');

/*Data for the table `myapp_dress` */

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'sadh123','1234','admin'),
(2,'test123','321','user'),
(3,'test321','1234','user');

/*Data for the table `myapp_mydress` */

/*Data for the table `myapp_suggestion` */

insert  into `myapp_suggestion`(`id`,`compaint`,`response`,`status`,`date`,`USER_id`) values 
(0,'this too good for me','','pendimg','11-10-2023',2),
(1,'this not good','','pending','10-10-2023',1);

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`email`,`phone`,`gender`,`LOGIN_id`) values 
(1,'ash','test1@gmail.com','9876543210','male',2),
(2,'hari','test2@gmail.com','9876543211','female',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
