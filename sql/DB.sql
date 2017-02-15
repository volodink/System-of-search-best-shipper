CREATE TABLE Considerations
(
	ID INTEGER,
	Date_of_delivery INTEGER,
	Quality INTEGER,
	ID_Reliability INTEGER,
	ID_Listing INTEGER,
	CONSTRAINT PK_considerations PRIMARY KEY (ID),
	CONSTRAINT FK_ID_Listing FOREIGN KEY (ID_Listing)
		REFERENCES Listing(ID) ,
	CONSTRAINT FK_ID_Listing FOREIGN KEY (ID_Listing)
		REFERENCES Listing(ID) ,
	CONSTRAINT FK_ID_Reliability FOREIGN KEY (ID_Reliability)
		REFERENCES Reliability(ID) 
)
;

CREATE TABLE Listing
(
	ID INTEGER,
	Name TEXT,
	Price REAL,
	Description TEXT,
	CONSTRAINT PK_Listing PRIMARY KEY (ID)
)
;

CREATE TABLE Reliability
(
	ID INTEGER,
	The_number_of_broken_supply INTEGER,
	Financial_position INTEGER,
	Number_of_clients INTEGER,
	Age INTEGER,
	The_number_of_lawsuits_now INTEGER,
	The_number_of_lawsuits_past INTEGER,
	CONSTRAINT PK_Reliability PRIMARY KEY (ID)
)
;

CREATE TABLE Suppliers
(
	ID INTEGER,
	Name TEXT,
	Email TEXT,
	Site TEXT,
	Telephone_number TEXT,
	ID_considerations INTEGER,
	CONSTRAINT PK_Suppliers PRIMARY KEY (ID),
	CONSTRAINT FK_ID_considerations FOREIGN KEY (ID_considerations)
		REFERENCES Considerations(ID) 
)
;
