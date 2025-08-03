-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 02, 2025 at 06:47 PM
-- Server version: 8.0.42-0ubuntu0.24.04.1
-- PHP Version: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `efileCabinet_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add custom user', 6, 'add_customuser'),
(22, 'Can change custom user', 6, 'change_customuser'),
(23, 'Can delete custom user', 6, 'delete_customuser'),
(24, 'Can view custom user', 6, 'view_customuser'),
(25, 'Can add role', 7, 'add_role'),
(26, 'Can change role', 7, 'change_role'),
(27, 'Can delete role', 7, 'delete_role'),
(28, 'Can view role', 7, 'view_role'),
(29, 'Can add workunit list', 8, 'add_workunitlist'),
(30, 'Can change workunit list', 8, 'change_workunitlist'),
(31, 'Can delete workunit list', 8, 'delete_workunitlist'),
(32, 'Can view workunit list', 8, 'view_workunitlist'),
(33, 'Can add kebele', 9, 'add_kebele'),
(34, 'Can change kebele', 9, 'change_kebele'),
(35, 'Can delete kebele', 9, 'delete_kebele'),
(36, 'Can view kebele', 9, 'view_kebele'),
(37, 'Can add nation', 10, 'add_nation'),
(38, 'Can change nation', 10, 'change_nation'),
(39, 'Can delete nation', 10, 'delete_nation'),
(40, 'Can view nation', 10, 'view_nation'),
(41, 'Can add region', 11, 'add_region'),
(42, 'Can change region', 11, 'change_region'),
(43, 'Can delete region', 11, 'delete_region'),
(44, 'Can view region', 11, 'view_region'),
(45, 'Can add woreda', 12, 'add_woreda'),
(46, 'Can change woreda', 12, 'change_woreda'),
(47, 'Can delete woreda', 12, 'delete_woreda'),
(48, 'Can view woreda', 12, 'view_woreda'),
(49, 'Can add zone', 13, 'add_zone'),
(50, 'Can change zone', 13, 'change_zone'),
(51, 'Can delete zone', 13, 'delete_zone'),
(52, 'Can view zone', 13, 'view_zone'),
(53, 'Can add notifiable users', 14, 'add_notifiableusers'),
(54, 'Can change notifiable users', 14, 'change_notifiableusers'),
(55, 'Can delete notifiable users', 14, 'delete_notifiableusers'),
(56, 'Can view notifiable users', 14, 'view_notifiableusers'),
(57, 'Can add notification', 15, 'add_notification'),
(58, 'Can change notification', 15, 'change_notification'),
(59, 'Can delete notification', 15, 'delete_notification'),
(60, 'Can view notification', 15, 'view_notification'),
(61, 'Can add system notification', 16, 'add_systemnotification'),
(62, 'Can change system notification', 16, 'change_systemnotification'),
(63, 'Can delete system notification', 16, 'delete_systemnotification'),
(64, 'Can view system notification', 16, 'view_systemnotification');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(6, 'app', 'customuser'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(9, 'demographic', 'kebele'),
(10, 'demographic', 'nation'),
(11, 'demographic', 'region'),
(12, 'demographic', 'woreda'),
(13, 'demographic', 'zone'),
(14, 'notification', 'notifiableusers'),
(15, 'notification', 'notification'),
(16, 'notification', 'systemnotification'),
(5, 'sessions', 'session'),
(7, 'superAdmin', 'role'),
(8, 'superAdmin', 'workunitlist');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-08-02 13:25:59.721713'),
(2, 'superAdmin', '0001_initial', '2025-08-02 13:25:59.754374'),
(3, 'contenttypes', '0002_remove_content_type_name', '2025-08-02 13:25:59.869702'),
(4, 'auth', '0001_initial', '2025-08-02 13:26:00.217554'),
(5, 'auth', '0002_alter_permission_name_max_length', '2025-08-02 13:26:00.293259'),
(6, 'auth', '0003_alter_user_email_max_length', '2025-08-02 13:26:00.325900'),
(7, 'auth', '0004_alter_user_username_opts', '2025-08-02 13:26:00.336257'),
(8, 'auth', '0005_alter_user_last_login_null', '2025-08-02 13:26:00.346722'),
(9, 'auth', '0006_require_contenttypes_0002', '2025-08-02 13:26:00.350449'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2025-08-02 13:26:00.361737'),
(11, 'auth', '0008_alter_user_username_max_length', '2025-08-02 13:26:00.372050'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2025-08-02 13:26:00.384240'),
(13, 'auth', '0010_alter_group_name_max_length', '2025-08-02 13:26:00.405625'),
(14, 'auth', '0011_update_proxy_permissions', '2025-08-02 13:26:00.419338'),
(15, 'auth', '0012_alter_user_first_name_max_length', '2025-08-02 13:26:00.429372'),
(16, 'app', '0001_initial', '2025-08-02 13:26:00.936231'),
(17, 'admin', '0001_initial', '2025-08-02 13:26:01.123960'),
(18, 'admin', '0002_logentry_remove_auto_add', '2025-08-02 13:26:01.139286'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-02 13:26:01.153844'),
(20, 'app', '0002_remove_customuser_otp_and_more', '2025-08-02 13:26:01.404742'),
(21, 'demographic', '0001_initial', '2025-08-02 13:26:01.529039'),
(22, 'notification', '0001_initial', '2025-08-02 13:26:01.607041'),
(23, 'sessions', '0001_initial', '2025-08-02 13:26:01.655572'),
(24, 'superAdmin', '0002_workunitlist', '2025-08-02 13:26:01.684434'),
(25, 'app', '0003_remove_customuser_cell_customuser_otp_and_more', '2025-08-02 13:41:11.535141');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('mctbx5lqwgi1gtjbyk4tgzec9rexwozp', '.eJxVjEEOgjAQRe_StWlmOtIOLt1zhmaYFosaSCisjHdXEha6_e-9_zJRtrXEreYljslcjDOn360XfeRpB-ku0222Ok_rMvZ2V-xBq-3mlJ_Xw_07KFLLtw6gzg8JyKuoY4_KmgJiS6FpOLMGPFOrTAxMqOJahECDxx5ACNi8P8HdNno:1uiCUj:P5BnfxdEOwOzGt38AR8g5ReyfUPkcgZDrpJT4l_0kYg', '2025-08-16 13:41:53.576244');

-- --------------------------------------------------------

--
-- Table structure for table `kebele`
--

CREATE TABLE `kebele` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nation`
--

