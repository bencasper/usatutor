-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema usa_tutor
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema usa_tutor
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usa_tutor` DEFAULT CHARACTER SET utf8mb4 ;
USE `usa_tutor` ;

-- -----------------------------------------------------
-- Table `usa_tutor`.`user_memeber_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`user_memeber_info` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`user_memeber_info` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(100) NOT NULL DEFAULT '',
  `user_phone` VARCHAR(20) NOT NULL DEFAULT '',
  `user_role_id` INT UNSIGNED NOT NULL,
  `is_tutor` TINYINT(4) UNSIGNED NOT NULL DEFAULT 0 COMMENT '是否tutor 0 否 1 是',
  `user_profile_url` VARCHAR(255) NOT NULL COMMENT '用户头像\n',
  `user_wx_openid` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '微信openid',
  `user_wx_unionid` VARCHAR(100) NOT NULL COMMENT '微信unionid',
  `register_time` DATETIME NOT NULL COMMENT '注册时间',
  `user_introduce` VARCHAR(255) NOT NULL COMMENT '自我介绍',
  `is_active` TINYINT(4) UNSIGNED NOT NULL DEFAULT 1 COMMENT '是否有效 1有效 0无效',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '注册用户基本信息';

CREATE UNIQUE INDEX `id_UNIQUE` ON `usa_tutor`.`user_memeber_info` (`id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `usa_tutor`.`user_role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`user_role` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`user_role` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(100) NOT NULL DEFAULT '',
  `role_desc` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '角色描述',
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '用户角色\n';

CREATE UNIQUE INDEX `id_UNIQUE` ON `usa_tutor`.`user_role` (`id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `usa_tutor`.`user_tutor_schedule`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`user_tutor_schedule` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`user_tutor_schedule` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tutor_id` INT UNSIGNED NOT NULL,
  `start_at` TIME NOT NULL COMMENT '开始时间',
  `end_at` TIME NOT NULL COMMENT '结束时间',
  `due_date` DATE NOT NULL,
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '教师课程安排\n';


-- -----------------------------------------------------
-- Table `usa_tutor`.`sale_order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`sale_order` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`sale_order` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_no` VARCHAR(45) NOT NULL DEFAULT '' COMMENT '订单编号',
  `tutor_id` INT UNSIGNED NOT NULL COMMENT '教师id',
  `tutor_name` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '教师用户名',
  `student_id` INT NOT NULL,
  `student_name` VARCHAR(100) NOT NULL DEFAULT '',
  `order_status` TINYINT(2) NOT NULL COMMENT '订单状态 1:待付款 2:已付款 3:已取消 4:履约中 6:履约完成 7:申请退款 8:已退款',
  `total_original_amount` DECIMAL(10,2) NOT NULL COMMENT '原价',
  `total_due_amount` DECIMAL(10,2) NOT NULL COMMENT '应付',
  `total_discount_amount` DECIMAL(10,2) NOT NULL COMMENT '折扣总金额',
  `total_paid_amount` DECIMAL(10,2) NOT NULL COMMENT '实付',
  `paid_time` DATETIME NOT NULL COMMENT '支付时间',
  `total_refundable_amount` DECIMAL(10,2) NOT NULL COMMENT '总可退款金额',
  `total_refunded_amount` DECIMAL(10,2) NOT NULL COMMENT '总已退款金额',
  `refund_status` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '退款状态 1 退款中 2 退款成功 3 退款失败',
  `refund_apply_time` DATETIME NULL,
  `refunded_time` DATETIME NULL COMMENT '退款成功时间',
  `cancel_time` DATETIME NULL COMMENT '取消时间',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '订单';

CREATE UNIQUE INDEX `id_UNIQUE` ON `usa_tutor`.`sale_order` (`id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `usa_tutor`.`sale_order_course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`sale_order_course` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`sale_order_course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `course_id` INT NOT NULL COMMENT '课程id',
  `course_name` VARCHAR(100) NOT NULL,
  `course_level_id` INT NOT NULL COMMENT '课程级别\n',
  `course_level_name` VARCHAR(45) NULL,
  `course_begin_time` DATETIME NOT NULL,
  `couse_end_time` DATETIME NOT NULL,
  `couse_tutor_id` INT NOT NULL,
  `couse_tutor_name` VARCHAR(100) NOT NULL,
  `couse_status` TINYINT(4) NOT NULL COMMENT '课程状态 1 未授课 2 已授课 3 已退课',
  `couse_income_amount` DECIMAL(10,2) NOT NULL COMMENT '课程实收',
  `couse_refundable_amount` DECIMAL(10,2) NOT NULL COMMENT '课程可退款金额',
  `couse_discount_amount` DECIMAL(10,2) NOT NULL COMMENT '课程优惠金额\n',
  `couse_refunded_amount` DECIMAL(10,2) NOT NULL COMMENT '课程已退款金额',
  `couse_refund_apply_time` DATETIME NULL,
  `couse_refunded_time` DATETIME NULL,
  `update_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '订单课程明细';


-- -----------------------------------------------------
-- Table `usa_tutor`.`sale_order_payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`sale_order_payment` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`sale_order_payment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `payment_method` TINYINT(4) NOT NULL COMMENT '支付方式 1 微信 2 支付宝',
  `payment_name` VARCHAR(100) NOT NULL COMMENT '支付方式名称',
  `due_amount` DECIMAL(10,2) NOT NULL COMMENT '应付金额',
  `paid_amount` DECIMAL(10,2) NOT NULL COMMENT '实付金额',
  `payment_status` TINYINT(4) NOT NULL DEFAULT 1 COMMENT '支付状态  1 未支付 2 已支付 3 支付失败\n',
  `thirdparty_payment_no` VARCHAR(100) NOT NULL COMMENT '三方支付流水',
  `is_refund` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '是否退款  0 否 1 是\n',
  `payment_apply_time` DATETIME NOT NULL COMMENT '支付发起时间\n',
  `payment_success_time` DATETIME NULL COMMENT '支付成功时间',
  `payment_failture_time` DATETIME NULL COMMENT '支付失败时间',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '订单支付明细';


-- -----------------------------------------------------
-- Table `usa_tutor`.`sale_order_finance`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`sale_order_finance` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`sale_order_finance` (
  `id` INT NOT NULL,
  `order_id` INT NOT NULL,
  `order_income_amount` DECIMAL(10,2) NOT NULL COMMENT '订单收入',
  `order_income_ratio` DECIMAL(10,2) NOT NULL COMMENT '订单分账比率\n',
  `thirdparty_fee_radio` DECIMAL(10,2) NOT NULL COMMENT '三方支付手续费率\n',
  `ledger_type` TINYINT(4) NOT NULL DEFAULT 1 COMMENT '分账类型 1 订单开始履约后  t+   2 订单履约结束后 t+',
  `ledger_day` TINYINT(4) NOT NULL COMMENT '分账时效  t+0',
  `self_income_amount` DECIMAL(10,2) NOT NULL COMMENT '自收入',
  `partner_due` DECIMAL(10,2) NOT NULL COMMENT '合伙方收入',
  `thirdparty_fee` DECIMAL(10,2) NULL COMMENT '三方支付手续费\n',
  `ledger_time` DATETIME NULL,
  `update_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '分账日期',
  `create_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '订单财务分账\n';


-- -----------------------------------------------------
-- Table `usa_tutor`.`textbook_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`textbook_category` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`textbook_category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(100) NOT NULL,
  `catetory_desc` VARCHAR(255) NOT NULL DEFAULT '',
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `usa_tutor`.`textbook_content`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`textbook_content` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`textbook_content` (
  `id` INT NOT NULL,
  `textbook_title` VARCHAR(100) NOT NULL COMMENT '教材名称',
  `textbook_url` VARCHAR(255) NOT NULL COMMENT '教材官方链接\n',
  `textbook_desc` VARCHAR(255) NOT NULL DEFAULT '',
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `usa_tutor`.`user_tutor_resume`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`user_tutor_resume` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`user_tutor_resume` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tutor_id` INT UNSIGNED NOT NULL,
  `resume_item` VARCHAR(255) NOT NULL COMMENT '简历项',
  `resume_order` SMALLINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '简历顺序',
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '教师简历';


-- -----------------------------------------------------
-- Table `usa_tutor`.`activity_entity`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`activity_entity` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`activity_entity` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tutor_id` INT UNSIGNED NOT NULL,
  `tutor_name` VARCHAR(100) NOT NULL,
  `student_id` INT UNSIGNED NOT NULL,
  `student_name` VARCHAR(100) NOT NULL,
  `order_id` INT UNSIGNED NOT NULL,
  `course_id` INT UNSIGNED NOT NULL,
  `course_name` VARCHAR(100) NOT NULL,
  `due_begin_time` DATETIME NOT NULL COMMENT '计划开始时间',
  `due_end_time` DATETIME NOT NULL COMMENT '计划结束时间\n',
  `webrtc_id` VARCHAR(100) NOT NULL COMMENT '视频id\n',
  `real_begin_time` DATETIME NOT NULL COMMENT '实际开始时间',
  `real_end_time` DATETIME NULL COMMENT '实际结束时间',
  `real_duration` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '授课时长（s）',
  `status` TINYINT(4) UNSIGNED NOT NULL COMMENT '授课状态 1 授课中 2 授课中断 3 授课完成',
  `tutor_score` TINYINT NOT NULL DEFAULT 10 COMMENT '教师得分',
  `student_score` TINYINT NOT NULL DEFAULT 10 COMMENT '学生得分\n',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '授课实例\n';


-- -----------------------------------------------------
-- Table `usa_tutor`.`course_level`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`course_level` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`course_level` (
  `id` INT NOT NULL,
  `level_name` VARCHAR(100) NOT NULL,
  `level_desc` VARCHAR(255) NOT NULL DEFAULT '',
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '课程等级/类型\n';


-- -----------------------------------------------------
-- Table `usa_tutor`.`course_content`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usa_tutor`.`course_content` ;

CREATE TABLE IF NOT EXISTS `usa_tutor`.`course_content` (
  `id` INT NOT NULL,
  `level_id` INT UNSIGNED NOT NULL,
  `course_name` VARCHAR(100) NOT NULL,
  `course_desc` VARCHAR(255) NOT NULL,
  `edit_by` INT NOT NULL,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`, `course_name`))
ENGINE = InnoDB
COMMENT = '课程内容';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
