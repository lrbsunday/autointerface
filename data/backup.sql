-- MySQL dump 10.13  Distrib 5.7.21, for osx10.12 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `fields`
--

DROP TABLE IF EXISTS `fields`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fields` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `default` json DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `null` tinyint(1) NOT NULL,
  `unique` tinyint(1) NOT NULL,
  `index` tinyint(1) NOT NULL,
  `foreign` int(11) DEFAULT NULL,
  `on_delete` varchar(255) DEFAULT NULL,
  `model_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `fields_model_id` (`model_id`),
  CONSTRAINT `fields_ibfk_1` FOREIGN KEY (`model_id`) REFERENCES `models` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fields`
--

LOCK TABLES `fields` WRITE;
/*!40000 ALTER TABLE `fields` DISABLE KEYS */;
INSERT INTO `fields` VALUES (1,'2018-10-04 22:13:37','2018-10-04 22:13:37','name','项目名称','null','string',0,0,0,NULL,NULL,1),(3,'2018-10-05 10:35:10','2018-10-05 10:35:10','state','项目状态','1','integer',0,0,0,NULL,NULL,1),(4,'2018-10-05 10:35:33','2018-10-05 10:35:33','description','项目描述','\"\"','text',0,0,0,NULL,NULL,1),(5,'2018-10-05 10:37:43','2018-10-05 10:37:43','name','模型英文名称','null','string',0,0,0,NULL,NULL,2),(6,'2018-10-05 10:37:56','2018-10-05 10:37:56','name_cn','模型中文名称','null','string',0,0,0,NULL,NULL,2),(7,'2018-10-05 10:38:22','2018-10-05 10:38:22','description','模型描述','\"\"','text',0,0,0,NULL,NULL,2),(8,'2018-10-05 10:40:15','2018-10-05 10:40:15','project','所属项目','null','foreign',0,0,0,1,'CASCADE',2),(9,'2018-10-05 10:42:10','2018-10-05 10:42:10','name','','null','string',0,0,0,NULL,NULL,3),(10,'2018-10-05 10:42:32','2018-10-05 10:42:32','description','','\"\"','text',0,0,0,NULL,NULL,3),(11,'2018-10-05 10:43:21','2018-10-05 10:43:21','default','','null','json',1,0,0,NULL,NULL,3),(12,'2018-10-05 10:44:29','2018-10-05 10:44:29','type','','null','string',0,0,0,NULL,NULL,3),(13,'2018-10-05 10:44:55','2018-10-05 10:44:55','null','','false','bool',0,0,0,NULL,NULL,3),(14,'2018-10-05 10:45:11','2018-10-05 10:45:11','unique','','false','bool',0,0,0,NULL,NULL,3),(15,'2018-10-05 10:45:22','2018-10-05 10:45:22','index','','false','bool',0,0,0,NULL,NULL,3),(16,'2018-10-05 10:45:45','2018-10-05 10:45:45','foreign','','null','integer',1,0,0,NULL,NULL,3),(17,'2018-10-05 10:46:10','2018-10-05 10:46:10','on_delete','','null','string',1,0,0,NULL,NULL,3),(18,'2018-10-05 10:47:37','2018-10-05 10:47:37','model','所属模型','null','foreign',0,0,0,2,'CASCADE',3),(19,'2018-10-05 10:49:29','2018-10-05 10:49:29','name','接口英文名称','null','string',0,0,0,NULL,NULL,4),(20,'2018-10-05 10:49:37','2018-10-05 10:49:37','name_cn','接口中文名称','null','string',0,0,0,NULL,NULL,4),(21,'2018-10-05 10:49:58','2018-10-05 10:49:58','method','接口请求方法','null','string',0,0,0,NULL,NULL,4),(22,'2018-10-05 10:50:19','2018-10-05 10:50:19','description','描述信息','\"\"','text',0,0,0,NULL,NULL,4),(23,'2018-10-05 10:51:16','2018-10-05 10:51:16','project','所属项目','null','foreign',0,0,0,1,'CASCADE',4),(24,'2018-10-05 10:51:40','2018-10-05 10:51:40','name','','null','string',0,0,0,NULL,NULL,5),(26,'2018-10-05 10:52:27','2018-10-05 10:52:27','description','','\"\"','text',0,0,0,NULL,NULL,5),(27,'2018-10-05 10:52:44','2018-10-05 10:52:44','need','','true','bool',0,0,0,NULL,NULL,5),(28,'2018-10-05 10:53:09','2018-10-05 10:53:09','default','','null','json',1,0,0,NULL,NULL,5),(29,'2018-10-05 10:53:26','2018-10-05 10:53:26','min','','null','integer',1,0,0,NULL,NULL,5),(30,'2018-10-05 10:53:33','2018-10-05 10:53:33','max','','null','integer',1,0,0,NULL,NULL,5),(31,'2018-10-05 10:53:48','2018-10-05 10:53:48','vtype','','null','string',1,0,0,NULL,NULL,5),(32,'2018-10-05 10:54:48','2018-10-05 10:54:48','function','','\"normal\"','string',0,0,0,NULL,NULL,5),(33,'2018-10-05 10:55:13','2018-10-05 10:55:13','filter_op','','null','string',1,0,0,NULL,NULL,5),(34,'2018-10-05 10:55:30','2018-10-05 10:55:30','filter_condition','','null','string',1,0,0,NULL,NULL,5),(35,'2018-10-05 11:09:28','2018-10-05 11:09:28','interface','所属接口','null','foreign',0,0,0,4,'CASCADE',5),(36,'2018-10-05 21:45:51','2018-10-05 21:45:51','choices','可选值','null','json',1,0,0,NULL,NULL,5);
/*!40000 ALTER TABLE `fields` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interfaces`
--

