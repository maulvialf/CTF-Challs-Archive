#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo "not up" && sleep .2; done

mysql -u root << EOF
CREATE DATABASE batchcraftpotions;

CREATE TABLE batchcraftpotions.users (
    id           INT                 NOT NULL AUTO_INCREMENT,
    username     VARCHAR(256) UNIQUE NOT NULL,
    password     VARCHAR(256)        NOT NULL,
    otpkey       VARCHAR(255)        NULL,
    is_admin     INTEGER             NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);


CREATE TABLE batchcraftpotions.products (
    id                INT             NOT NULL AUTO_INCREMENT,
    product_name      VARCHAR(256)    NOT NULL,
    product_desc      VARCHAR(256)    NOT NULL,
    product_price     DOUBLE          NOT NULL DEFAULT 0.00,
    product_category  INTEGER         NOT NULL,
    product_keywords  VARCHAR(256)    NOT NULL,
    product_og_title  VARCHAR(256)    NOT NULL,
    product_og_desc   VARCHAR(256)    NOT NULL,
    product_seller    VARCHAR(256)    NOT NULL,
    product_approved  INTEGER         NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO batchcraftpotions.products(
    product_name,
    product_desc,
    product_price,
    product_category,
    product_keywords,
    product_og_title,
    product_og_desc,
    product_seller,
    product_approved
)
VALUES
(
    'Fire Resistant Spell',
    '<p>Makes you immune to fire for 30 minutes.</p><p><b>Caution:</b> You loose the ability to swim for 30 minutes.</p>',
    69.42,
    4,
    'fire-resistant, fire, fire-shield',
    'Fire Resistant Spell',
    'Fire Resistant Spell',
    'admin',
    1
),
(
    'Poison Resistant Spell',
    '<p>Makes you immune to all kinds of poison for 45 minutes.</p><p><b>Caution:</b> You loose the ability to smell for 45 minutes.</p>',
    129.32,
    1,
    'poison-resistant, poison, poison-safe',
    'Poison Resistant Spell',
    'Poison Resistant Spell',
    'admin',
    1
),
(
    'Stamina Boost Spell',
    '<p>Increases lung capacity for 1 hour.</p><p><b>Caution:</b> Might cause fuzziness after the spell wears out.</p>',
    429.12,
    5,
    'stamina-boost, stamina, breath',
    'Stamina Boost Spell',
    'Stamina Boost Spell',
    'admin',
    1
)
,
(
    'Lightweight Spell',
    '<p>Decreases your weight by 90% for 35 minutes.</p><p><b>Caution:</b> vulnerable to strong wind.</p>',
    139.12,
    2,
    'stamina-boost, stamina, breath',
    'Lightweight Spell',
    'Lightweight Spell',
    'admin',
    1
)
,
(
    'Increased Vision Spell',
    '<p>Increased vision for 45 minutes.</p><p><b>Caution:</b> Wears off your stamina.</p>',
    139.12,
    3,
    'stamina-boost, stamina, breath',
    'Increased Vision Spell',
    'Increased Vision Spell',
    'admin',
    1
)
,
(
    'Forbidden Silencer Spell',
    '<p>Silence your oponent for 10 minutes by uttering their name while looking at them.</p>',
    539.12,
    6,
    'dark-spell, curse, silence, block-speech',
    'Forbidden Silencer Spell',
    'Forbidden Silencer Spell',
    'admin',
    1
);


GRANT ALL ON batchcraftpotions.* TO 'batchcraftpotions'@'%' IDENTIFIED BY 'batchcraftpotions' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EOF

/usr/bin/supervisord -c /etc/supervisord.conf
