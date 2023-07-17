
DROP TABLE IF EXISTS Applicants;

CREATE TABLE Applicants
	(CWL VARCHAR(125) NOT NULL,
	ShibStudentNumber INT(10) NOT NULL,
	ShibFirstName VARCHAR(125) NOT NULL,
	ShibLastName VARCHAR(125) NOT NULL,
	FirstName VARCHAR(125) NOT NULL,
	LastName VARCHAR(125) NOT NULL,
	ID INT(10) NOT NULL,
	CurrentInstitution VARCHAR(125) NOT NULL, 
	Phone VARCHAR(125) NULL,
	UBCEmail VARCHAR(125) NULL, 
	Email VARCHAR(125) NULL,
	Birthday DATE NULL,
	FirstApp VARCHAR(125) NULL,
	NumberOfApps VARCHAR(125) NULL,
	Aboriginal VARCHAR(125) NULL,
	AboriginalIdentity VARCHAR(125) NULL,
	ApplicationNumber VARCHAR(125) NULL,
	FilePath VARCHAR(125) NULL,
	CreateDate DATE NOT NULL,
	PRIMARY KEY (CWL));
	