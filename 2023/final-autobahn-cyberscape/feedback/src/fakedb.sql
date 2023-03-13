DROP TABLE IF EXISTS `faketable`;

CREATE TABLE `faketable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fakeuser` varchar(50) NOT NULL,
  `fakepass` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

INSERT INTO `faketable` (`id`, `fakeuser`, `fakepass`) VALUES (1, 'REDACTED', 'REDACTED');

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(50) NOT NULL,
  `comment` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'REDACTED';
