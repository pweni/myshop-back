--
-- Create model DepartInfo
--
--
-- Create model UserBaseInfo
--
--
-- Create model UserExtraInfo
--
CREATE TABLE `UserExtraInfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(30) NOT NULL, `truename` varchar(30) NOT NULL, `password` varchar(20) NOT NULL, `sex` integer NOT NULL, `salary` numeric(8, 2) NOT NULL, `birthday` date NOT NULL, `age` integer NOT NULL, `email` varchar(50) NOT NULL, `department` varchar(20) NOT NULL, `status` varchar(1) NOT NULL, `createDate` datetime(6) NOT NULL, `memo` longtext NULL, `depart_id` integer NOT NULL, `user_id` integer NOT NULL UNIQUE);
--
-- Create model SkillInfo
--
CREATE TABLE `SkillInfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `skillname` varchar(30) NOT NULL, `createDate` datetime(6) NOT NULL);
CREATE TABLE `user_skill` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `skillinfo_id` integer NOT NULL, `userextrainfo_id` integer NOT NULL);
ALTER TABLE `UserExtraInfo` ADD CONSTRAINT `UserExtraInfo_depart_id_b6541f57_fk_DepartInfo_id` FOREIGN KEY (`depart_id`) REFERENCES `DepartInfo` (`id`);
ALTER TABLE `UserExtraInfo` ADD CONSTRAINT `UserExtraInfo_user_id_dbbba9c6_fk_UserBaseInfo_id` FOREIGN KEY (`user_id`) REFERENCES `UserBaseInfo` (`id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_skillinfo_id_userextrainfo_id_bb402257_uniq` UNIQUE (`skillinfo_id`, `userextrainfo_id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_skillinfo_id_c8628996_fk_SkillInfo_id` FOREIGN KEY (`skillinfo_id`) REFERENCES `SkillInfo` (`id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_userextrainfo_id_c88b7530_fk_UserExtraInfo_id` FOREIGN KEY (`userextrainfo_id`) REFERENCES `UserExtraInfo` (`id`);
