-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: tyre_trust
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add tyre model',7,'add_tyremodel'),(26,'Can change tyre model',7,'change_tyremodel'),(27,'Can delete tyre model',7,'delete_tyremodel'),(28,'Can view tyre model',7,'view_tyremodel'),(29,'Can add tyre variant',8,'add_tyrevariant'),(30,'Can change tyre variant',8,'change_tyrevariant'),(31,'Can delete tyre variant',8,'delete_tyrevariant'),(32,'Can view tyre variant',8,'view_tyrevariant'),(33,'Can add cart item',9,'add_cartitem'),(34,'Can change cart item',9,'change_cartitem'),(35,'Can delete cart item',9,'delete_cartitem'),(36,'Can view cart item',9,'view_cartitem'),(37,'Can add Заказ',10,'add_order'),(38,'Can change Заказ',10,'change_order'),(39,'Can delete Заказ',10,'delete_order'),(40,'Can view Заказ',10,'view_order'),(41,'Can add order item',11,'add_orderitem'),(42,'Can change order item',11,'change_orderitem'),(43,'Can delete order item',11,'delete_orderitem'),(44,'Can view order item',11,'view_orderitem'),(45,'Can add favourite',12,'add_favourite'),(46,'Can change favourite',12,'change_favourite'),(47,'Can delete favourite',12,'delete_favourite'),(48,'Can view favourite',12,'view_favourite'),(49,'Can add Категория',14,'add_category'),(50,'Can change Категория',14,'change_category'),(51,'Can delete Категория',14,'delete_category'),(52,'Can view Категория',14,'view_category'),(53,'Can add rim',15,'add_rim'),(54,'Can change rim',15,'change_rim'),(55,'Can delete rim',15,'delete_rim'),(56,'Can view rim',15,'view_rim'),(57,'Can add Модель диска',16,'add_rimmodel'),(58,'Can change Модель диска',16,'change_rimmodel'),(59,'Can delete Модель диска',16,'delete_rimmodel'),(60,'Can view Модель диска',16,'view_rimmodel'),(61,'Can add Вариант диска',17,'add_rimvariant'),(62,'Can change Вариант диска',17,'change_rimvariant'),(63,'Can delete Вариант диска',17,'delete_rimvariant'),(64,'Can view Вариант диска',17,'view_rimvariant'),(65,'Can add favourite rim',18,'add_favouriterim'),(66,'Can change favourite rim',18,'change_favouriterim'),(67,'Can delete favourite rim',18,'delete_favouriterim'),(68,'Can view favourite rim',18,'view_favouriterim');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$aErtsFJyI0cawyVE1arxQs$Itz0WGeIV23J1btdydwsCqwkD6DQcof9cq3U0sG+Onk=','2025-06-04 01:35:11.480502',0,'iceboyonda','Дима','Зима','oy.shit.205@mail.ru',1,1,'2025-05-05 19:14:03.598500'),(3,'pbkdf2_sha256$600000$lBbulTJxwglVHEpsj6gwmg$ljY2lNYKFSQhhlKGvj9j8rB+Vi7WFR/mwRiwk+pJOrU=','2025-05-15 23:50:09.044678',1,'iceboy.on.da','','','oy.shit.205@mail.ru',1,1,'2025-05-05 19:22:44.926420'),(4,'pbkdf2_sha256$600000$1NUm41PlJ5foSfu7UxNdxW$5y3X58kSb2nxrDlHzzIXT9Px/MzCN1s3xUHn+svuAOw=','2025-05-15 20:08:54.734346',0,'DANBEBOV','010','101','BEBOV@qwe.ru',0,1,'2025-05-15 20:08:53.766933'),(5,'pbkdf2_sha256$600000$l31ibSwMdegpOVB0aWUgwF$WPSPndIbkasLnwJTZrP19IvMqz8loILrqTTNGmTDDNM=','2025-06-08 09:51:43.493374',1,'iceboy','','','iceboy69@vk.com',1,1,'2025-05-15 23:14:46.638792'),(6,'pbkdf2_sha256$600000$KfgNev8ogpbBcppBs6ykik$KdueYTAxQFqfzdL++PqbICkL0x49qmzMPSlRYlCZoN4=','2025-05-21 04:46:26.502896',0,'lol','kek','kekov','lol@mail.ru',0,1,'2025-05-15 23:55:48.269001'),(7,'pbkdf2_sha256$720000$ZPMLFbrDevVFdeMV1GIKD9$a6w/E7fiHc6J/I3tlbwXD+6Zdlk9coN2MebQk2XMPB4=',NULL,1,'ice','','','ice@vk.com',1,1,'2025-06-04 02:41:23.879979');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-05-05 19:24:25.305864','2','ice',3,'',4,3),(2,'2025-05-14 19:10:00.219537','17','Michelin pilot sport',1,'[{\"added\": {}}]',7,3),(3,'2025-05-14 19:17:44.919565','17','Michelin pilot sport',3,'',7,3),(4,'2025-05-15 17:52:14.412235','6','Gislaved Gislaved Nord Frost 200',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(5,'2025-05-15 17:52:25.847717','6','Gislaved Nord Frost 200',2,'[{\"changed\": {\"fields\": [\"\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435\"]}}]',7,3),(6,'2025-05-15 17:54:14.055479','5','Goodyear UltraGrip Ice 2',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(7,'2025-05-15 17:55:03.182459','4','Nokian Hakkapeliitta 10',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(8,'2025-05-15 17:57:55.731041','3','Bridgestone Blizzak VRX3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(9,'2025-05-15 18:46:25.207066','2','Continental IceContact 3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(10,'2025-05-15 18:46:41.794197','5','Goodyear UltraGrip Ice 2',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(11,'2025-05-15 18:47:15.360651','6','Gislaved Nord Frost 200',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(12,'2025-05-15 18:47:29.578174','1','Michelin X-Ice North 4',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(13,'2025-05-15 18:47:46.424019','3','Bridgestone Blizzak VRX3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(14,'2025-05-15 18:48:10.057149','4','Nokian Hakkapeliitta 10',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(15,'2025-05-15 18:57:29.202321','16','Toyo Proxes R888R',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(16,'2025-05-15 18:57:52.990262','15','Continental AllSeasonContact',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(17,'2025-05-15 18:58:04.114234','14','Michelin CrossClimate+',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(18,'2025-05-15 18:58:15.631876','13','Goodyear Vector 4Seasons Gen-3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(19,'2025-05-15 18:58:38.914653','12','Nokian Nordman SX2',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(20,'2025-05-15 18:58:53.214723','11','Goodyear EfficientGrip Performance',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(21,'2025-05-15 18:59:00.947585','10','Michelin Energy Saver+',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(22,'2025-05-15 18:59:13.820495','9','Continental EcoContact 6',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(23,'2025-05-15 18:59:32.994474','8','Bridgestone Turanza T005',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(24,'2025-05-15 18:59:38.109268','7','Michelin Pilot Sport 4',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,3),(25,'2025-05-20 00:16:50.653328','1','blitz brv 03',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"blitz brv 03 16.0x10.0 4\"}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"blitz brv 03 17.0x10.0 5\"}}]',16,5),(26,'2025-05-20 00:24:26.019372','2','blitz brv 03',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"blitz brv 03 16.0x10.0 4x100\"}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"blitz brv 03 17.0x10.0 4x100\"}}]',16,5),(27,'2025-05-20 00:25:20.490683','1','blitz brv 03 16.0x10.0 4',3,'',17,5),(28,'2025-05-20 00:25:20.551364','2','blitz brv 03 17.0x10.0 5',3,'',17,5),(29,'2025-05-20 04:06:13.038860','3','vossen chinese chit',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"vossen chinese chit 19.0x12.0 5x112\"}}]',16,5),(30,'2025-05-20 16:55:18.413225','3','blitz brv 03 16.0x10.0 4x100',3,'',17,5),(31,'2025-05-20 16:55:18.645888','4','blitz brv 03 17.0x10.0 4x100',3,'',17,5),(32,'2025-05-20 16:55:18.841498','5','vossen chinese chit 19.0x12.0 5x112',3,'',17,5),(33,'2025-05-20 16:56:54.967454','4','vossen chinese shit',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"vossen chinese shit 19.0x10.0 5x112\"}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"vossen chinese shit 20.0x10.0 5x112\"}}]',16,5),(34,'2025-05-20 21:37:48.333156','5','test brand test name',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"test brand test name 19.0x21.0 2112\"}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"test brand test name 18.0x21.0 2112\"}}, {\"added\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"test brand test name 17.0x21.0 2113\"}}]',16,5),(35,'2025-05-21 01:57:58.281311','11','Aez Kiel',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Aez Kiel 16.0x7.0 4x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Aez Kiel 17.0x7.5 4x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(36,'2025-05-21 01:58:13.680939','7','BBS CH-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 18.0x8.0 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 19.0x8.5 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(37,'2025-05-21 01:58:22.565918','12','Dotz Hanzo',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 18.0x8.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 19.0x8.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 20.0x9.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(38,'2025-05-21 01:58:31.121218','9','Enkei RPF1',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Enkei RPF1 16.0x7.0 4x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Enkei RPF1 17.0x7.5 4x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(39,'2025-05-21 01:58:38.817252','8','OZ Ultraleggera',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"OZ Ultraleggera 17.0x7.5 5x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"OZ Ultraleggera 18.0x8.0 5x100\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(40,'2025-05-21 01:58:52.815336','13','Rays Volk Racing TE37',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 17.0x8.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 18.0x9.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 19.0x10.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(41,'2025-05-21 01:59:02.949408','6','Replica RS-1',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Replica RS-1 17.0x7.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Replica RS-1 18.0x8.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Replica RS-1 19.0x8.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(42,'2025-05-21 01:59:17.482624','10','Rial Lucca',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 17.0x7.5 5x108\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 18.0x8.0 5x108\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 19.0x8.5 5x108\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(43,'2025-05-21 01:59:26.013891','16','Rotiform LAS-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 19.0x8.5 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 19.0x10.0 5x120\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 20.0x10.5 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(44,'2025-05-21 01:59:35.024626','15','Vossen HF-3',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 20.0x9.0 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 20.0x10.5 5x120\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 21.0x11.0 5x112\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(45,'2025-05-21 01:59:43.066634','14','Work Emotion CR Kai',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 17.0x9.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 18.0x9.5 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 19.0x10.0 5x114.3\", \"fields\": [\"\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u043d\\u0430 \\u0441\\u043a\\u043b\\u0430\\u0434\\u0435\"]}}]',16,5),(46,'2025-05-21 02:17:14.080947','6','Replica RS-1',3,'',16,5),(47,'2025-05-21 02:22:39.578465','11','Aez Kiel',3,'',16,5),(48,'2025-05-21 02:23:53.656168','7','BBS CH-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 18.0x8.0 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 19.0x8.5 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(49,'2025-05-21 02:24:56.237252','12','Dotz Hanzo',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 18.0x8.0 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 19.0x8.5 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Dotz Hanzo 20.0x9.0 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(50,'2025-05-21 02:25:11.362895','9','Enkei RPF1',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Enkei RPF1 16.0x7.0 4x100\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Enkei RPF1 17.0x7.5 4x100\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(51,'2025-05-21 02:25:37.632117','8','OZ Ultraleggera',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"OZ Ultraleggera 17.0x7.5 5x100\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"OZ Ultraleggera 18.0x8.0 5x100\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(52,'2025-05-21 02:25:58.696659','13','Rays Volk Racing TE37',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 17.0x8.0 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 18.0x9.5 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rays Volk Racing TE37 19.0x10.5 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(53,'2025-05-21 02:26:17.683637','10','Rial Lucca',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 17.0x7.5 5x108\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 18.0x8.0 5x108\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rial Lucca 19.0x8.5 5x108\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(54,'2025-05-21 02:26:51.694300','16','Rotiform LAS-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 19.0x8.5 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 19.0x10.0 5x120\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Rotiform LAS-R 20.0x10.5 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(55,'2025-05-21 02:27:17.859832','15','Vossen HF-3',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 20.0x9.0 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 20.0x10.5 5x120\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Vossen HF-3 21.0x11.0 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(56,'2025-05-21 02:27:34.579701','14','Work Emotion CR Kai',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 17.0x9.0 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 18.0x9.5 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"Work Emotion CR Kai 19.0x10.0 5x114.3\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(57,'2025-05-21 02:32:29.758585','7','BBS CH-R',2,'[]',16,5),(58,'2025-05-21 03:39:08.581946','7','BBS CH-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 18.0x8.0 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 19.0x8.5 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(59,'2025-05-21 03:43:20.355467','7','BBS CH-R',2,'[{\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 18.0x8.0 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}, {\"changed\": {\"name\": \"\\u0412\\u0430\\u0440\\u0438\\u0430\\u043d\\u0442 \\u0434\\u0438\\u0441\\u043a\\u0430\", \"object\": \"BBS CH-R 19.0x8.5 5x112\", \"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',16,5),(60,'2025-05-21 04:15:47.771116','8','Bridgestone Turanza T005',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(61,'2025-05-21 04:16:10.092168','15','Continental AllSeasonContact',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(62,'2025-05-21 04:16:34.807989','9','Continental EcoContact 6',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(63,'2025-05-21 04:16:38.395720','2','Continental IceContact 3',2,'[]',7,5),(64,'2025-05-21 04:17:10.051430','2','Continental IceContact 3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(65,'2025-05-21 04:17:54.869737','6','Gislaved Nord Frost 200',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(66,'2025-05-21 04:18:16.876257','11','Goodyear EfficientGrip Performance',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(67,'2025-05-21 04:18:24.841153','5','Goodyear UltraGrip Ice 2',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(68,'2025-05-21 04:18:39.292512','13','Goodyear Vector 4Seasons Gen-3',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(69,'2025-05-21 04:18:59.235924','14','Michelin CrossClimate+',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(70,'2025-05-21 04:19:14.164841','10','Michelin Energy Saver+',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(71,'2025-05-21 04:19:22.678560','7','Michelin Pilot Sport 4',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(72,'2025-05-21 04:19:35.738842','1','Michelin X-Ice North 4',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(73,'2025-05-21 04:19:48.611700','1','Michelin X-Ice North 4',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(74,'2025-05-21 04:19:59.409927','4','Nokian Hakkapeliitta 10',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(75,'2025-05-21 04:20:09.128509','12','Nokian Nordman SX2',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5),(76,'2025-05-21 04:20:18.119643','16','Toyo Proxes R888R',2,'[{\"changed\": {\"fields\": [\"\\u0418\\u0437\\u043e\\u0431\\u0440\\u0430\\u0436\\u0435\\u043d\\u0438\\u0435\"]}}]',7,5);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'cart','cartitem'),(5,'contenttypes','contenttype'),(10,'orders','order'),(11,'orders','orderitem'),(6,'sessions','session'),(14,'tyres','category'),(12,'tyres','favourite'),(18,'tyres','favouriterim'),(15,'tyres','rim'),(16,'tyres','rimmodel'),(17,'tyres','rimvariant'),(13,'tyres','tyreimage'),(7,'tyres','tyremodel'),(8,'tyres','tyrevariant');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-05-05 16:23:10.674649'),(2,'auth','0001_initial','2025-05-05 16:23:42.662796'),(3,'admin','0001_initial','2025-05-05 16:23:48.555186'),(4,'admin','0002_logentry_remove_auto_add','2025-05-05 16:23:48.704095'),(5,'admin','0003_logentry_add_action_flag_choices','2025-05-05 16:23:48.859000'),(6,'contenttypes','0002_remove_content_type_name','2025-05-05 16:23:51.992082'),(7,'auth','0002_alter_permission_name_max_length','2025-05-05 16:23:54.652444'),(8,'auth','0003_alter_user_email_max_length','2025-05-05 16:23:55.018222'),(9,'auth','0004_alter_user_username_opts','2025-05-05 16:23:55.083180'),(10,'auth','0005_alter_user_last_login_null','2025-05-05 16:23:57.173894'),(11,'auth','0006_require_contenttypes_0002','2025-05-05 16:23:57.250846'),(12,'auth','0007_alter_validators_add_error_messages','2025-05-05 16:23:57.407752'),(13,'auth','0008_alter_user_username_max_length','2025-05-05 16:23:59.453913'),(14,'auth','0009_alter_user_last_name_max_length','2025-05-05 16:24:01.021108'),(15,'auth','0010_alter_group_name_max_length','2025-05-05 16:24:01.270952'),(16,'auth','0011_update_proxy_permissions','2025-05-05 16:24:01.411866'),(17,'auth','0012_alter_user_first_name_max_length','2025-05-05 16:24:03.469611'),(20,'sessions','0001_initial','2025-05-05 16:24:14.897980'),(21,'tyres','0002_favourite','2025-05-14 21:44:26.296274'),(28,'tyres','0002_add_variant_id_to_favouriterim','2025-06-08 19:25:51.652330'),(30,'tyres','0001_initial','2025-06-08 20:13:07.463527'),(31,'orders','0001_initial','2025-06-08 20:13:17.320640');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1982scf12s0d7fgbglpwqfepf09oqp53','.eJxVjDsOwjAQBe_iGlmOP_KGkp4zWOvdNQ4gR4qTCnF3iJQC2jcz76USbmtNW5clTazOalCn3y0jPaTtgO_YbrOmua3LlPWu6IN2fZ1ZnpfD_Tuo2Ou3DjyKZwJrgRnIGODsmEWi84VDiSOiN75gdhEJKQA4GwcbGCRE79T7AwkEOG4:1uMai1:SO5qyLAsOqQKvZEfHvo0TctPnP2XtD7d4PNM-crWF8Y','2025-06-17 23:06:17.841053'),('485piojwnn6xndxhzlpqsppme7497v2r','.eJxVjDsOgzAQBe-ydWSBP_JCmT5nQOvdJSaJQMJQIe5OkGho38y8DZjmBdptf0BH65K7tejcDQIt1HDbEvFXxxPIh8b3ZHgal3lI5lTMRYt5TaK_5-XeDjKV_K-DNOqF0VoUQa4qlOREVKPzvYQ-NkS-8j0lF4mJA6KzsbZBUEP0DvYDUEg7ug:1uMaiJ:j-c1RYjr4BsK1DaMo_U2RhAyZbe_b102ybPGTfb8hc0','2025-06-17 23:06:35.736449'),('c867dx1uss61xbzu6eh6j2kfkdzyu1c2','.eJxVjDsOgzAQRO-yNbL8lQ1l-pwBrb0mOIlMYkwRIe4ekGhoppj3ZlYIWCp0K5gjvgvmmuoPOtHAp6QQoQMnOGecw7Y10ONSx36ZY-kT7UzApfMYXjEfgJ6YHxMLU64leXYo7KQzu08U37fTvRyMOI_72lAbNQUnpSNygXNHXhHFaJUeyAy2RdRcD-iVxYDBOKekFdKQi8ZqBdsfYMVF6w:1uC1GP:bjo-W7Jwi7QUimgKGcAUgB8DJ957qnS9prvoOnNfd3Y','2025-05-19 19:14:05.502303'),('qld7n5i1eewx8g6f2s79dgmsnlwuxrui','.eJxVjDsOgzAQBe-ydWSBP_JCmT5nQOvdJSaJQMJQIe5OkGho38y8DZjmBdptf0BH65K7tejcDQIt1HDbEvFXxxPIh8b3ZHgal3lI5lTMRYt5TaK_5-XeDjKV_K-DNOqF0VoUQa4qlOREVKPzvYQ-NkS-8j0lF4mJA6KzsbZBUEP0DvYDUEg7ug:1uMahz:cE_4HlQyfe5E5iEOEDSv2NtGJSqJYqYGCTd_o867NOQ','2025-06-17 23:06:15.215758'),('wqg41tqb87uzwmsorwmf9w9eu6t6odlo','.eJxVjDsOgzAQRO-ydWTh4B-U6TkDWs_agSQCiU-FuHtAokGaat6b2Qg8LVRv-4NaXpeuXec0tb1QTZpuXWR803AC-fDwHhXGYZn6qE5FXXRWzSjp97rc20HHc3esg_WuOAITCzjt4XPpmH1ICNrA4plKZCDbjGysFh_FxYCKXSXaCu1_LAQ77A:1uMcgN:7YadaxkW2YXbWJPGoZxQUBrLdyFDXGvtQ2Dw1011rMk','2025-06-18 01:12:43.847456'),('wtyny2832m6op8cl6j551giqprt0genj','.eJxVjDsOgzAQBe_iOrLiD8ZLmZ4zoPWuHUgikGyoEHePkSiS9s282cWA2zoOW4l5mFh0ohG33y0gveN8An7h_FwkLfOapyBPRV60yH7h-Hlc7l9gxDLWN2jNxAH0XSWLFAxpDMQeI2HyTWvRWWWcCehbZwG46pBUiiYpBQw1SphX0e3H8QVUmjwU:1uOjTX:SksNeYSnGAycuvl0HIZpRbkCEoceyEPKrJXsax6cdPo','2025-06-23 20:52:11.041024'),('xz0nqm3oionjws018jftlbodfpg2pwmk','.eJxVjE0OgyAYRO_CuiFS-dNl957BfAxQbBtIRFfGu1cTF20yq5k3b2MjrUsa1xrmcfKsZ4LdfjtHeId8Dv5F-Vk4Sl7myfET4dda-VB8-Dwu9k-QqKbjbZXRzRFI10ALAxNbTWRsgBUSCvfQIgJRRUSphDfOa2fRke68UKcUNC-s3_b9CynKO-w:1uOLg8:ku9EEineeLAJfLDdkqr2rDhblowgZPQH8EjV1a2op-g','2025-06-22 19:27:36.449585'),('zyje5axkpj75b8t8i94nf9156tfleloj','.eJxVjDsOgzAQBe-ydWTFrLENZfqcAT177ZgkAolPhbh7gkRD-2bmbRQxLdRu-406rEvp1jlNXS_UkqbLFhA_aTiAvDG8RhXHYZn6oA5FnXRWz1HS93G6l4OCufxrD5vqRlccjQNX4rONBjXM3WkDr13IWVJwBiEzrEQwe-8NGq5ZAmj_AS74O6k:1uMcgN:lZM1XtiZiLNGztTKyarRGtu1eSnbRFLIEuHszaSONbo','2025-06-18 01:12:43.531650');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `postal_code` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `note` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_user_id_e9b59eb1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `orders_order_user_id_e9b59eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_orderitem`
--

DROP TABLE IF EXISTS `orders_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `price` decimal(10,2) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `order_id` bigint NOT NULL,
  `rim_id` bigint DEFAULT NULL,
  `tyre_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`),
  KEY `orders_orderitem_rim_id_ff96b004_fk_tyres_rimvariant_id` (`rim_id`),
  KEY `orders_orderitem_tyre_id_532e8551_fk_tyres_tyrevariant_id` (`tyre_id`),
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderitem_rim_id_ff96b004_fk_tyres_rimvariant_id` FOREIGN KEY (`rim_id`) REFERENCES `tyres_rimvariant` (`id`),
  CONSTRAINT `orders_orderitem_tyre_id_532e8551_fk_tyres_tyrevariant_id` FOREIGN KEY (`tyre_id`) REFERENCES `tyres_tyrevariant` (`id`),
  CONSTRAINT `orders_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderitem`
--

LOCK TABLES `orders_orderitem` WRITE;
/*!40000 ALTER TABLE `orders_orderitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_category`
--

DROP TABLE IF EXISTS `tyres_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_category`
--

LOCK TABLES `tyres_category` WRITE;
/*!40000 ALTER TABLE `tyres_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `tyres_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_favourite`
--

DROP TABLE IF EXISTS `tyres_favourite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_favourite` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `added_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `variant_id` bigint NOT NULL,
  `tyre_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tyres_favourite_variant_id_7e67102d_fk_tyres_tyrevariant_id` (`variant_id`),
  KEY `tyres_favourite_user_id_51b65116` (`user_id`),
  KEY `tyres_favourite_tyre_id_ee4c3162_fk_tyres_tyremodel_id` (`tyre_id`),
  CONSTRAINT `tyres_favourite_tyre_id_ee4c3162_fk_tyres_tyremodel_id` FOREIGN KEY (`tyre_id`) REFERENCES `tyres_tyremodel` (`id`),
  CONSTRAINT `tyres_favourite_user_id_51b65116_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `tyres_favourite_variant_id_7e67102d_fk_tyres_tyrevariant_id` FOREIGN KEY (`variant_id`) REFERENCES `tyres_tyrevariant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_favourite`
--

LOCK TABLES `tyres_favourite` WRITE;
/*!40000 ALTER TABLE `tyres_favourite` DISABLE KEYS */;
INSERT INTO `tyres_favourite` VALUES (12,'2025-05-15 19:57:45.928473',3,1,1),(13,'2025-05-15 20:09:59.015090',3,3,1),(15,'2025-05-15 20:17:09.236691',3,4,1),(34,'2025-05-20 21:50:51.898071',5,6,1),(37,'2025-05-22 20:45:57.554781',5,5,1),(41,'2025-06-04 06:55:03.284661',1,31,1);
/*!40000 ALTER TABLE `tyres_favourite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_favouriterim`
--

DROP TABLE IF EXISTS `tyres_favouriterim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_favouriterim` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `rim_variant_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `variant_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tyres_favouriterim_rim_variant_id_4d11daf4_fk_tyres_rim` (`rim_variant_id`),
  KEY `tyres_favouriterim_user_id_1fb80b36` (`user_id`),
  KEY `tyres_favouriterim_variant_id_3d9a533c_fk_tyres_rimvariant_id` (`variant_id`),
  CONSTRAINT `tyres_favouriterim_rim_variant_id_4d11daf4_fk_tyres_rim` FOREIGN KEY (`rim_variant_id`) REFERENCES `tyres_rimvariant` (`id`),
  CONSTRAINT `tyres_favouriterim_user_id_1fb80b36_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `tyres_favouriterim_variant_id_3d9a533c_fk_tyres_rimvariant_id` FOREIGN KEY (`variant_id`) REFERENCES `tyres_rimvariant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_favouriterim`
--

LOCK TABLES `tyres_favouriterim` WRITE;
/*!40000 ALTER TABLE `tyres_favouriterim` DISABLE KEYS */;
INSERT INTO `tyres_favouriterim` VALUES (41,'2025-05-21 06:59:36.190294',14,6,NULL),(52,'2025-05-22 22:30:50.856266',14,5,NULL),(53,'2025-05-22 22:30:52.224102',15,5,NULL),(55,'2025-06-04 07:31:26.175555',14,1,NULL);
/*!40000 ALTER TABLE `tyres_favouriterim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_rimmodel`
--

DROP TABLE IF EXISTS `tyres_rimmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_rimmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `brand` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tyres_rimmo_brand_a7d348_idx` (`brand`,`name`),
  KEY `tyres_rimmodel_name_2d0be4bb` (`name`),
  KEY `tyres_rimmodel_brand_6c01e319` (`brand`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_rimmodel`
--

LOCK TABLES `tyres_rimmodel` WRITE;
/*!40000 ALTER TABLE `tyres_rimmodel` DISABLE KEYS */;
INSERT INTO `tyres_rimmodel` VALUES (7,'CH-R','BBS','Классический дизайн с Y-образными спицами, премиальное качество',''),(8,'Ultraleggera','OZ','Легкосплавные диски с уникальным дизайном, минимальный вес',''),(9,'RPF1','Enkei','Легкие гоночные диски с классическим дизайном',''),(10,'Lucca','Rial','Элегантный дизайн с 10 спицами, отличное соотношение цена/качество',''),(12,'Hanzo','Dotz','Агрессивный дизайн с острыми спицами, стильный внешний вид',''),(13,'Volk Racing TE37','Rays','Культовые кованые диски с уникальным дизайном, легкий вес и высокая прочность',''),(14,'Emotion CR Kai','Work','Современный дизайн с двойными спицами, популярный выбор для тюнинга',''),(15,'HF-3','Vossen','Премиальные диски с уникальным дизайном, идеально подходят для люксовых автомобилей',''),(16,'LAS-R','Rotiform','Стильные диски с агрессивным дизайном, популярны в стэнс-культуре','');
/*!40000 ALTER TABLE `tyres_rimmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_rimvariant`
--

DROP TABLE IF EXISTS `tyres_rimvariant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_rimvariant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `diameter` double NOT NULL,
  `width` double NOT NULL,
  `bolt_pattern` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `offset` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dia` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `color` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `material` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `model_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tyres_rimva_diamete_27acc7_idx` (`diameter`,`width`,`bolt_pattern`),
  KEY `tyres_rimva_price_c036e1_idx` (`price`),
  KEY `tyres_rimvariant_model_id_15bd22a9_fk_tyres_rimmodel_id` (`model_id`),
  CONSTRAINT `tyres_rimvariant_model_id_15bd22a9_fk_tyres_rimmodel_id` FOREIGN KEY (`model_id`) REFERENCES `tyres_rimmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_rimvariant`
--

LOCK TABLES `tyres_rimvariant` WRITE;
/*!40000 ALTER TABLE `tyres_rimvariant` DISABLE KEYS */;
INSERT INTO `tyres_rimvariant` VALUES (14,18,8,'5x112','45','66.6','Серебристый','Алюминий',45000.00,20,'rims/variants/bbschr_Kz5P0FI.jpg',7),(15,19,8.5,'5x112','40','66.6','Черный','Алюминий',52000.00,20,'rims/variants/bbschr_3TPS1p5.jpg',7),(16,17,7.5,'5x100','48','56.1','Серебристый','Алюминий',32000.00,20,'rims/variants/ozracingultraleggera.jpg',8),(17,18,8,'5x100','45','56.1','Черный','Алюминий',38000.00,20,'rims/variants/ozracingultraleggera_iPfMhs0.jpg',8),(18,16,7,'4x100','43','73.1','Серебристый','Алюминий',15000.00,20,'rims/variants/enkeirpf1.jpg',9),(19,17,7.5,'4x100','40','73.1','Черный','Алюминий',18000.00,20,'rims/variants/enkeirpf1_Wu1clpe.jpg',9),(20,17,7.5,'5x108','45','63.4','Серебристый','Алюминий',12000.00,20,'rims/variants/riallucca.jpg',10),(21,18,8,'5x108','40','63.4','Черный','Алюминий',14000.00,20,'rims/variants/riallucca_Gywcn6g.jpg',10),(22,19,8.5,'5x108','35','63.4','Серебристый','Алюминий',16000.00,20,'rims/variants/riallucca_TDzDm4P.jpg',10),(25,18,8,'5x114.3','40','73.1','Черный','Алюминий',22000.00,20,'rims/variants/dotzhanzo.jpg',12),(26,19,8.5,'5x114.3','35','73.1','Серебристый','Алюминий',25000.00,20,'rims/variants/dotzhanzo_JShigJs.jpg',12),(27,20,9,'5x114.3','30','73.1','Черный','Алюминий',28000.00,20,'rims/variants/dotzhanzo_iaMoCbX.jpg',12),(28,17,8,'5x114.3','35','73.1','Бронза','Кованый алюминий',65000.00,20,'rims/variants/TE37.png',13),(29,18,9.5,'5x114.3','22','73.1','Черный','Кованый алюминий',75000.00,20,'rims/variants/TE37_EHBIV9W.png',13),(30,19,10.5,'5x114.3','15','73.1','Бронза','Кованый алюминий',85000.00,20,'rims/variants/TE37_spXQcch.png',13),(31,17,9,'5x114.3','17','73.1','Белый','Алюминий',20000.00,20,'rims/variants/worksrkai.jpg',14),(32,18,9.5,'5x114.3','30','73.1','Матовый бронзовый','Алюминий',24000.00,20,'rims/variants/worksrkai_jV1nVoF.jpg',14),(33,19,10,'5x114.3','25','73.1','Черный','Алюминий',28000.00,20,'rims/variants/worksrkai_vMCZB72.jpg',14),(34,20,9,'5x112','32','66.6','Глянцевый черный','Гибридный кованый',40000.00,20,'rims/variants/vossenhf3.jpg',15),(35,20,10.5,'5x120','42','72.5','Двойной глянцевый черный','Гибридный кованый',45000.00,20,'rims/variants/vossenhf3_1qFMpxK.jpg',15),(36,21,11,'5x112','35','66.6','Глянцевый черный','Гибридный кованый',50000.00,20,'rims/variants/vossenhf3_ya0I6n6.jpg',15),(37,19,8.5,'5x112','35','57.1','Серебристый машинный','Алюминий',25000.00,20,'rims/variants/lasr.jpg',16),(38,19,10,'5x120','40','72.5','Серебристый машинный','Алюминий',28000.00,20,'rims/variants/lasr_3Vm5qC1.jpg',16),(39,20,10.5,'5x112','30','57.1','Черный машинный','Алюминий',32000.00,20,'rims/variants/lasr_Jw9E67y.jpg',16);
/*!40000 ALTER TABLE `tyres_rimvariant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_tyremodel`
--

DROP TABLE IF EXISTS `tyres_tyremodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_tyremodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `brand` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_tyremodel`
--

LOCK TABLES `tyres_tyremodel` WRITE;
/*!40000 ALTER TABLE `tyres_tyremodel` DISABLE KEYS */;
INSERT INTO `tyres_tyremodel` VALUES (1,'X-Ice North 4','Michelin','Зимняя шина с отличным сцеплением на льду.','tyres/michelinx-icenorth4_hxq4suD.jpg'),(2,'IceContact 3','Continental','Современная зимняя шина для суровых условий.','tyres/continentalicecontact3.jpg'),(3,'Blizzak VRX3','Bridgestone','Японская зимняя шина для города и трассы.','tyres/bridgestoneblizzakvrx3.jpg'),(4,'Hakkapeliitta 10','Nokian','Финская шина для суровой зимы.','tyres/nokianhakkapelita10.jpg'),(5,'UltraGrip Ice 2','Goodyear','Зимняя нешипованная шина для легковых авто.','tyres/goodyearultragripice2.jpg'),(6,'Nord Frost 200','Gislaved','Надежная зимняя шина для России.','tyres/gislavednordfrost200.jpg'),(7,'Pilot Sport 4','Michelin','Летняя шина для динамичной езды.','tyres/MichelinPilotSport4.jpg'),(8,'Turanza T005','Bridgestone','Летняя шина для комфорта и безопасности.','tyres/BridgestoneTuranzaT005.jpg'),(9,'EcoContact 6','Continental','Экономичная летняя шина.','tyres/ContinentalEcoContact6.jpg'),(10,'Energy Saver+','Michelin','Летняя шина для экономии топлива.','tyres/MichelinEnergySaver.jpg'),(11,'EfficientGrip Performance','Goodyear','Летняя шина для мокрой дороги.','tyres/GoodyearEfficientGripPerformance.jpg'),(12,'Nordman SX2','Nokian','Бюджетная летняя шина.','tyres/NokianNordmanSX2.jpg'),(13,'Vector 4Seasons Gen-3','Goodyear','Всесезонная шина для любых условий.','tyres/GoodyearVector4SeasonsGen-3.jpg'),(14,'CrossClimate+','Michelin','Всесезонная шина для Европы и России.','tyres/michelincrossclimate.jpg'),(15,'AllSeasonContact','Continental','Всесезонная шина для мягких зим.','tyres/continentalallseasonscontact.jpg'),(16,'Proxes R888R','Toyo','Спортивная полуслик-шина для трека и быстрой езды.','tyres/toyoproxesr888r.jpg');
/*!40000 ALTER TABLE `tyres_tyremodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tyres_tyrevariant`
--

DROP TABLE IF EXISTS `tyres_tyrevariant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tyres_tyrevariant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `width` int NOT NULL,
  `profile` int NOT NULL,
  `radius` int NOT NULL,
  `season` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `studded` tinyint(1) NOT NULL,
  `speed_index` varchar(4) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  `model_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tyres_tyrevariant_model_id_535a923a_fk_tyres_tyremodel_id` (`model_id`),
  CONSTRAINT `tyres_tyrevariant_model_id_535a923a_fk_tyres_tyremodel_id` FOREIGN KEY (`model_id`) REFERENCES `tyres_tyremodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyres_tyrevariant`
--

LOCK TABLES `tyres_tyrevariant` WRITE;
/*!40000 ALTER TABLE `tyres_tyrevariant` DISABLE KEYS */;
INSERT INTO `tyres_tyrevariant` VALUES (1,205,55,16,'winter',1,'T',7500.00,10,1),(2,215,60,17,'winter',0,'H',8200.00,5,1),(3,195,65,15,'winter',1,'T',6900.00,8,2),(4,225,45,18,'winter',0,'V',9900.00,3,2),(5,205,60,16,'winter',0,'H',8100.00,7,3),(6,215,55,17,'winter',1,'T',8700.00,4,3),(7,225,50,17,'winter',1,'H',9500.00,6,4),(8,235,45,18,'winter',0,'V',10200.00,2,4),(9,195,65,15,'winter',0,'T',6700.00,9,5),(10,205,60,16,'winter',0,'H',7300.00,5,5),(11,215,55,16,'winter',1,'T',7900.00,6,6),(12,225,50,17,'winter',1,'H',8600.00,3,6),(13,225,45,17,'summer',0,'W',9800.00,7,7),(14,235,40,18,'summer',0,'Y',11200.00,4,7),(15,205,55,16,'summer',0,'V',7200.00,8,8),(16,215,60,17,'summer',0,'W',8300.00,5,8),(17,195,65,15,'summer',0,'T',6100.00,10,9),(18,205,60,16,'summer',0,'H',6700.00,6,9),(19,185,65,15,'summer',0,'T',5900.00,12,10),(20,195,60,16,'summer',0,'H',6500.00,7,10),(21,205,55,16,'summer',0,'V',7100.00,9,11),(22,215,50,17,'summer',0,'W',8200.00,4,11),(23,195,65,15,'summer',0,'T',5700.00,11,12),(24,205,60,16,'summer',0,'H',6300.00,6,12),(25,205,60,16,'all_season',0,'H',7900.00,8,13),(26,215,55,17,'all_season',0,'V',8700.00,5,13),(27,195,65,15,'all_season',0,'T',8100.00,7,14),(28,205,60,16,'all_season',0,'H',8700.00,4,14),(29,215,55,17,'all_season',0,'V',9200.00,6,15),(30,225,50,18,'all_season',0,'W',9900.00,3,15),(31,195,50,15,'summer',0,'V',9000.00,4,16),(32,205,50,16,'summer',0,'W',9500.00,3,16),(33,215,50,17,'summer',0,'Y',11000.00,2,16),(34,225,50,18,'summer',0,'Y',12000.00,2,16),(35,235,50,18,'summer',0,'Y',12500.00,1,16);
/*!40000 ALTER TABLE `tyres_tyrevariant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-10  0:16:31
