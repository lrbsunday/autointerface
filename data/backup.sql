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
-- Dumping data for table `fields`
--

LOCK TABLES `fields` WRITE;
/*!40000 ALTER TABLE `fields` DISABLE KEYS */;
INSERT INTO `fields` (`uid`,`create_time`,`update_time`,`name`,`description`,`default`,`type`,`null`,`unique`,`index`,`foreign`,`on_delete`,`model_id`)VALUES (1,'2018-10-04 22:13:37','2018-10-04 22:13:37','name','项目名称','null','string',0,0,0,NULL,NULL,1),(3,'2018-10-05 10:35:10','2018-10-05 10:35:10','state','项目状态','1','integer',0,0,0,NULL,NULL,1),(4,'2018-10-05 10:35:33','2018-10-05 10:35:33','description','项目描述','null','text',0,0,0,NULL,NULL,1),(5,'2018-10-05 10:37:43','2018-10-05 10:37:43','name','模型英文名称','null','string',0,0,0,NULL,NULL,2),(6,'2018-10-05 10:37:56','2018-10-05 10:37:56','name_cn','模型中文名称','null','string',0,0,0,NULL,NULL,2),(7,'2018-10-05 10:38:22','2018-10-05 10:38:22','description','模型描述','null','text',0,0,0,NULL,NULL,2),(8,'2018-10-05 10:40:15','2018-10-05 10:40:15','project','所属项目','null','foreign',0,0,0,1,'CASCADE',2),(9,'2018-10-05 10:42:10','2018-10-05 10:42:10','name','','null','string',0,0,0,NULL,NULL,3),(10,'2018-10-05 10:42:32','2018-10-05 10:42:32','description','','null','text',0,0,0,NULL,NULL,3),(11,'2018-10-05 10:43:21','2018-10-05 10:43:21','default','','null','json',1,0,0,NULL,NULL,3),(12,'2018-10-05 10:44:29','2018-10-05 10:44:29','type','','null','string',0,0,0,NULL,NULL,3),(13,'2018-10-05 10:44:55','2018-10-05 10:44:55','null','','false','bool',0,0,0,NULL,NULL,3),(14,'2018-10-05 10:45:11','2018-10-05 10:45:11','unique','','false','bool',0,0,0,NULL,NULL,3),(15,'2018-10-05 10:45:22','2018-10-05 10:45:22','index','','false','bool',0,0,0,NULL,NULL,3),(16,'2018-10-05 10:45:45','2018-10-05 10:45:45','foreign','','null','integer',1,0,0,NULL,NULL,3),(17,'2018-10-05 10:46:10','2018-10-05 10:46:10','on_delete','','null','string',1,0,0,NULL,NULL,3),(18,'2018-10-05 10:47:37','2018-10-05 10:47:37','model','所属模型','null','foreign',0,0,0,2,'CASCADE',3),(19,'2018-10-05 10:49:29','2018-10-05 10:49:29','name','接口英文名称','null','string',0,0,0,NULL,NULL,4),(20,'2018-10-05 10:49:37','2018-10-05 10:49:37','name_cn','接口中文名称','null','string',0,0,0,NULL,NULL,4),(21,'2018-10-05 10:49:58','2018-10-05 10:49:58','method','接口请求方法','null','string',0,0,0,NULL,NULL,4),(22,'2018-10-05 10:50:19','2018-10-05 10:50:19','description','描述信息','null','text',0,0,0,NULL,NULL,4),(23,'2018-10-05 10:51:16','2018-10-05 10:51:16','project','所属项目','null','foreign',0,0,0,1,'CASCADE',4),(24,'2018-10-05 10:51:40','2018-10-05 10:51:40','name','','null','string',0,0,0,NULL,NULL,5),(26,'2018-10-05 10:52:27','2018-10-05 10:52:27','description','','null','text',0,0,0,NULL,NULL,5),(27,'2018-10-05 10:52:44','2018-10-05 10:52:44','need','','true','bool',0,0,0,NULL,NULL,5),(28,'2018-10-05 10:53:09','2018-10-05 10:53:09','default','','null','json',1,0,0,NULL,NULL,5),(29,'2018-10-05 10:53:26','2018-10-05 10:53:26','min','','null','integer',1,0,0,NULL,NULL,5),(30,'2018-10-05 10:53:33','2018-10-05 10:53:33','max','','null','integer',1,0,0,NULL,NULL,5),(31,'2018-10-05 10:53:48','2018-10-05 10:53:48','vtype','','null','string',1,0,0,NULL,NULL,5),(32,'2018-10-05 10:54:48','2018-10-05 10:54:48','function','','\"normal\"','string',0,0,0,NULL,NULL,5),(33,'2018-10-05 10:55:13','2018-10-05 10:55:13','filter_op','','null','string',1,0,0,NULL,NULL,5),(34,'2018-10-05 10:55:30','2018-10-05 10:55:30','filter_condition','','null','string',1,0,0,NULL,NULL,5),(35,'2018-10-05 11:09:28','2018-10-05 11:09:28','interface','所属接口','null','foreign',0,0,0,4,'CASCADE',5),(36,'2018-10-05 21:45:51','2018-10-05 21:45:51','choices','可选值','null','json',1,0,0,NULL,NULL,5),(37,'2018-10-06 17:02:29','2018-10-06 17:02:29','recurse','返回外键所指对象的内容，仅对查询类接口有效','null','bool',1,0,0,NULL,NULL,4),(38,'2018-10-06 17:09:25','2018-10-06 17:09:25','backref','返回被作为外键的对象列表，仅对查询类接口有','null','bool',1,0,0,NULL,NULL,4),(39,'2018-10-07 20:07:16','2018-10-07 20:07:16','field','','null','foreign',1,0,0,3,'CASCADE',5),(40,'2018-10-10 18:26:16','2018-10-10 18:26:16','max_depth','查询的递归深度，默认为0，表示查询外键对象','0','integer',0,0,0,NULL,NULL,4);
/*!40000 ALTER TABLE `fields` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `interfaces`
--

LOCK TABLES `interfaces` WRITE;
/*!40000 ALTER TABLE `interfaces` DISABLE KEYS */;
INSERT INTO `interfaces` (`uid`,`create_time`,`update_time`,`name`,`name_cn`,`method`,`description`,`project_id`,`recurse`,`backref`,`max_depth`)VALUES (1,'2018-10-05 19:27:34','2018-10-05 19:27:34','projects','项目','POST','新增项目',1,NULL,NULL,0),(2,'2018-10-05 19:27:47','2018-10-05 19:27:47','models','模型','POST','新增模型',1,NULL,NULL,0),(3,'2018-10-05 19:28:02','2018-10-05 19:28:02','fields','模型字段','POST','新增模型字段',1,NULL,NULL,0),(4,'2018-10-05 19:28:09','2018-10-05 19:28:09','interfaces','接口','POST','新增接口',1,NULL,NULL,0),(5,'2018-10-05 19:28:20','2018-10-05 19:28:20','params','接口参数','POST','新增接口参数',1,NULL,NULL,0),(8,'2018-10-06 11:07:55','2018-10-06 11:07:55','interfaces','接口','GET','获取接口详情',1,1,1,1),(9,'2018-10-07 15:53:06','2018-10-07 15:53:06','interfaces','删除接口','DELETE','删除接口',1,NULL,NULL,0),(10,'2018-10-07 15:53:32','2018-10-07 15:53:32','interfaces','更新接口','PUT','更新接口',1,NULL,NULL,0),(13,'2018-10-07 16:06:15','2018-10-07 16:06:15','interfaces','查询接口列表','GETS','查询接口列表',1,1,1,0);
/*!40000 ALTER TABLE `interfaces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `migratehistory`
--

LOCK TABLES `migratehistory` WRITE;
/*!40000 ALTER TABLE `migratehistory` DISABLE KEYS */;
-- INSERT INTO `migratehistory` VALUES (1,'001_auto','2018-10-10 09:03:26'),(30,'002_manuel','2018-10-10 11:21:18'),(31,'003_auto','2018-10-10 11:21:43');
/*!40000 ALTER TABLE `migratehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `models`
--

LOCK TABLES `models` WRITE;
/*!40000 ALTER TABLE `models` DISABLE KEYS */;
INSERT INTO `models` (`uid`,`create_time`,`update_time`,`name`,`name_cn`,`description`,`project_id`)VALUES (1,'2018-10-04 21:56:28','2018-10-04 21:56:28','projects','项目','每个项目生成一份代码',1),(2,'2018-10-04 21:57:46','2018-10-04 21:57:46','models','模型','每个数据库表是一个模型，后端使用peewee',1),(3,'2018-10-04 21:58:08','2018-10-04 21:58:08','fields','模型字段','每个数据库字段是一个模型字段',1),(4,'2018-10-04 21:58:17','2018-10-04 21:58:17','interfaces','接口','web接口',1),(5,'2018-10-04 21:58:25','2018-10-04 21:58:25','params','接口参数','web接口参数',1);
/*!40000 ALTER TABLE `models` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `params`
--

LOCK TABLES `params` WRITE;
/*!40000 ALTER TABLE `params` DISABLE KEYS */;
INSERT INTO `params` (`uid`,`create_time`,`update_time`,`name`,`description`,`need`,`default`,`min`,`max`,`vtype`,`function`,`filter_op`,`filter_condition`,`interface_id`,`choices`,`field_id`)VALUES (1,'2018-10-05 19:34:49','2018-10-05 19:34:49','name','项目名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,1,'null',NULL),(2,'2018-10-05 19:35:03','2018-10-05 19:35:03','state','项目状态',0,'1',NULL,NULL,'integer','normal',NULL,NULL,1,'null',NULL),(3,'2018-10-05 19:35:13','2018-10-05 19:35:13','description','项目描述',0,'\"\"',NULL,NULL,'string','normal',NULL,NULL,1,'null',NULL),(4,'2018-10-05 19:36:10','2018-10-05 19:36:10','name','模型英文名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,2,'null',NULL),(5,'2018-10-05 19:36:20','2018-10-05 19:36:20','name_cn','模型中文名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,2,'null',NULL),(6,'2018-10-05 19:36:41','2018-10-05 19:36:41','description','模型描述',0,'\"\"',NULL,NULL,'string','normal',NULL,NULL,2,'null',NULL),(7,'2018-10-05 19:37:09','2018-10-05 19:37:09','project_id','所属项目',1,'null',NULL,NULL,'integer','normal',NULL,NULL,2,'null',NULL),(8,'2018-10-05 19:37:46','2018-10-05 19:37:46','name','',1,'null',NULL,NULL,'string','normal',NULL,NULL,3,'null',NULL),(9,'2018-10-05 19:38:13','2018-10-05 19:38:13','description','',0,'\"\"',NULL,NULL,'string','normal',NULL,NULL,3,'null',NULL),(10,'2018-10-05 19:56:11','2018-10-05 19:56:11','default','',0,'null',NULL,NULL,NULL,'normal',NULL,NULL,3,'null',NULL),(11,'2018-10-05 19:58:25','2018-10-05 19:58:25','type','',1,'null',NULL,NULL,'string','normal',NULL,NULL,3,'null',NULL),(12,'2018-10-05 19:59:07','2018-10-05 19:59:07','null','',0,'false',NULL,NULL,'bool','normal',NULL,NULL,3,'null',NULL),(13,'2018-10-05 19:59:19','2018-10-05 19:59:19','unique','',0,'false',NULL,NULL,'bool','normal',NULL,NULL,3,'null',NULL),(14,'2018-10-05 19:59:29','2018-10-05 19:59:29','index','',0,'false',NULL,NULL,'bool','normal',NULL,NULL,3,'null',NULL),(15,'2018-10-05 19:59:48','2018-10-05 19:59:48','foreign','',0,'null',NULL,NULL,'integer','normal',NULL,NULL,3,'null',NULL),(16,'2018-10-05 20:00:11','2018-10-05 20:00:11','on_delete','',0,'null',NULL,NULL,'string','normal',NULL,NULL,3,'null',NULL),(17,'2018-10-05 20:00:22','2018-10-05 20:00:22','model_id','所属模型',1,'null',NULL,NULL,'integer','normal',NULL,NULL,3,'null',NULL),(18,'2018-10-05 20:00:42','2018-10-05 20:00:42','name','接口英文名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,4,'null',NULL),(19,'2018-10-05 20:00:53','2018-10-05 20:00:53','name_cn','接口中文名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,4,'null',NULL),(20,'2018-10-05 20:01:07','2018-10-05 20:01:07','method','接口请求方法',1,'null',NULL,NULL,'string','normal',NULL,NULL,4,'[\"GET\", \"GETS\", \"POST\", \"PUT\", \"DELETE\"]',NULL),(21,'2018-10-05 20:01:35','2018-10-05 20:01:35','description','描述信息',0,'\"\"',NULL,NULL,'string','normal',NULL,NULL,4,'null',NULL),(22,'2018-10-05 20:01:47','2018-10-05 20:01:47','project_id','所属项目',1,'null',NULL,NULL,'integer','normal',NULL,NULL,4,'null',NULL),(23,'2018-10-05 20:02:01','2018-10-05 20:02:01','name','参数名称',1,'null',NULL,NULL,'string','normal',NULL,NULL,5,'null',NULL),(24,'2018-10-05 20:02:21','2018-10-05 20:02:21','description','参数描述信息',0,'\"\"',NULL,NULL,'string','normal',NULL,NULL,5,'null',NULL),(25,'2018-10-05 20:02:37','2018-10-05 20:02:37','need','是否必填',0,'true',NULL,NULL,'bool','normal',NULL,NULL,5,'null',NULL),(26,'2018-10-05 20:03:05','2018-10-05 20:03:05','default','默认值',0,'null',NULL,NULL,NULL,'normal',NULL,NULL,5,'null',NULL),(27,'2018-10-05 20:03:17','2018-10-05 20:03:17','min','最小值',0,'null',NULL,NULL,'integer','normal',NULL,NULL,5,'null',NULL),(28,'2018-10-05 20:03:26','2018-10-05 20:03:26','max','最大值',0,'null',NULL,NULL,'integer','normal',NULL,NULL,5,'null',NULL),(29,'2018-10-05 20:03:35','2018-10-05 20:03:35','vtype','参数类型',0,'null',NULL,NULL,'string','normal',NULL,NULL,5,'null',NULL),(30,'2018-10-05 20:03:47','2018-10-05 20:03:47','choices','可选值',0,'null',NULL,NULL,'list','normal',NULL,NULL,5,'null',NULL),(31,'2018-10-05 20:04:30','2018-10-05 20:04:30','function','参数用途，filter、sort、page',0,'\"normal\"',NULL,NULL,'string','normal',NULL,NULL,5,'[\"normal\", \"filter\", \"sort\", \"page\", \"size\"]',NULL),(32,'2018-10-05 20:04:43','2018-10-05 20:04:43','filter_op','过滤专用，表示过滤操作符',0,'null',NULL,NULL,'string','normal',NULL,NULL,5,'null',NULL),(33,'2018-10-05 20:04:52','2018-10-05 20:04:52','filter_condition','过滤专用，表示过滤条件',0,'null',NULL,NULL,'string','normal',NULL,NULL,5,'null',NULL),(34,'2018-10-05 20:05:04','2018-10-05 20:05:04','interface_id','接口外键',1,'null',NULL,NULL,'integer','normal',NULL,NULL,5,'null',NULL),(35,'2018-10-06 17:06:22','2018-10-06 17:06:22','recurse','返回外键所指对象的内容，仅对查询类接口有效',0,'null',NULL,NULL,'bool','normal',NULL,NULL,4,'null',NULL),(36,'2018-10-06 17:09:00','2018-10-06 17:09:00','backref','返回被作为外键的对象列表，仅对查询类接口有效',0,'null',NULL,NULL,'bool','normal',NULL,NULL,4,'null',NULL),(37,'2018-10-07 15:55:07','2018-10-07 15:55:07','name','接口名称',0,'null',NULL,NULL,'string','normal',NULL,NULL,10,'null',NULL),(38,'2018-10-07 15:55:45','2018-10-07 15:55:45','name_cn','接口中文名称',0,'null',NULL,NULL,'string','normal',NULL,NULL,10,'null',NULL),(39,'2018-10-07 15:55:58','2018-10-07 15:55:58','method','接口请求方法',0,'null',NULL,NULL,'string','normal',NULL,NULL,10,'null',NULL),(40,'2018-10-07 15:56:12','2018-10-07 15:56:12','description','接口描述信息',0,'null',NULL,NULL,'string','normal',NULL,NULL,10,'null',NULL),(41,'2018-10-07 15:56:55','2018-10-07 15:56:55','recurse','是否返回外键所指对象',0,'null',NULL,NULL,'bool','normal',NULL,NULL,10,'null',NULL),(42,'2018-10-07 15:57:48','2018-10-07 15:57:48','backref','',0,'null',NULL,NULL,'bool','normal',NULL,NULL,10,'null',NULL),(43,'2018-10-07 16:20:22','2018-10-07 16:20:22','name','按接口名称前缀过滤',0,'null',NULL,NULL,'string','filter','.startswith',NULL,13,'null',NULL),(44,'2018-10-07 16:36:27','2018-10-07 16:36:27','method','按接口方法查询',0,'null',NULL,NULL,'string','filter',NULL,NULL,13,'[\"GET\", \"GETS\", \"POST\", \"PUT\", \"DELETE\"]',NULL),(45,'2018-10-07 16:40:47','2018-10-07 16:40:47','project_id','按项目ID查询',0,'null',NULL,NULL,'integer','filter',NULL,NULL,13,'null',NULL),(46,'2018-10-07 16:43:53','2018-10-07 16:43:53','s_name','按名称排序',0,'null',NULL,NULL,'string','sort',NULL,NULL,13,'null',19),(47,'2018-10-07 20:13:39','2018-10-07 20:13:39','field_id','与接口字段相关的模型字段',0,'null',NULL,NULL,'integer','normal',NULL,NULL,5,'null',NULL),(48,'2018-10-07 21:23:45','2018-10-07 21:23:45','project_name','',0,'null',NULL,NULL,'string','filter',NULL,NULL,13,'null',1),(49,'2018-10-07 21:45:30','2018-10-07 21:45:30','p','分页参数，页数',0,'1',NULL,NULL,'integer','page',NULL,NULL,13,'null',NULL),(50,'2018-10-07 21:46:48','2018-10-07 21:46:48','s','分页参数，每页条数',0,'10',NULL,NULL,'integer','size',NULL,NULL,13,'null',NULL),(51,'2018-10-10 18:27:35','2018-10-10 18:27:35','max_depth','查询的递归深度，默认为0，表示查询外键对',0,'0',NULL,NULL,'integer','normal',NULL,NULL,10,'null',NULL),(52,'2018-10-10 20:21:38','2018-10-10 20:21:38','s_method','按请求方法排序',0,'null',NULL,NULL,'string','sort',NULL,NULL,13,'null',21);
/*!40000 ALTER TABLE `params` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` (`uid`,`create_time`,`update_time`,`name`,`state`,`description`)VALUES (1,'2018-10-04 21:49:40','2018-10-04 21:49:40','autointerface',1,'自动代码生成工具');
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

-- Dump completed on 2018-10-13  9:34:42
