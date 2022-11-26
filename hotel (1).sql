-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2022 at 05:02 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `book_id` bigint(20) NOT NULL,
  `room_id` bigint(20) DEFAULT NULL,
  `cust_id` bigint(20) DEFAULT NULL,
  `doo` date DEFAULT NULL,
  `dol` date DEFAULT NULL,
  `advance` float(10,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`book_id`, `room_id`, `cust_id`, `doo`, `dol`, `advance`) VALUES
(1, 1, 1, '2020-02-20', '2020-12-25', 2000.00),
(2, 2, 1, '2020-12-23', '2020-12-25', 4500.00),
(3, 4, 1, '2020-12-23', '2020-12-25', 3400.00),
(4, 1, 1, '2020-11-29', '2020-12-25', 2000.00),
(5, 1, 1, '2020-12-20', '2020-12-25', 2000.00),
(6, 1, 1, '2020-12-20', '2020-12-25', 4500.00),
(7, 1, 1, '2020-12-19', '2020-12-25', 4500.00),
(8, 1, 1, '2020-12-20', '2020-12-25', 4500.00),
(9, 1, 1, '2020-12-20', NULL, 2500.00),
(10, 2, 2, '2020-12-29', '2020-12-29', 3400.00),
(11, 10, 2, '2023-02-05', NULL, 100.00);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` bigint(20) NOT NULL,
  `name` char(50) DEFAULT NULL,
  `address` char(100) DEFAULT NULL,
  `phone` char(15) DEFAULT NULL,
  `email` char(80) DEFAULT NULL,
  `id_proof` char(20) DEFAULT NULL,
  `id_proof_no` char(25) DEFAULT NULL,
  `males` int(2) DEFAULT NULL,
  `females` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `address`, `phone`, `email`, `id_proof`, `id_proof_no`, `males`, `females`) VALUES
(1, 'rakesh kumar', 'CF-4 BRIJ VIHAR', '98718168101', 'RAKESH@GMAIL.COM', 'AADHAR CARD', '4544-5656-5656', 1, 1),
(2, 'ajmal khan', 'F-234 BRIJ VIHAR', '456465456', 'AJMAL@GMAIL.COM', 'AADHAR', '4353-4564-5675', 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(10) NOT NULL,
  `room_no` int(4) DEFAULT NULL,
  `room_type` char(20) DEFAULT NULL,
  `room_rent` float(10,2) DEFAULT NULL,
  `room_bed` char(20) DEFAULT NULL,
  `status` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `room_no`, `room_type`, `room_rent`, `room_bed`, `status`) VALUES
(1, 1, 'AC', 2500.00, 'Single Bed', 'occupied'),
(2, 2, 'AC', 2500.00, 'Single Bed', 'free'),
(3, 3, 'AC', 2500.00, 'Single Bed', 'free'),
(4, 4, 'AC', 2500.00, 'Single Bed', 'free'),
(6, 5, 'AC', 3500.00, 'Double Bed', 'free'),
(7, 6, 'AC', 3500.00, 'Double Bed', 'free'),
(8, 7, 'AC', 3500.00, 'Double Bed', 'free'),
(9, 8, 'Delux', 4500.00, 'Double Bed', 'free'),
(10, 9, 'Delux', 4500.00, 'Double Bed', 'occupied'),
(11, 10, 'Delux', 4500.00, 'Double Bed', 'free'),
(12, 10, 'Super Delux', 5500.00, 'Double Bed', 'free'),
(13, 11, 'Super Delux', 5500.00, 'Double Bed', 'free'),
(20, 17, 'Delux', 4000.00, 'Single Bed', 'free'),
(21, 18, 'Super Delux', 4500.00, 'Single Bed', 'free'),
(22, 19, 'Super Delux', 4500.00, 'Single Bed', 'free'),
(23, 20, 'AC', 2650.00, 'SINGLE', 'free'),
(24, 23, 'Non-AC', NULL, NULL, NULL),
(25, 24, 'Non-AC', NULL, NULL, NULL),
(26, 25, ' AC', 3500.00, 'SINGLE', 'free'),
(27, 40, 'AC', 1000.00, 'SINGLE', 'free'),
(28, 600, 'AC', 292.00, 'SINGLE', 'free'),
(29, 27, 'DELUX', 3000.00, 'DOUBLE', 'free');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `book_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
