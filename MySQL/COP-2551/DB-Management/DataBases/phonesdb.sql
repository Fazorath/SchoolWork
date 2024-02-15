-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 25, 2024 at 03:41 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phonesdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `adressestbl`
--

CREATE TABLE `adressestbl` (
  `addressesID` int(11) NOT NULL,
  `addressespersonFK` int(11) NOT NULL,
  `address` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `zip` char(4) NOT NULL,
  `ziptext` char(4) NOT NULL DEFAULT '0000'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `carriertbl`
--

CREATE TABLE `carriertbl` (
  `carrierID` int(11) NOT NULL,
  `carrierName` varchar(45) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `emailtbl`
--

CREATE TABLE `emailtbl` (
  `emailid` int(11) NOT NULL,
  `emailpersonfk` int(11) NOT NULL,
  `email` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `extensiontbl`
--

CREATE TABLE `extensiontbl` (
  `extid` int(11) NOT NULL,
  `extphonefk` int(11) NOT NULL,
  `ext` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `peopletbl`
--

CREATE TABLE `peopletbl` (
  `personid` int(11) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `middlename` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `prefferedfirst` varchar(20) NOT NULL,
  `persondate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `phonestbl`
--

CREATE TABLE `phonestbl` (
  `phonesId` int(11) NOT NULL,
  `phonePersonfk` int(11) NOT NULL,
  `phoneCarrierfk` int(11) NOT NULL,
  `phoneTypefk` int(11) NOT NULL,
  `phoneNumber` char(10) NOT NULL,
  `phoneDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `phonetypetbl`
--

CREATE TABLE `phonetypetbl` (
  `phonetypeid` int(11) NOT NULL,
  `phonetype` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `planstbl`
--

CREATE TABLE `planstbl` (
  `plansId` int(11) NOT NULL,
  `carrierfk` int(11) NOT NULL,
  `planName` varchar(45) NOT NULL,
  `dateStarted` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adressestbl`
--
ALTER TABLE `adressestbl`
  ADD PRIMARY KEY (`addressesID`),
  ADD KEY `addressespersonFK` (`addressespersonFK`);

--
-- Indexes for table `carriertbl`
--
ALTER TABLE `carriertbl`
  ADD PRIMARY KEY (`carrierID`);

--
-- Indexes for table `emailtbl`
--
ALTER TABLE `emailtbl`
  ADD PRIMARY KEY (`emailid`),
  ADD KEY `emailpersonfk` (`emailpersonfk`);

--
-- Indexes for table `extensiontbl`
--
ALTER TABLE `extensiontbl`
  ADD PRIMARY KEY (`extid`),
  ADD KEY `extphonefk` (`extphonefk`);

--
-- Indexes for table `peopletbl`
--
ALTER TABLE `peopletbl`
  ADD PRIMARY KEY (`personid`);

--
-- Indexes for table `phonestbl`
--
ALTER TABLE `phonestbl`
  ADD PRIMARY KEY (`phonesId`),
  ADD KEY `phonePersonfk` (`phonePersonfk`),
  ADD KEY `phoneCarrierfk` (`phoneCarrierfk`),
  ADD KEY `phoneTypefk` (`phoneTypefk`);

--
-- Indexes for table `phonetypetbl`
--
ALTER TABLE `phonetypetbl`
  ADD PRIMARY KEY (`phonetypeid`);

--
-- Indexes for table `planstbl`
--
ALTER TABLE `planstbl`
  ADD PRIMARY KEY (`plansId`),
  ADD KEY `carrierfk` (`carrierfk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adressestbl`
--
ALTER TABLE `adressestbl`
  MODIFY `addressesID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `carriertbl`
--
ALTER TABLE `carriertbl`
  MODIFY `carrierID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emailtbl`
--
ALTER TABLE `emailtbl`
  MODIFY `emailid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `extensiontbl`
--
ALTER TABLE `extensiontbl`
  MODIFY `extid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `peopletbl`
--
ALTER TABLE `peopletbl`
  MODIFY `personid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `phonestbl`
--
ALTER TABLE `phonestbl`
  MODIFY `phonesId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `phonetypetbl`
--
ALTER TABLE `phonetypetbl`
  MODIFY `phonetypeid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `planstbl`
--
ALTER TABLE `planstbl`
  MODIFY `plansId` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adressestbl`
--
ALTER TABLE `adressestbl`
  ADD CONSTRAINT `adressestbl_ibfk_1` FOREIGN KEY (`addressespersonFK`) REFERENCES `peopletbl` (`personid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `emailtbl`
--
ALTER TABLE `emailtbl`
  ADD CONSTRAINT `emailtbl_ibfk_1` FOREIGN KEY (`emailid`) REFERENCES `peopletbl` (`personid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `emailtbl_ibfk_2` FOREIGN KEY (`emailpersonfk`) REFERENCES `peopletbl` (`personid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `extensiontbl`
--
ALTER TABLE `extensiontbl`
  ADD CONSTRAINT `extensiontbl_ibfk_1` FOREIGN KEY (`extphonefk`) REFERENCES `phonestbl` (`phonesId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `phonestbl`
--
ALTER TABLE `phonestbl`
  ADD CONSTRAINT `phonestbl_ibfk_1` FOREIGN KEY (`phoneTypefk`) REFERENCES `phonetypetbl` (`phonetypeid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `phonestbl_ibfk_2` FOREIGN KEY (`phonePersonfk`) REFERENCES `peopletbl` (`personid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `phonestbl_ibfk_3` FOREIGN KEY (`phoneCarrierfk`) REFERENCES `carriertbl` (`carrierID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `planstbl`
--
ALTER TABLE `planstbl`
  ADD CONSTRAINT `planstbl_ibfk_1` FOREIGN KEY (`carrierfk`) REFERENCES `carriertbl` (`carrierID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
