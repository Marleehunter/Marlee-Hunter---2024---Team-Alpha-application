%{
MATLAB
Author: Marlee Hunter
Notes:
  Flashcards to help students study their prefix's name and abbreviation. 
  How many prefixes the student wants to study and the abbreviation is read from input. If it is right,
  the program will say it is correct, else it will say the right abbreviation.
%}

%clearing exisiting code
clear
clc

%Pull data from the given Excel Sheet into a Table object. 
% This will contain three arrays, with the prefixes, their exponents, 
% and their abbreviations.
 metricTable = readtable("metricPrefixes.xlsx");

 %Create two separate string arrays for the names and abbreviations 
 % of the prefixes, and a numeric array for their exponents.
prefixAbbreviation = string(metricTable.abbreviation);
prefixExponents = double(metricTable.exponent);
prefixName = string(metricTable.prefix);

%Display the logo.
disp("//----------------------\\");
disp("||  METRIC FLASH CARDS  ||");
disp("\\----------------------//");

%Request the user to input how many prefixes they will review. 
% This value should be read and stored as an integer.
numPrefixes = input("How many prefixes would you like to review?: ");
numCorrectAbbrev = 0;
numCorrectExponent = 0;
storage = [];

%Repeat the following steps for the number of prefixes requested
for i = 1: numPrefixes

%Using the length of one of the arrays, generate a random integer that will
% represent the row number of a random prefix from the spreadsheet.
rowNumber = randi(length(prefixName));

%Find the name, abbreviation, and exponent of the prefix and store all 
% three as variables.
%Store the row number of the prefix in an array for later use when
% generating the summary.
rightName = prefixName(rowNumber);
rightExponent = prefixExponents(rowNumber);
rightAbbreviation = prefixAbbreviation(rowNumber);

%Report the prefix’s name to the user.
correctName = rightName;
fprintf("The metric prefix is %s\n", rightName);

%Prompt the user to input the abbreviation of the prefix.
abbrevGuess = input("What is the abbreviation?: ", "s");

%If the input is correct, display a message of congratulations.
%If the input is incorrect, display the correct answer.
if abbrevGuess == rightAbbreviation
    disp('Congratulations it is correct!');
    numCorrectAbbrev = numCorrectAbbrev + 1;

%otherwise display the correct answer
else
    fprintf("Incorrect, the right answer is %s. \n", rightAbbreviation);
end

%Prompt the user to input the exponent of the prefix.
exponentGuess = input("What is the exponent?: ");

%If the input is correct, display a message of congratulations.
%If the input is incorrect, display the correct answer.
if exponentGuess == rightExponent
    disp('Congratulations it is correct!');
    numCorrectExponent = numCorrectExponent + 1;

%otherwise display the correct answer
else
    fprintf("Incorrect, the right answer is %.0f. \n", rightExponent);
end

%Pause the script for .5 seconds to give the student a short break, 
% then print a blank line.
pause(.5)
fprintf("  \n")
storage = [storage, rowNumber];
end

%Abbreviations and exponent's correctness
percentNumCorrectAbbrev = ((numCorrectAbbrev / numPrefixes) * 100);
percentNumCorrectExponent = ((numCorrectExponent / numPrefixes) * 100);


%Determine whether or not the user has reviewed any prefixes. 
% If not, display a message which says: "No prefixes were reviewed." 
% Otherwise, display a score report as follows: 
if numPrefixes <= 0 
    disp("No prefixes were reviewed.")
else

disp("//-------------------------------------------\\")
disp("|| SESSION REVIEW                            ||")
disp("||-------------------------------------------||")
fprintf("|| Number of Prefixes Reviewed:   %-2.0f         || \n", ...
    numPrefixes)
fprintf("|| Correct Abbreviations:    %-1.f (%5.1f%%)      || \n", ...
    numCorrectAbbrev, percentNumCorrectAbbrev)
fprintf("|| Correct Exponents:        %-1.f (%5.1f%%)      || \n", ...
    numCorrectExponent, percentNumCorrectExponent)
disp("||-------------------------------------------||")
disp("|| REVIEWED PREFIXES                         ||")
disp("||-------------------------------------------||")

for i = 1: numPrefixes
    fprintf("|| %-5s %-3s 10^%-3d                          || \n", ...
        prefixName(storage(i)), prefixAbbreviation(storage(i)), ... 
        prefixExponents(storage(i)))
end
disp("||-------------------------------------------||")
disp(" ")
end

%Ending the program with a message
disp("Thank you for using Metric Flash Cards!")