DROP TABLE IF EXISTS `interfaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interfaces` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `name` varchar(255) NOT NULL,
  `name_cn` varchar(255) NOT NULL,
  `method` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `interfaces_project_id` (`project_id`),
  CONSTRAINT `interfaces_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interfaces`
--

LOCK TABLES `interfaces` WRITE;
/*!40000 ALTER TABLE `interfaces` DISABLE KEYS */;
INSERT INTO `interfaces` VALUES (1,'2018-10-05 19:27:34','2018-10-05 19:27:34','projects','项目','POST','新增项目',1),(2,'2018-10-05 19:27:47','2018-10-05 19:27:47','models','模型','POST','新增模型',1),(3,'2018-10-05 19:28:02','2018-10-05 19:28:02','fields','模型字段','POST','新增模型字段',1),(4,'2018-10-05 19:28:09','2018-10-05 19:28:09','interfaces','接口','POST','新增接口',1),(5,'2018-10-05 19:28:20','2018-10-05 19:28:20','params','接口参数','POST','新增接口参数',1);
/*!40000 ALTER TABLE `interfaces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `models`
--

DROP TABLE IF EXISTS `models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `models` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `name` varchar(255) NOT NULL,
  `name_cn` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `models_project_id` (`project_id`),
  CONSTRAINT `models_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `models`
--

LOCK TABLES `models` WRITE;
/*!40000 ALTER TABLE `models` DISABLE KEYS */;
INSERT INTO `models` VALUES (1,'2018-10-04 21:56:28','2018-10-04 21:56:28','projects','项目','每个项目生成一份代码',1),(2,'2018-10-04 21:57:46','2018-10-04 21:57:46','models','模型','每个数据库表是一个模型，后端使用peewee',1),(3,'2018-10-04 21:58:08','2018-10-04 21:58:08','fields','模型字段','每个数据库字段是一个模型字段',1),(4,'2018-10-04 21:58:17','2018-10-04 21:58:17','interfaces','接口','web接口',1),(5,'2018-10-04 21:58:25','2018-10-04 21:58:25','params','接口参数','web接口参数',1);
/*!40000 ALTER TABLE `models` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `params`
--

DROP TABLE IF EXISTS `params`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `params` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `need` tinyint(1) NOT NULL,
  `default` json DEFAULT NULL,
  `min` int(11) DEFAULT NULL,
  `max` int(11) DEFAULT NULL,
  `choices` json DEFAULT NULL,
  `vtype` varchar(255) DEFAULT NULL,
  `function` varchar(255) NOT NULL,
  `filter_op` varchar(255) DEFAULT NULL,
  `filter_condition` varchar(255) DEFAULT NULL,
  `interface_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `params_interface_id` (`interface_id`),
  CONSTRAINT `params_ibfk_1` FOREIGN KEY (`interface_id`) REFERENCES `interfaces` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `params`
--

LOCK TABLES `params` WRITE;
/*!40000 ALTER TABLE `params` DISABLE KEYS */;
INSERT INTO `params` VALUES (1,'2018-10-05 19:34:49','2018-10-05 19:34:49','name','项目名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,1),(2,'2018-10-05 19:35:03','2018-10-05 19:35:03','state','项目状态',0,'1',NULL,NULL,'null','integer','normal',NULL,NULL,1),(3,'2018-10-05 19:35:13','2018-10-05 19:35:13','description','项目描述',0,'\"\"',NULL,NULL,'null','string','normal',NULL,NULL,1),(4,'2018-10-05 19:36:10','2018-10-05 19:36:10','name','模型英文名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,2),(5,'2018-10-05 19:36:20','2018-10-05 19:36:20','name_cn','模型中文名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,2),(6,'2018-10-05 19:36:41','2018-10-05 19:36:41','description','模型描述',0,'\"\"',NULL,NULL,'null','string','normal',NULL,NULL,2),(7,'2018-10-05 19:37:09','2018-10-05 19:37:09','project_id','所属项目',1,'null',NULL,NULL,'null','integer','normal',NULL,NULL,2),(8,'2018-10-05 19:37:46','2018-10-05 19:37:46','name','',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,3),(9,'2018-10-05 19:38:13','2018-10-05 19:38:13','description','',0,'\"\"',NULL,NULL,'null','string','normal',NULL,NULL,3),(10,'2018-10-05 19:56:11','2018-10-05 19:56:11','default','',0,'null',NULL,NULL,'null',NULL,'normal',NULL,NULL,3),(11,'2018-10-05 19:58:25','2018-10-05 19:58:25','type','',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,3),(12,'2018-10-05 19:59:07','2018-10-05 19:59:07','null','',0,'false',NULL,NULL,'null','bool','normal',NULL,NULL,3),(13,'2018-10-05 19:59:19','2018-10-05 19:59:19','unique','',0,'false',NULL,NULL,'null','bool','normal',NULL,NULL,3),(14,'2018-10-05 19:59:29','2018-10-05 19:59:29','index','',0,'false',NULL,NULL,'null','bool','normal',NULL,NULL,3),(15,'2018-10-05 19:59:48','2018-10-05 19:59:48','foreign','',0,'null',NULL,NULL,'null','integer','normal',NULL,NULL,3),(16,'2018-10-05 20:00:11','2018-10-05 20:00:11','on_delete','',0,'null',NULL,NULL,'null','string','normal',NULL,NULL,3),(17,'2018-10-05 20:00:22','2018-10-05 20:00:22','model_id','所属模型',1,'null',NULL,NULL,'null','integer','normal',NULL,NULL,3),(18,'2018-10-05 20:00:42','2018-10-05 20:00:42','name','接口英文名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,4),(19,'2018-10-05 20:00:53','2018-10-05 20:00:53','name_cn','接口中文名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,4),(20,'2018-10-05 20:01:07','2018-10-05 20:01:07','method','接口请求方法',1,'null',NULL,NULL,'[\"GET\", \"GETS\", \"POST\", \"PUT\", \"DELETE\"]','string','normal',NULL,NULL,4),(21,'2018-10-05 20:01:35','2018-10-05 20:01:35','description','描述信息',0,'\"\"',NULL,NULL,'null','string','normal',NULL,NULL,4),(22,'2018-10-05 20:01:47','2018-10-05 20:01:47','project_id','所属项目',1,'null',NULL,NULL,'null','integer','normal',NULL,NULL,4),(23,'2018-10-05 20:02:01','2018-10-05 20:02:01','name','参数名称',1,'null',NULL,NULL,'null','string','normal',NULL,NULL,5),(24,'2018-10-05 20:02:21','2018-10-05 20:02:21','description','参数描述信息',0,'\"\"',NULL,NULL,'null','string','normal',NULL,NULL,5),(25,'2018-10-05 20:02:37','2018-10-05 20:02:37','need','是否必填',0,'true',NULL,NULL,'null','bool','normal',NULL,NULL,5),(26,'2018-10-05 20:03:05','2018-10-05 20:03:05','default','默认值',0,'null',NULL,NULL,'null',NULL,'normal',NULL,NULL,5),(27,'2018-10-05 20:03:17','2018-10-05 20:03:17','min','最小值',0,'null',NULL,NULL,'null','integer','normal',NULL,NULL,5),(28,'2018-10-05 20:03:26','2018-10-05 20:03:26','max','最大值',0,'null',NULL,NULL,'null','integer','normal',NULL,NULL,5),(29,'2018-10-05 20:03:35','2018-10-05 20:03:35','vtype','参数类型',0,'null',NULL,NULL,'null','string','normal',NULL,NULL,5),(30,'2018-10-05 20:03:47','2018-10-05 20:03:47','choices','可选值',0,'null',NULL,NULL,'null','list','normal',NULL,NULL,5),(31,'2018-10-05 20:04:30','2018-10-05 20:04:30','function','参数用途，filter、sort、page',0,'\"normal\"',NULL,NULL,'[\"normal\", \"filter\", \"sort\", \"page\"]','string','normal',NULL,NULL,5),(32,'2018-10-05 20:04:43','2018-10-05 20:04:43','filter_op','过滤专用，表示过滤操作符',0,'null',NULL,NULL,'null','string','normal',NULL,NULL,5),(33,'2018-10-05 20:04:52','2018-10-05 20:04:52','filter_condition','过滤专用，表示过滤条件',0,'null',NULL,NULL,'null','string','normal',NULL,NULL,5),(34,'2018-10-05 20:05:04','2018-10-05 20:05:04','interface_id','接口外键',1,'null',NULL,NULL,'null','integer','normal',NULL,NULL,5);
/*!40000 ALTER TABLE `params` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `name` varchar(255) NOT NULL,
  `state` int(11) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `projects_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'2018-10-04 21:49:40','2018-10-04 21:49:40','autointerface',1,'自动代码生成工具');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-05 21:48:10