CREATE TABLE `nation` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notifiable_user`
--

CREATE TABLE `notifiable_user` (
  `id` bigint NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id` bigint NOT NULL,
  `holder` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `region`
--

CREATE TABLE `region` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` bigint NOT NULL,
  `role_name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `role_name`, `description`, `soft_delete`, `created_at`, `updated_at`) VALUES
(1, 'Super Admin', 'Super Admin Role', '0', '2025-08-02 18:45:41.687439', '2025-08-02 18:45:41.687444'),
(2, 'website Administrator', 'A website Administrator is a person who manages the static pages on the system', '1', '2025-08-02 09:11:06.376177', '2025-08-02 09:11:06.376181'),
(3, 'Author', 'An Author is a person who writes contents of website', '1', '2025-08-02 13:49:38.881659', '2025-08-02 13:49:38.881666'),
(4, 'Subscriber', 'A Subscriber is a guest for this system ', '1', '2025-08-02 13:49:53.243347', '2025-08-02 13:49:53.243352'),
(5, 'Documentation Officer', 'Main documentation officer at organization level', '0', '2025-08-02 16:08:22.565841', '2025-08-02 16:08:22.565864'),
(6, 'Work-unit Executive', 'Work-unit Executive', '0', '2025-08-02 16:09:32.841794', '2025-08-02 16:09:32.841830'),
(7, 'Work-unit documentation officer', 'Documentation officer at workunit level', '0', '2025-08-02 16:10:20.936862', '2025-08-02 16:10:20.936884');

-- --------------------------------------------------------

--
-- Table structure for table `system_notification`
--

