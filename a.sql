--
-- Rename field depart on userextrainfo to depart1
--
ALTER TABLE `UserExtraInfo` CHANGE `depart_id` `depart1_id` integer NOT NULL;
