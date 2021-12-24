-- MySQL dump 10.13  Distrib 8.0.27, for macos11.6 (x86_64)
--
-- Host: 127.0.0.1    Database: yearsinpixels
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `day`
--

DROP TABLE IF EXISTS `day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `day` (
  `id_user` int unsigned NOT NULL COMMENT 'This table holds all data of the different days from the users',
  `date` date NOT NULL,
  `title` text COLLATE utf8_bin,
  `notes` text COLLATE utf8_bin,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_mood1` int unsigned NOT NULL,
  `id_mood2` int unsigned DEFAULT NULL,
  PRIMARY KEY (`date`,`id_user`),
  KEY `tbl.day.user_id_idx` (`id_user`),
  KEY `tblday_fk_id_mood_idx` (`id_mood1`,`id_mood2`),
  KEY `tblday_fk_id_mood2` (`id_mood2`),
  CONSTRAINT `tblday_fk_id_mood1` FOREIGN KEY (`id_mood1`) REFERENCES `mood` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `tblday_fk_id_mood2` FOREIGN KEY (`id_mood2`) REFERENCES `mood` (`id`),
  CONSTRAINT `tblday_fk_id_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `day`
--

LOCK TABLES `day` WRITE;
/*!40000 ALTER TABLE `day` DISABLE KEYS */;
INSERT INTO `day` VALUES (1,'2021-12-21','My day was awesome!!!','asfd','2021-12-21 16:45:58','2021-12-21 16:45:58',3,NULL),(1,'2021-12-23','Fantastisch!a','','2021-12-23 13:21:23','2021-12-23 13:21:23',1,NULL),(1,'2021-12-24','super!','nice','2021-12-24 09:07:38','2021-12-24 09:07:38',4,NULL);
/*!40000 ALTER TABLE `day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mood`
--

DROP TABLE IF EXISTS `mood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mood` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` text COLLATE utf8_bin,
  `color` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT 'Hex',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mood`
--

LOCK TABLES `mood` WRITE;
/*!40000 ALTER TABLE `mood` DISABLE KEYS */;
INSERT INTO `mood` VALUES (1,'fantastisch','10271907'),(2,'sehr gut','10271907'),(3,'normal','12032199'),(4,'ermüdend','8441320'),(5,'frustrierend','12275286'),(6,'stressig','14591881');
/*!40000 ALTER TABLE `mood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_user` int unsigned NOT NULL,
  `username` varchar(45) COLLATE utf8_bin NOT NULL,
  `link_profilepicture` text COLLATE utf8_bin,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,1,'some',NULL,'2021-08-04 13:08:38');
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `guid` varchar(45) COLLATE utf8_bin NOT NULL,
  `email` varchar(128) COLLATE utf8_bin NOT NULL,
  `email_verified` tinyint(1) NOT NULL DEFAULT '0',
  `name_first` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `name_last` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `gender` int unsigned DEFAULT NULL,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `password_last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `enabled` tinyint NOT NULL DEFAULT '0',
  `twofatoken` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `login_last` timestamp NULL DEFAULT NULL,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `guid_UNIQUE` (`guid`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'17743754-5192-423f-a5ab-1797fb674081','daniel',1,'Daniel','Gran',NULL,'$argon2id$v=19$m=65536,t=3,p=4$GQh8SeEFz1LkPd1N5QI8CA$gBuHn2hh+DlMyeRarBpAEJnoVlTzf/2AAZ1UD3vmU4c','2021-12-18 12:15:35',1,'','2021-12-18 12:15:35','2021-12-18 12:15:35','2021-12-18 12:15:35');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-24 11:25:44
