-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-08-24 09:51:11
-- 伺服器版本： 10.4.13-MariaDB
-- PHP 版本： 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `taeyeon`
--

-- --------------------------------------------------------

--
-- 資料表結構 `direction`
--

CREATE TABLE `direction` (
  `id` tinyint(1) NOT NULL,
  `direction_id` int(11) NOT NULL,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `direction`
--

INSERT INTO `direction` (`id`, `direction_id`, `name`, `description`) VALUES
(1, 0, 'gafdg', 'fsgsh'),
(2, 0, 'hhhh', 'shsfsg'),
(3, 0, 'reqrqew', 'qreqr'),
(4, 0, 'aaaa', 'aaaa');

-- --------------------------------------------------------

--
-- 資料表結構 `member`
--

CREATE TABLE `member` (
  `id` tinyint(1) NOT NULL,
  `project_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `member`
--

INSERT INTO `member` (`id`, `project_id`, `user_id`, `type`) VALUES
(6, 1, 2, 1),
(7, 1, 4, 2),
(8, 1, 5, 2),
(9, 1, 6, 2),
(10, 1, 7, 2),
(11, 1, 10, 2);

-- --------------------------------------------------------

--
-- 資料表結構 `project`
--

CREATE TABLE `project` (
  `id` tinyint(1) UNSIGNED ZEROFILL NOT NULL,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `project`
--

INSERT INTO `project` (`id`, `name`, `description`) VALUES
(1, '太妍', '唱歌'),
(2, 'IU', '唱歌');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `id` tinyint(1) UNSIGNED ZEROFILL NOT NULL,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `account` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `type` tinyint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `user`
--

INSERT INTO `user` (`id`, `name`, `account`, `password`, `type`) VALUES
(1, 'admin', 'admin', '1234', 1),
(2, 'utest1', 'test1', '1234', 2),
(4, 'utest3', 'test3', '1234', 2),
(5, 'utest4', 'test4', '1234', 2),
(6, 'utest5', 'test5', '1234', 2),
(7, 'utest6', 'test6', '1234', 2),
(10, 'utest8', 'test2', '1234', 2);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `direction`
--
ALTER TABLE `direction`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `direction`
--
ALTER TABLE `direction`
  MODIFY `id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `member`
--
ALTER TABLE `member`
  MODIFY `id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `project`
--
ALTER TABLE `project`
  MODIFY `id` tinyint(1) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user`
--
ALTER TABLE `user`
  MODIFY `id` tinyint(1) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
