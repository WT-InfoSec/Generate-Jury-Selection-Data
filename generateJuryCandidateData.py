# generateJuryCandidateData.py 
# Will Taylor
# 09/27/2019

# CSV HEADING
# Candidate_ID, Name, Age, Address, Exempt List, Checked In


import random
import csv


def main():
	jurySummonsCSV = createCandidateProfiles()
	print(jurySummonsCSV)

def createCandidateProfiles():
	output = ""
	candidateNumbers = getJuryCandidateNumbers()
	candidateNames = createCandidateList()
	for i in range(len(candidateNumbers)):
		number = candidateNumbers[i]
		name = candidateNames[i]
		age = getRandomAge()
		address = getCandidateAddress()
		exemptList = getExemptList(age)
		checkedIn = "True"
		output += formatCandidateProfile(number, name, age, address,
						 exemptList, checkedIn)
	return output


def formatCandidateProfile(candidateNumber, name, age, 
			   address, exemptList, checkedIn):
	canID = "j"+str(candidateNumber)
	return "%s, %s, %s, %s, %s, %s\n" % (canID, name, str(age), 
					     address, exemptList, checkedIn)


def createCandidateList():
	candidateNames = list()
	with open('juryNames.txt') as juryNames:
		csv_reader = csv.reader(juryNames, delimiter=',')
		for row in juryNames:
			name = row
			candidateNames.append(name.strip())
		return candidateNames

def createStreetList():
	streetNames = list()
	with open('most-common-nouns-english.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		lineCount = 0
		for row in csv_reader:
			if (lineCount > 0):
				streetNames.append(row[0])
			lineCount += 1
	return streetNames

def getRandomStreet():
	streetList = createStreetList()
	index = random.randint(0,len(streetList)-1)
	return streetList[index]

def getRandomStreetSuffix():
	endings = ['Ct', 'Rd', 'St', 'Blvd', 'Ave', 'Way', 'Dr']
	index = random.randint(0,len(endings)-1)
	return endings[index].lower()

def getCandidateAddress():
	return (str(getRandomStreetNumber()) + " " 
			  + getRandomStreet() + " " 
			  + getRandomStreetSuffix())

def getExemptList(age):
	# Add age exemption if over 70
	if age >= 70:
		return "[True, False, False, False, False, False, False, False]"
	else:
		return "[False, False, False, False, False, False, False, False]"


def getJuryCandidateNumbers():
	numStart, numEnd = 6823, 8023
	summoned = range(numStart, numEnd)
	return summoned


def getRandomStreetNumber():
	validAddresses = range(100,10000)
	index = random.randint(0,len(validAddresses)-1)
	return validAddresses[index]

def getRandomAge():
	validAges = range(18,76)
	index = random.randint(0, len(validAges)-1)
	return validAges[index]


main()
