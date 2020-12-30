-- MySQL dump 10.13  Distrib 8.0.22, for osx10.15 (x86_64)
--
-- Host: localhost    Database: Dneuro
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `auth_numbers`
--

DROP TABLE IF EXISTS `auth_numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_numbers` (
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `auth_number` int NOT NULL,
  PRIMARY KEY (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_numbers`
--

LOCK TABLES `auth_numbers` WRITE;
/*!40000 ALTER TABLE `auth_numbers` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_numbers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_kor` varchar(45) NOT NULL,
  `name_eng` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (2,'대한민국','KOREA');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(2,'sessions','session'),(6,'survey','category'),(7,'survey','effectivedate'),(8,'survey','evasiongrade'),(9,'survey','investtype'),(12,'survey','result'),(10,'survey','survey'),(11,'survey','usersurvey'),(3,'user','authsms'),(4,'user','country'),(5,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-12-29 02:44:40.235690'),(2,'contenttypes','0002_remove_content_type_name','2020-12-29 02:44:40.312314'),(3,'sessions','0001_initial','2020-12-29 02:44:40.342378'),(4,'user','0001_initial','2020-12-29 02:44:40.412602'),(5,'survey','0001_initial','2020-12-29 02:44:40.596970');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `effective_dates`
--

DROP TABLE IF EXISTS `effective_dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `effective_dates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start_at` date DEFAULT NULL,
  `end_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `effective_dates`
--

LOCK TABLES `effective_dates` WRITE;
/*!40000 ALTER TABLE `effective_dates` DISABLE KEYS */;
INSERT INTO `effective_dates` VALUES (2,'2020-12-01','2020-12-31');
/*!40000 ALTER TABLE `effective_dates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evasion_grade`
--

DROP TABLE IF EXISTS `evasion_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evasion_grade` (
  `id` int NOT NULL AUTO_INCREMENT,
  `grade` int NOT NULL,
  `tendency` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evasion_grade`
--

LOCK TABLES `evasion_grade` WRITE;
/*!40000 ALTER TABLE `evasion_grade` DISABLE KEYS */;
INSERT INTO `evasion_grade` VALUES (1,1,'극도로 높은 {0} 회피 경향'),(2,2,'매우 높은 {0} 회피 경향'),(3,3,'높은 회피 {0} 경향'),(4,4,'보통의 {0} 회피 경향'),(5,5,'낮은 {0} 회피 경향'),(6,6,'매우 {0} 낮은 회피 경향'),(7,7,'극도로 낮은 {0} 회피 경향'),(8,1,'극도로 높은 {0} 회피 경향'),(9,2,'매우 높은 {0} 회피 경향'),(10,3,'높은 회피 {0} 경향'),(11,4,'보통의 {0} 회피 경향'),(12,5,'낮은 {0} 회피 경향'),(13,6,'매우 {0} 낮은 회피 경향'),(14,7,'극도로 낮은 {0} 회피 경향');
/*!40000 ALTER TABLE `evasion_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invest_types`
--

DROP TABLE IF EXISTS `invest_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invest_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invest_types`
--

LOCK TABLES `invest_types` WRITE;
/*!40000 ALTER TABLE `invest_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `invest_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` longtext,
  `effective_date_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `results_effective_date_id_fa72147f_fk_effective_dates_id` (`effective_date_id`),
  KEY `results_user_id_1a41824a_fk_users_id` (`user_id`),
  CONSTRAINT `results_effective_date_id_fa72147f_fk_effective_dates_id` FOREIGN KEY (`effective_date_id`) REFERENCES `effective_dates` (`id`),
  CONSTRAINT `results_user_id_1a41824a_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_categories`
--

DROP TABLE IF EXISTS `survey_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_categories`
--

LOCK TABLES `survey_categories` WRITE;
/*!40000 ALTER TABLE `survey_categories` DISABLE KEYS */;
INSERT INTO `survey_categories` VALUES (1,'금융지식평가'),(2,'위험회피평가'),(3,'손실회피평'),(4,'금융지식평가'),(5,'위험회피평가'),(6,'손실회피평');
/*!40000 ALTER TABLE `survey_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surveys`
--

DROP TABLE IF EXISTS `surveys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `surveys` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `category_id` int NOT NULL,
  `effective_date_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `surveys_category_id_adb5fe00_fk_survey_categories_id` (`category_id`),
  KEY `surveys_effective_date_id_d43f5a25_fk_effective_dates_id` (`effective_date_id`),
  CONSTRAINT `surveys_category_id_adb5fe00_fk_survey_categories_id` FOREIGN KEY (`category_id`) REFERENCES `survey_categories` (`id`),
  CONSTRAINT `surveys_effective_date_id_d43f5a25_fk_effective_dates_id` FOREIGN KEY (`effective_date_id`) REFERENCES `effective_dates` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surveys`
--

LOCK TABLES `surveys` WRITE;
/*!40000 ALTER TABLE `surveys` DISABLE KEYS */;
INSERT INTO `surveys` VALUES (14,'회사채를 사는 경우, 회사채 만기까지만 기다리면 투자금을 언제나 받을 수 있다.|(A)True|(B)False',4,2),(15,'주식 배당금액은 회사의 성과에 따라 변할 수 있다.|(A)True|(B)False',4,2),(16,'투자에서 높은 수익을 원한다면 위험을 더 취해야 한다.|(A)True|(B)False',4,2),(17,'TV게임쇼에 참가했다고 생각하시고 다음 중 하나를 고르세요.|(A)  30% 의 확률로 $14,000를 얻는 선택|(B) 확실히 $3,100 받기',5,2),(18,'좋습니다! 지금 또 다른 선택의 기회가 있습니다.|(A) 20% 의 확률로 $12,000 받기|(B) 그냥 $2,300 받고 끝내기',5,2),(19,'지금 다음 중 하나를 골라야 합니다.|(A)  10% 의 확률로 $7,000 를 얻는 것을 시도합니다.|(B) 그냥 $970 받고 만족합니다.',5,2),(20,'이런 경우는 무엇을 선택하시겠습니까?|(A)  20% 의 확률로 $11,000 를 받을 수 있는 복권|(B) 그냥 $1,700 받고 끝내기',5,2),(21,'마지막으로 둘 중 하나를 선택해야 한다면?|(A) 20% 의 확률로 $11,000 를 받기에 도전하기|(B) 아니면 $1,200 으로 만족하기',5,2),(22,'다음 주 무엇을 선호하십니까?|(A) 70% 의 확률로 $14,000 얻거나  30% 의 확률로 $2,000 잃는 선택|(B)  $5,800 얻는 선택',6,2),(23,'다음 중에서는 무엇을 선택하시겠습니까?|(A) 70% 의 확률로 $10,000 을 받거나  30% 의 확률로 $2,000의 벌금을 내는 선택|(B)  $3,100 받고 끝내는 선택',6,2),(24,'다음의 경우, 무엇을 선택하시겠습니까?|(A) 90%  의 확률로 $14,000 를 벌고  10% 의 확률로 $4,000 를 잃는 선택|(B) 확실히 $7,200 받는 선택',6,2),(25,'다음의 선택은 어떻습니까?|(A) 60% 의 확률로 $10,000 받거나  40% 의 확률로  $4,000를 내야 하는 선택|(B)  $110 로 만족하는 선택',6,2),(26,'둘 중 하나를 선택해야 합니다.|(A) 60% 의 확률로 $13,000  따거나  40% 의 확률로 $2,000를 잃는 선택|(B)  $110 로 만족하는 선택',6,2);
/*!40000 ALTER TABLE `surveys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `kakao_id` varchar(45) DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_country_id_df94ce74_fk_countries_id` (`country_id`),
  CONSTRAINT `users_country_id_df94ce74_fk_countries_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_surveys`
--

DROP TABLE IF EXISTS `users_surveys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_surveys` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` int DEFAULT NULL,
  `answer` varchar(45) DEFAULT NULL,
  `create_at` datetime(6) NOT NULL,
  `survey_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_surveys_survey_id_17431a28_fk_surveys_id` (`survey_id`),
  KEY `users_surveys_user_id_bb624c4e_fk_users_id` (`user_id`),
  CONSTRAINT `users_surveys_survey_id_17431a28_fk_surveys_id` FOREIGN KEY (`survey_id`) REFERENCES `surveys` (`id`),
  CONSTRAINT `users_surveys_user_id_bb624c4e_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_surveys`
--

LOCK TABLES `users_surveys` WRITE;
/*!40000 ALTER TABLE `users_surveys` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_surveys` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-29 12:59:53