CREATE TABLE `system_notification` (
  `id` bigint NOT NULL,
  `recipient` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `read` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(150) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(100) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `user_profile` varchar(100) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `last_password_change` datetime(6) DEFAULT NULL,
  `user_roles_id` bigint NOT NULL,
  `otp` varchar(255) NOT NULL,
  `password_change_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `password`, `last_login`, `username`, `date_joined`, `email`, `first_name`, `last_name`, `is_superuser`, `is_active`, `is_staff`, `user_profile`, `soft_delete`, `last_password_change`, `user_roles_id`, `otp`, `password_change_status`) VALUES
(2, 'pbkdf2_sha256$1000000$0pfYs7a1KGHw0CxooAwkZH$U6Ts1bDNN+I+ZZzQIZSwFkR5vaP0/5F0z6vQ1caWREo=', '2025-08-02 13:41:53.565836', 'Super@astu.edu.et', '2025-07-06 16:21:56.000000', 'kemal.nure@astu.edu.et', 'Super', 'Admin', 1, 1, 1, 'profile_pic/team-4_ooPwbqR.jpg', '0', '2025-07-06 13:22:07.421816', 1, '000', '0'),
(5, 'pbkdf2_sha256$1000000$4MGWSqkzc9YQ9PW57wa9gH$LzFu1aDwVE/X/iLd1Qu6CbzNBrDjpraKcJt/OesgCTc=', NULL, 'kemal@email.com', '2025-08-02 18:21:46.990981', 'kemal@email.com', 'kemal', 'Executive', 0, 1, 1, 'profile_pic/team-1.jpg', '0', '2025-08-02 18:21:46.991011', 6, '000', '0'),
(6, 'pbkdf2_sha256$1000000$FVJ06W5d0vjn8dNhyx3rzb$Qko9rXrrkvs1zlMscLiCdQpABamoPovFL/Gwey2CpWc=', NULL, 'documentation.officer@gmail.com', '2025-08-02 18:22:43.909480', 'documentation.officer@gmail.com', 'Documentation', 'Officer', 0, 1, 1, 'profile_pic/team-4.jpg', '0', '2025-08-02 18:22:43.909510', 5, '000', '0'),
(7, 'pbkdf2_sha256$1000000$QxHzswxSGBFnExryhKVVaI$ZzcgFWMMQFhN/b3iv8ADJgoqQQWSajcQ5ERgKaYMo60=', NULL, 'workunit.officer@gmail.com', '2025-08-02 18:23:53.651506', 'workunit.officer@gmail.com', 'Workunit', 'Officer', 0, 1, 1, 'profile_pic/team-3.jpg', '0', '2025-08-02 18:23:53.651534', 7, '000', '0');

-- --------------------------------------------------------

--
-- Table structure for table `users_groups`
--

CREATE TABLE `users_groups` (
  `id` bigint NOT NULL,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_user_permissions`
--

CREATE TABLE `users_user_permissions` (
  `id` bigint NOT NULL,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `woreda`
--

CREATE TABLE `woreda` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `workunit`
--

CREATE TABLE `workunit` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `zone`
--

CREATE TABLE `zone` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `soft_delete` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `kebele`
--
ALTER TABLE `kebele`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nation`
--
ALTER TABLE `nation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notifiable_user`
--
ALTER TABLE `notifiable_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `region`
--
ALTER TABLE `region`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `system_notification`
--
ALTER TABLE `system_notification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `users_user_roles_id_b21b4fb3_fk_role_id` (`user_roles_id`);

--
-- Indexes for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_groups_customuser_id_group_id_927de924_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_groups_group_id_2f3517aa_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_permissions_customuser_id_permission_id_2b4e4e39_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `woreda`
--
ALTER TABLE `woreda`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `workunit`
--
ALTER TABLE `workunit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zone`
--
ALTER TABLE `zone`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `kebele`
--
ALTER TABLE `kebele`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nation`
--
ALTER TABLE `nation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notifiable_user`
--
ALTER TABLE `notifiable_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `region`
--
ALTER TABLE `region`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `system_notification`
--
ALTER TABLE `system_notification`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users_groups`
--
ALTER TABLE `users_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `woreda`
--
ALTER TABLE `woreda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `workunit`
--
ALTER TABLE `workunit`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `zone`
--
ALTER TABLE `zone`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_user_roles_id_b21b4fb3_fk_role_id` FOREIGN KEY (`user_roles_id`) REFERENCES `role` (`id`);

--
-- Constraints for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD CONSTRAINT `users_groups_customuser_id_4bd991a9_fk_users_id` FOREIGN KEY (`customuser_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_groups_group_id_2f3517aa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD CONSTRAINT `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_user_permissions_customuser_id_efdb305c_fk_users_id` FOREIGN KEY (`customuser_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
