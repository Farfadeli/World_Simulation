-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 08 oct. 2025 à 14:35
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `world_simulation`
--

-- --------------------------------------------------------

--
-- Structure de la table `couple`
--

CREATE TABLE `couple` (
  `uuid` varchar(32) NOT NULL,
  `first_human` varchar(32) NOT NULL,
  `second_human` varchar(32) NOT NULL,
  `simulation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `human`
--

CREATE TABLE `human` (
  `uuid` varchar(32) NOT NULL,
  `simulation_id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `health` varchar(16) NOT NULL,
  `sexuality` char(1) NOT NULL,
  `is_gay` tinyint(1) NOT NULL DEFAULT 0,
  `in_couple` tinyint(1) NOT NULL DEFAULT 0,
  `birth_date` date NOT NULL,
  `death_date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `simulation`
--

CREATE TABLE `simulation` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `fertility_rate` float(5,2) NOT NULL DEFAULT 0.00,
  `send_adoption_rate` float(5,2) NOT NULL DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `couple`
--
ALTER TABLE `couple`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `fk_first_human` (`first_human`),
  ADD KEY `fk_second_human` (`second_human`),
  ADD KEY `fk_couple_simulation_id` (`simulation_id`);

--
-- Index pour la table `human`
--
ALTER TABLE `human`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `fk_simulation_id` (`simulation_id`);

--
-- Index pour la table `simulation`
--
ALTER TABLE `simulation`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `simulation`
--
ALTER TABLE `simulation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `couple`
--
ALTER TABLE `couple`
  ADD CONSTRAINT `fk_couple_simulation_id` FOREIGN KEY (`simulation_id`) REFERENCES `simulation` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_first_human` FOREIGN KEY (`first_human`) REFERENCES `human` (`uuid`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_second_human` FOREIGN KEY (`second_human`) REFERENCES `human` (`uuid`) ON DELETE CASCADE;

--
-- Contraintes pour la table `human`
--
ALTER TABLE `human`
  ADD CONSTRAINT `fk_simulation_id` FOREIGN KEY (`simulation_id`) REFERENCES `simulation` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
