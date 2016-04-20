-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 20, 2016 at 11:30 PM
-- Server version: 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Sarcina`
--

-- --------------------------------------------------------

--
-- Table structure for table `Scripts`
--

CREATE TABLE IF NOT EXISTS `Scripts` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `file_location` varchar(255) DEFAULT NULL,
  `Applications_involved` varchar(500) DEFAULT NULL,
  `Need_Sudo_Permission` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `Scripts`
--

INSERT INTO `Scripts` (`Id`, `Name`, `file_location`, `Applications_involved`, `Need_Sudo_Permission`) VALUES
(5, 'Create file', '/team4cs243/Sarcina/taskerpage/scripts/create_file.py', 'System', 0),
(6, 'Create folder', '/team4cs243/Sarcina/taskerpage/scripts/create_folder.py', 'System', 0),
(7, 'Delete file', '/team4cs243/Sarcina/taskerpage/scripts/delete_file.py', 'System', 0),
(8, 'Delete folder', '/team4cs243/Sarcina/taskerpage/scripts/delete_folder.py', 'System', 0),
(9, 'List files', '/team4cs243/Sarcina/taskerpage/scripts/ls.py', 'System', 0),
(10, 'Play-Pause Music', '/team4cs243/Sarcina/taskerpage/scripts/music.py', 'Rhythmbox', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE IF NOT EXISTS `tasks` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(100) NOT NULL,
  `task_script_address` varchar(1000) NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
