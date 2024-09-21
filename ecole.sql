-- Active: 1726748712633@@127.0.0.1@3306@ecole
-- Création de la base de données
CREATE DATABASE Ecole;
USE Ecole;

-- Création de la table des étudiants
CREATE TABLE etudiants (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(100),
    nom VARCHAR(100),
    numero_salle INT,
    telephone VARCHAR(15),
    email VARCHAR(100),
    annee_obtention YEAR,
    numero_classe INT
);

-- Création de la table des enseignants
CREATE TABLE enseignants (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(100),
    nom VARCHAR(100),
    numero_salle INT,
    departement VARCHAR(100),
    annee_obtention YEAR,
    email VARCHAR(100),
    telephone VARCHAR(15),
    numero_classe INT
);

-- Insertions 
INSERT INTO etudiants (prenom, nom, telephone, annee_obtention, numero_classe)
VALUES ('Mark', 'Watney', '777-555-1234', 2035, 5);


INSERT INTO enseignants (prenom, nom, departement, email, telephone, numero_classe)
VALUES ('Jonas', 'Salk', 'Biologie', 'jsalk@school.org', '777-555-4321', 5);


SELECT * FROM enseignants

SELECT * FROM etudiants