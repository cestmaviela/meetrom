-- =================================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：数据库创建文件
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- =================================================================================
-- 创建数据库
DROP DATABASE IF EXISTS bounty;
CREATE DATABASE bounty character set utf8;
USE bounty;
SET NAMES 'utf8';

-- 创建用户信息数据表
USE bounty;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	name VARCHAR(255) NOT NULL UNIQUE, -- 用户注册姓名
	pwd VARCHAR(255) NOT NULL, -- 用户注册密码
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 用户注册时间
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

-- 创建节点信息数据表
USE bounty;
DROP TABLE IF EXISTS node_info;
CREATE TABLE node_info (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	node_id INT(10) NOT NULL UNIQUE, -- 地址节点信息
	parent_id INT(10) NOT NULL  DEFAULT 0, -- 地址父节点信息
	name VARCHAR(255) NOT NULL UNIQUE, -- 地址名称
	link_name VARCHAR(2048), -- 地址链接名
	addris BOOL NULL DEFAULT FALSE, -- 地址差别标志
	category TINYINT(4)  NOT NULL DEFAULT 3, -- 城市级别，1:一线城市，2:二线城市，3:三线城市，4:四线城市，默认为三线城市
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 地址创建时间
	UNIQUE KEY (`node_id`,`name`), -- 地址与节点编号唯一对应
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

-- 创建房产中介信息表
USE bounty;
DROP TABLE IF EXISTS estate_agents;
CREATE TABLE estate_agents (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	name VARCHAR(255) NOT NULL UNIQUE, -- 房产中介名称
	level TINYINT(4) NOT NULL DEFAULT 1, -- 房产中介布局等级信息
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 用户注册时间
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
 

